import os
import json
import base64
import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Obsidian Vault Reader")

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
VAULT_REPOS = json.loads(os.environ.get("VAULT_REPOS", "[]"))

HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}


def resolve_repo(vault: str):
    """Find repo config by name or repo slug. Falls back to first."""
    for r in VAULT_REPOS:
        if not vault:
            return r
        if r["name"].lower() == vault.lower() or r["repo"].lower() == vault.lower():
            return r
    return VAULT_REPOS[0] if VAULT_REPOS else None


@mcp.tool()
async def list_vaults() -> str:
    """List all Obsidian vaults connected to this server."""
    if not VAULT_REPOS:
        return "No vaults configured."
    return "\n".join(f"- {r['name']} ({r['owner']}/{r['repo']})" for r in VAULT_REPOS)


@mcp.tool()
async def list_files(path: str = "", vault: str = "") -> str:
    """
    List files and folders in a vault directory.
    Args:
        path: Folder path relative to vault root. Leave empty for root.
        vault: Vault name (e.g. 'EE-Vault'). Defaults to first vault.
    """
    repo = resolve_repo(vault)
    if not repo:
        return "No vault configured."

    url = f"https://api.github.com/repos/{repo['owner']}/{repo['repo']}/contents/{path}"
    async with httpx.AsyncClient(timeout=15) as client:
        r = await client.get(url, headers=HEADERS)

    if r.status_code == 404:
        return f"Path not found: {path or '(root)'}"
    if r.status_code != 200:
        return f"GitHub error {r.status_code}: {r.text[:200]}"

    items = r.json()
    if isinstance(items, dict):
        return f"That path is a file, not a folder. Use read_note to read it."

    output = [f"📂 {repo['name']}/{path or ''}"]
    for item in sorted(items, key=lambda x: (x["type"] != "dir", x["name"])):
        if item["name"].startswith("."):
            continue
        icon = "📁" if item["type"] == "dir" else "📄"
        output.append(f"  {icon} {item['path']}")

    return "\n".join(output)


@mcp.tool()
async def read_note(path: str, vault: str = "") -> str:
    """
    Read the full contents of a note.
    Args:
        path: File path relative to vault root (e.g. 'Notes/MyNote.md')
        vault: Vault name. Defaults to first vault.
    """
    repo = resolve_repo(vault)
    if not repo:
        return "No vault configured."

    url = f"https://api.github.com/repos/{repo['owner']}/{repo['repo']}/contents/{path}"
    async with httpx.AsyncClient(timeout=15) as client:
        r = await client.get(url, headers=HEADERS)

    if r.status_code == 404:
        return f"Note not found: {path}"
    if r.status_code != 200:
        return f"GitHub error {r.status_code}"

    data = r.json()
    if data.get("encoding") == "base64":
        try:
            content = base64.b64decode(data["content"]).decode("utf-8")
            return f"--- {repo['name']}/{path} ---\n\n{content}"
        except Exception as e:
            return f"Decode error: {e}"
    return "Could not read file content."


@mcp.tool()
async def search_vault(query: str, vault: str = "") -> str:
    """
    Search for notes containing a query string.
    Args:
        query: Search terms
        vault: Vault name. Defaults to first vault.
    Note: GitHub indexes code with some delay. Recent commits may not appear immediately.
    """
    repo = resolve_repo(vault)
    if not repo:
        return "No vault configured."

    url = "https://api.github.com/search/code"
    params = {
        "q": f"{query} repo:{repo['owner']}/{repo['repo']}",
        "per_page": 15,
    }
    async with httpx.AsyncClient(timeout=20) as client:
        r = await client.get(url, headers=HEADERS, params=params)

    if r.status_code == 422:
        return "Search query too short or invalid."
    if r.status_code != 200:
        return f"Search error {r.status_code}: {r.text[:200]}"

    data = r.json()
    items = data.get("items", [])
    if not items:
        return f"No results for '{query}' in {repo['name']}."

    lines = [f"Search: '{query}' in {repo['name']} — {data['total_count']} result(s)\n"]
    for item in items:
        lines.append(f"📄 {item['path']}")

    return "\n".join(lines)


@mcp.tool()
async def get_vault_structure(vault: str = "", depth: int = 2) -> str:
    """
    Get a high-level overview of vault folder structure.
    Args:
        vault: Vault name. Defaults to first vault.
        depth: How many levels deep (1-3). Default 2.
    """
    repo = resolve_repo(vault)
    if not repo:
        return "No vault configured."

    depth = max(1, min(depth, 3))

    async def list_dir(path: str, current_depth: int) -> list[str]:
        url = f"https://api.github.com/repos/{repo['owner']}/{repo['repo']}/contents/{path}"
        async with httpx.AsyncClient(timeout=15) as client:
            r = await client.get(url, headers=HEADERS)
        if r.status_code != 200:
            return []
        items = r.json()
        if not isinstance(items, list):
            return []

        lines = []
        indent = "  " * current_depth
        for item in sorted(items, key=lambda x: (x["type"] != "dir", x["name"])):
            if item["name"].startswith("."):
                continue
            if item["type"] == "dir":
                lines.append(f"{indent}📁 {item['name']}/")
                if current_depth < depth:
                    sub = await list_dir(item["path"], current_depth + 1)
                    lines.extend(sub)
            else:
                lines.append(f"{indent}📄 {item['name']}")
        return lines

    lines = [f"📂 {repo['name']} vault structure (depth {depth})"]
    lines.extend(await list_dir("", 1))
    return "\n".join(lines)


@mcp.tool()
async def write_note(path: str, content: str, vault: str = "", commit_message: str = "") -> str:
    """
    Create or update a note in the vault.
    Args:
        path: File path relative to vault root (e.g. 'UNDOXXING/Samsung-TV.md')
        content: Full markdown content to write
        vault: Vault name. Defaults to first vault.
        commit_message: Optional git commit message. Auto-generated if omitted.
    """
    repo = resolve_repo(vault)
    if not repo:
        return "No vault configured."

    url = f"https://api.github.com/repos/{repo['owner']}/{repo['repo']}/contents/{path}"

    # Check if file exists to get its SHA (required for updates)
    sha = None
    async with httpx.AsyncClient(timeout=15) as client:
        r = await client.get(url, headers=HEADERS)
        if r.status_code == 200:
            sha = r.json().get("sha")

    encoded = base64.b64encode(content.encode("utf-8")).decode("utf-8")
    msg = commit_message or f"{'Update' if sha else 'Create'} {path.split('/')[-1]}"

    payload = {"message": msg, "content": encoded}
    if sha:
        payload["sha"] = sha

    async with httpx.AsyncClient(timeout=15) as client:
        r = await client.put(url, headers=HEADERS, json=payload)

    if r.status_code in (200, 201):
        action = "Updated" if sha else "Created"
        return f"{action}: {repo['name']}/{path}"
    return f"Write error {r.status_code}: {r.text[:200]}"

if __name__ == "__main__":
    import uvicorn
    app = mcp.streamable_http_app()
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))

import os
import json
import base64
import httpx
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
VAULT_REPOS = json.loads(os.environ.get("VAULT_REPOS", "[]"))

GH_HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}

TOOLS = [
    {
        "name": "list_vaults",
        "description": "List all connected Obsidian vaults.",
        "inputSchema": {"type": "object", "properties": {}},
    },
    {
        "name": "list_files",
        "description": "List files and folders in a vault directory.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "vault": {"type": "string", "description": "Vault name (e.g. EE-Vault). Defaults to first vault."},
                "path": {"type": "string", "description": "Folder path relative to vault root. Leave empty for root."},
            },
        },
    },
    {
        "name": "read_note",
        "description": "Read the full contents of a note.",
        "inputSchema": {
            "type": "object",
            "required": ["path"],
            "properties": {
                "path": {"type": "string", "description": "File path relative to vault root (e.g. Notes/MyNote.md)"},
                "vault": {"type": "string", "description": "Vault name. Defaults to first vault."},
            },
        },
    },
    {
        "name": "search_vault",
        "description": "Search for notes containing a query string.",
        "inputSchema": {
            "type": "object",
            "required": ["query"],
            "properties": {
                "query": {"type": "string", "description": "Search terms"},
                "vault": {"type": "string", "description": "Vault name. Defaults to first vault."},
            },
        },
    },
    {
        "name": "get_vault_structure",
        "description": "Get a high-level overview of vault folder structure.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "vault": {"type": "string", "description": "Vault name. Defaults to first vault."},
                "depth": {"type": "integer", "description": "How many levels deep (1-3). Default 2."},
            },
        },
    },
    {
        "name": "write_note",
        "description": "Create or update a note in the vault.",
        "inputSchema": {
            "type": "object",
            "required": ["path", "content"],
            "properties": {
                "path": {"type": "string", "description": "File path relative to vault root"},
                "content": {"type": "string", "description": "Full markdown content to write"},
                "vault": {"type": "string", "description": "Vault name. Defaults to first vault."},
                "commit_message": {"type": "string", "description": "Git commit message (optional)"},
            },
        },
    },
]


def resolve_repo(vault: str = ""):
    for r in VAULT_REPOS:
        if not vault:
            return r
        if r["name"].lower() == vault.lower() or r["repo"].lower() == vault.lower():
            return r
    return VAULT_REPOS[0] if VAULT_REPOS else None


async def call_tool(name: str, args: dict) -> str:
    vault = args.get("vault", "")
    repo = resolve_repo(vault)

    if name == "list_vaults":
        if not VAULT_REPOS:
            return "No vaults configured."
        return "\n".join(f"- {r['name']} ({r['owner']}/{r['repo']})" for r in VAULT_REPOS)

    if not repo:
        return "No vault configured."

    if name == "list_files":
        path = args.get("path", "")
        url = f"https://api.github.com/repos/{repo['owner']}/{repo['repo']}/contents/{path}"
        async with httpx.AsyncClient(timeout=15) as client:
            r = await client.get(url, headers=GH_HEADERS)
        if r.status_code == 404:
            return f"Path not found: {path or '(root)'}"
        if r.status_code != 200:
            return f"GitHub error {r.status_code}"
        items = r.json()
        if isinstance(items, dict):
            return "That path is a file. Use read_note to read it."
        lines = [f"Vault: {repo['name']}/{path or '(root)'}"]
        for item in sorted(items, key=lambda x: (x["type"] != "dir", x["name"])):
            if item["name"].startswith("."):
                continue
            icon = "D" if item["type"] == "dir" else "F"
            lines.append(f"  [{icon}] {item['path']}")
        return "\n".join(lines)

    if name == "read_note":
        path = args.get("path", "")
        url = f"https://api.github.com/repos/{repo['owner']}/{repo['repo']}/contents/{path}"
        async with httpx.AsyncClient(timeout=15) as client:
            r = await client.get(url, headers=GH_HEADERS)
        if r.status_code == 404:
            return f"Note not found: {path}"
        if r.status_code != 200:
            return f"GitHub error {r.status_code}"
        data = r.json()
        if data.get("encoding") == "base64":
            content = base64.b64decode(data["content"]).decode("utf-8")
            return f"--- {repo['name']}/{path} ---\n\n{content}"
        return "Could not read file."

    if name == "search_vault":
        query = args.get("query", "")
        url = "https://api.github.com/search/code"
        params = {"q": f"{query} repo:{repo['owner']}/{repo['repo']}", "per_page": 15}
        async with httpx.AsyncClient(timeout=20) as client:
            r = await client.get(url, headers=GH_HEADERS, params=params)
        if r.status_code != 200:
            return f"Search error {r.status_code}: {r.text[:200]}"
        data = r.json()
        items = data.get("items", [])
        if not items:
            return f"No results for '{query}' in {repo['name']}."
        lines = [f"'{query}' in {repo['name']} -- {data['total_count']} result(s)"]
        for item in items:
            lines.append(f"  [F] {item['path']}")
        return "\n".join(lines)

    if name == "get_vault_structure":
        depth = max(1, min(args.get("depth", 2), 3))

        async def list_dir(path, current_depth):
            url = f"https://api.github.com/repos/{repo['owner']}/{repo['repo']}/contents/{path}"
            async with httpx.AsyncClient(timeout=15) as client:
                r = await client.get(url, headers=GH_HEADERS)
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
                    lines.append(f"{indent}[D] {item['name']}/")
                    if current_depth < depth:
                        lines.extend(await list_dir(item["path"], current_depth + 1))
                else:
                    lines.append(f"{indent}[F] {item['name']}")
            return lines

        lines = [f"Vault: {repo['name']} (depth {depth})"]
        lines.extend(await list_dir("", 1))
        return "\n".join(lines)

    if name == "write_note":
        path = args.get("path", "")
        content = args.get("content", "")
        commit_message = args.get("commit_message", "")
        url = f"https://api.github.com/repos/{repo['owner']}/{repo['repo']}/contents/{path}"
        sha = None
        async with httpx.AsyncClient(timeout=15) as client:
            r = await client.get(url, headers=GH_HEADERS)
            if r.status_code == 200:
                sha = r.json().get("sha")
        encoded = base64.b64encode(content.encode("utf-8")).decode("utf-8")
        msg = commit_message or f"{'Update' if sha else 'Create'} {path.split('/')[-1]}"
        payload = {"message": msg, "content": encoded}
        if sha:
            payload["sha"] = sha
        async with httpx.AsyncClient(timeout=15) as client:
            r = await client.put(url, headers=GH_HEADERS, json=payload)
        if r.status_code in (200, 201):
            return f"{'Updated' if sha else 'Created'}: {repo['name']}/{path}"
        return f"Write error {r.status_code}: {r.text[:200]}"

    return f"Unknown tool: {name}"


@app.post("/mcp")
async def mcp_handler(request: Request):
    body = await request.json()
    method = body.get("method")
    params = body.get("params", {})
    req_id = body.get("id")

    if method == "initialize":
        return JSONResponse({
            "jsonrpc": "2.0", "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "vault-mcp", "version": "1.0.0"},
            },
        })

    if method in ("notifications/initialized", "ping"):
        return JSONResponse({"jsonrpc": "2.0", "id": req_id, "result": {}})

    if method == "tools/list":
        return JSONResponse({
            "jsonrpc": "2.0", "id": req_id,
            "result": {"tools": TOOLS},
        })

    if method == "tools/call":
        tool_name = params.get("name")
        arguments = params.get("arguments", {})
        result = await call_tool(tool_name, arguments)
        return JSONResponse({
            "jsonrpc": "2.0", "id": req_id,
            "result": {"content": [{"type": "text", "text": result}]},
        })

    return JSONResponse({
        "jsonrpc": "2.0", "id": req_id,
        "error": {"code": -32601, "message": f"Method not found: {method}"},
    })


@app.get("/health")
async def health():
    return {"status": "ok", "vaults": [r["name"] for r in VAULT_REPOS]}


if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

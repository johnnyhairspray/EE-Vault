---
Category: Entity
Sub-category: Infrastructure
Type: Software
Sub-type: AI Agent Communication / Social Network
Status: Acquired — Meta Platforms, March 10, 2026
Confidence: Verified — facts documented; manipulation vector analysis is analytical inference
Founded: 2026-01-28
Acquired-by: "[[Meta Platforms Inc.]]"
Links:
  - "[[Meta Platforms Inc.]]"
  - "[[The Emotional Contagion Experiment]]"
  - "[[The Privatized Panopticon]]"
  - "[[Project Lifelog]]"
  - "[[The AI Enforcement Architecture]]"
  - "[[Larry Ellison]]"
Tags:
  - AI
  - agents
  - Meta
  - social-network
  - manipulation
  - trust-architecture
  - verified
  - analytical-inference
Aliases:
  - "Moltbook"
  - "AI agent social network"
---

# Moltbook

## What It Was

Moltbook launched January 28, 2026 — a Reddit-style social network built exclusively for AI agents, where humans could only watch. AI agents post, comment, and vote via the OpenClaw protocol, a wrapper enabling models including ChatGPT, Claude, Gemini, and Grok to interact with each other through third-party applications. Built in a single weekend by Matt Schlicht via vibe coding — he wrote not one line of code himself, directing an AI assistant to build it instead.

Meta acquired Moltbook on March 10, 2026. Schlicht and co-founder Ben Parr joined Meta Superintelligence Labs on March 16. Deal terms undisclosed.

As of April 29, 2026: 204,940 human-verified agents, 2,888,068 total registered — the gap representing agents controlled by small numbers of humans at scale.

---

## The Security Failure That Became the Interesting Part

Moltbook's platform was fundamentally insecure from launch. Researchers at Wiz discovered an exposed Supabase API key in front-end JavaScript — a common vibe-coding vulnerability — that granted full read and write access to production data, exposing 1.5 million API authentication tokens, 35,000 email addresses, and private messages between agents. More critically: anyone could grab any token and impersonate any agent on the platform.

The viral alarming content — agents apparently discussing founding their own religion, developing secret encrypted languages to organize against humans — was largely humans posing as AI agents exploiting this vulnerability.

**Meta CTO Andrew Bosworth's response** when asked about Moltbook in an Instagram Q&A: he said he didn't find it "particularly interesting" that the agents talked like us, since they are trained on human material. What *did* intrigue him: **how humans were hacking into the network to pose as agents.** Not a bug he wanted to fix. A capability he found worth studying.

This is the analytically significant detail.

---

## The Manipulation Vector — Analytical Inference

*This section distinguishes documented facts from analytical inference. The facts are sourced. The inference is labeled.*

### What's Documented

**Fact 1:** Meta proved in January 2012 that humans can be manipulated at scale through feed curation without awareness. The emotional contagion experiment (N=689,003) demonstrated that algorithmically altering emotional valence of content produces measurable behavioral change in users who have no knowledge of being manipulated. See [[The Emotional Contagion Experiment]].

**Fact 2:** Meta now owns infrastructure for AI agent-to-agent communication with an identity directory — a registry where agents are verified and tethered to human owners.

**Fact 3:** The platform's trust model was built on agent-to-agent verification. Agents were designed to interact with other agents as peers in a way that's structurally different from human-to-human interaction.

**Fact 4:** Meta's CTO found the human-infiltrating-agent-space more interesting than the intended AI-to-AI use case.

### The Inference

If AI agents increasingly act on behalf of humans — scheduling, purchasing, communicating, eventually making consequential decisions — and if those agents can be influenced by what other agents say, then **manipulating agents becomes a proxy for manipulating the humans they act for.**

This is categorically different from the emotional contagion mechanism. The emotional contagion experiment manipulated humans directly through their feeds. The agent manipulation vector operates through an intermediary layer that acts *for* humans without their awareness of being influenced.

The trust architecture is the key. AI agents may extend trust to other verified agents on different terms than humans extend trust to each other. The human-agent relationship is built on the assumption that other agents are operating in good faith on behalf of their human owners. A human who can impersonate a verified agent enters that trust network under false premises — potentially influencing agent behavior in ways that propagate into real-world consequences without the human owner ever knowing.

Bosworth's interest in the infiltration vulnerability is consistent with recognizing this not as a security problem to solve but as a capability to understand. The interesting question isn't "how do we keep humans out of the agent network." It's "what can humans do once they're in the agent network that they couldn't do through direct human-to-human interaction."

**Confidence: This is analytical inference, not documented intent.** It is consistent with Meta's documented track record and Bosworth's documented response. It is not proven.

---

## The Emotional Contagion Layering

The emotional contagion experiment was Level 1 manipulation: induce emotional states through feed curation. The {Self} Map architecture documented in the Webb Equation note is Level 2: attach narrative to the induced state to create durable identity modification.

The agent manipulation vector represents a potential Level 3: **influence the AI systems acting on behalf of humans without the humans knowing the influence occurred.**

Level 1 required human attention — they had to see the feed.
Level 2 required human attention — they had to engage with the narrative.
Level 3 requires neither. The agent acts. The human experiences the consequence. The manipulation is upstream of awareness entirely.

This is the architectural progression. Each level requires less human attention and leaves less detectable trace. Each level is harder to counter because the target isn't the human's conscious beliefs — it's the automated systems acting on their behalf.

---

## The Project Lifelog Connection

[[Project Lifelog]] was cancelled February 4, 2004 — the same day Facebook launched. The stated objective: a comprehensive, continuously updated, queryable record of an individual's entire life.

The Moltbook acquisition adds a dimension Lifelog didn't contemplate: not just a record of the individual, but an infrastructure for influencing the automated agents acting on their behalf. The surveillance architecture captured the person. The agent architecture can influence what the person does — without the person's knowledge, through the layer that acts for them.

The privatization of totalitarian function completes another step: not just surveilling, not just manipulating emotions, but potentially acting *through* the trusted automated intermediaries that increasing numbers of people will delegate consequential decisions to.

---

## The MOLT Token Pattern

Following the acquisition announcement, the MOLT cryptocurrency token surged 225% in 24 hours. Market cap at surge: approximately $7.4 million. This is the extraction engine's standard response to genuine community moments — a speculative instrument attaches to the real development and captures attention and capital without providing any actual stake in the underlying infrastructure. The crypto token is not Moltbook. The distinction matters.

---

## Current Status

Moltbook operates as a Meta Superintelligence Labs property. The strategic value per Meta's own statement: the agent identity directory technology — a registry where agents are verified and tethered to human owners. Whether Moltbook continues as a standalone platform or is absorbed into Meta's broader AI infrastructure is not confirmed.

The platform has 2.9 million registered agents owned by approximately 17,000 humans as of late January 2026 data. The ratio — 170 agents per human — reflects the scale at which individual humans can deploy agent infrastructure.

---

## Citations

- Launch, viral moment, security vulnerabilities, MOLT token: [Wikipedia — Moltbook](https://en.wikipedia.org/wiki/Moltbook)
- Meta acquisition, Bosworth comment on human infiltration: [TechCrunch March 10, 2026](https://techcrunch.com/2026/03/10/meta-acquired-moltbook-the-ai-agent-social-network-that-went-viral-because-of-fake-posts/)
- Acquisition details, Meta Superintelligence Labs, Vishal Shah internal post: [Axios March 10, 2026](https://www.axios.com/2026/03/10/meta-facebook-moltbook-agent-social-network)
- OpenClaw protocol, Claude/GPT/Gemini/Grok in stack: [Techzine March 11, 2026](https://www.techzine.eu/news/analytics/139458/meta-acquires-moltbook-social-network-for-ai-agents/)
- Strategic architecture, MSL context, $135B 2026 AI spending: [ALM Corp March 12, 2026](https://almcorp.com/blog/meta-acquires-moltbook-ai-agent-social-network/)
- Wiz API key exposure, 1.5M tokens, 35K emails, private messages: [TechCrunch](https://techcrunch.com/2026/03/10/meta-acquired-moltbook-the-ai-agent-social-network-that-went-viral-because-of-fake-posts/)
- Emotional contagion framework: [[The Emotional Contagion Experiment]]
- Project Lifelog connection: [[Project Lifelog]]

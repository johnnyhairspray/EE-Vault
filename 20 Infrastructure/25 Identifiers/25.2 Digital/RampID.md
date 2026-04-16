---
Category: Entity
Sub-category: Infrastructure
Type: Identifier
Sub-type: Persistent Identity Key
Status: Active
Confidence: Verified
Developer: "[[LiveRamp]]"
Connected-to:
  - "[[LiveRamp]]"
  - "[[Auren Hoffman]]"
Links:
  - "[[LiveRamp]]"
  - "[[Auren Hoffman]]"
  - "[[The Privatized Panopticon]]"
Tags:
  - infrastructure
  - identifier
  - digital
  - persistent-key
  - identity-resolution
  - ad-tech
  - cross-channel
Aliases:
  - RampID
  - LiveRamp RampID
  - AbiliTec
---
# RampID

Persistent cross-channel identity identifier developed by [[LiveRamp]]. The primary mechanism for linking offline consumer identity (name, email, address) to online behavioral data (browser cookies, mobile advertising IDs, connected TV identifiers).

## How It Works

RampID uses LiveRamp's AbiliTec identity graph to create a durable, privacy-preserving identifier that:

- **Links offline PII** (CRM records, purchase history, mailing lists) to digital identifiers
- **Bridges devices** — connecting a person's desktop browser, mobile phone, and connected TV as the same individual
- **Enables cross-organization matching** — different companies can match audiences on RampID without exchanging raw PII (the privacy-preserving claim: they share hashed identifiers, not names and emails)

The "100% activation match rate" for synced partner destinations means: if an individual has been previously identified through any connected channel, they can be re-identified even if they switch devices, change email addresses, or delete cookies.

## RampID vs. LexID

**LexID** (LexisNexis): Government-facing persistent key derived from public records — criminal, financial, address history. Used for vetting, background checks, law enforcement.

**RampID** (LiveRamp): Commercial-facing persistent key linking behavioral data across digital channels. Used for advertising targeting, audience matching, commercial analytics.

The vault's significance: these two identifier systems, operating in separate legal domains, connect at the enforcement layer. When ImmigrationOS or ELITE generates an enforcement target, the target's LexID (government records) can be correlated with their RampID (commercial behavioral profile) through data broker intermediaries — producing a complete dossier that spans both the government-facing and commercial-facing identity layers.

## The Clean Room Application

RampID is the identifier that enables LiveRamp's Clean Room product — allowing two organizations to perform analytics on combined datasets by matching on RampID without sharing raw PII. As noted in the [[LiveRamp]] vault note, this is the technical architecture that allows government agencies and commercial data brokers to effectively combine datasets without the government formally "accessing" the commercial data in a way that would require warrants.

## Citations

- RampID methodology, AbiliTec, cross-channel linking: [LiveRamp Docs](https://docs.liveramp.com/identity/en/rampid-methodology.html)
- Identity resolution overview: [Improvado January 2026](https://improvado.io/blog/what-does-liveramp-do)

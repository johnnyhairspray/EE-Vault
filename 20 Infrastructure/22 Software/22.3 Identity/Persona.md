---
Category: Infrastructure
Sub-category: Software
Type: Identity Verification
Sub-type:
Status: Active
Confidence: Verified
Founded: 2018
Headquarters: "San Francisco, CA"
Valuation: "$2 billion"
Funded-by:
  - "[[Founders Fund]]"
  - "[[Peter Thiel]]"
Links:
  - "[[Peter Thiel]]"
  - "[[Founders Fund]]"
  - "[[Palantir Technologies]]"
  - "[[ICE]]"
  - "[[LiveRamp]]"
  - "[[DOGE]]"
  - "[[Schedule F]]"
  - "[[ImmigrationOS]]"
  - "[[Sparta]]"
tags:
  - Persona
  - identity-verification
  - KYC
  - surveillance
  - FedRAMP
  - Thiel
  - biometric
  - 269-checks
  - federal-pipeline
  - SAR
  - age-verification
  - Roblox
  - Discord
  - OpenAI
Aliases:
  - "Persona Identity"
  - "Persona.com"
---
# Persona

Identity verification company founded 2018. Headquarters San Francisco. Valuation approximately $2 billion. Funded by [[Peter Thiel]]'s [[Founders Fund]]. Clients include OpenAI, Discord, Roblox, Reddit, LinkedIn, Coursera, Square, and Lime. Pursuing FedRAMP authorization for *"workforce security."*

Persona presents as a Know Your Customer (KYC) compliance and age verification tool. What researchers discovered when its frontend code was left publicly accessible on a FedRAMP-authorized government server is something significantly more expansive.

## The 269 Checks

Researchers accessed 2,456 source files from Persona's publicly exposed codebase on a FedRAMP-authorized government server — revealing the full operational scope of what occurs during a standard Persona "verification."

Beyond confirming identity, every Persona verification runs up to **269 distinct checks** including:

- **Facial recognition** against watchlists and Politically Exposed Persons (PEP) databases
- **Adverse media screening** across 14 categories: terrorism, espionage, cannabis trafficking, fentanyl trafficking, romance fraud, money laundering, wildlife trade, and more
- **Cryptocurrency activity checks** via Chainalysis and TRM Labs
- **Cross-referencing** against government databases, consumer credit agencies, utilities, and postal databases
- **Risk and similarity scores** assigned to each verified individual
- **Suspicious Activity Reports (SARs) filed directly** with U.S. and Canadian federal agencies

Data collected includes: facial biometrics, government ID numbers, IP addresses, browser fingerprints, device fingerprints, phone numbers, selfie backgrounds, and financial data. Retention: **up to 3 years.**

Persona shares verified identity data with **17 subprocessors.**

**The critical architectural fact:** The government platform and the consumer platform **share the same codebase.** The "age verification" a child completes to access Roblox runs on the same infrastructure as the federal workforce verification system.

## The Consent Fiction

Every Persona verification is technically consented to — users tap "Agree" to a terms of service document they did not read, under conditions where refusing means the service is inaccessible. The 269 checks are not disclosed at the point of consent. The SAR filing authority is not prominently disclosed.

Persona's position: not all 269 checks run on every user — specific checks are determined by client configuration. What this means operationally: the platform is **built** to run 269 checks and report to federal agencies. Whether Discord activates every check is a configuration setting, not a different product. The infrastructure exists and connects to government databases regardless of which client turns which feature on.

## The FedRAMP Pipeline

Persona is pursuing FedRAMP authorization with a stated goal of *"workforce security"* — verifying the identities of federal employees.

The threat model this creates:

1. Federal employee verifies identity through Persona for agency access
2. Persona flags them as a federal employee in verification metadata
3. 269 checks run including adverse media screening and government database cross-referencing
4. That identity flag propagates to Persona's 17 subprocessors
5. [[LiveRamp]] links verified federal identity → RampID → behavioral profile across all platforms
6. The resulting dossier: federal employee's social media consumption, news sources, financial stress indicators, political engagement, associations — all linked to their verified federal identity

The policy context: [[Schedule F]] and [[DOGE]]'s civil service purges require identifying which federal employees are ideologically aligned with the administration. The Persona/FedRAMP infrastructure provides the mechanism to flag, profile, and track federal employees across their digital lives — using tools they were required to use to do their jobs.

## The Children Pipeline

January 2026: Roblox — with 151 million daily users, 40% of whom are under 13 — began mandatory global facial scans through Persona for age verification.

March 2026: Discord began expanding Persona-based age verification globally.

Reddit, LinkedIn, OpenAI, and Coursera already use Persona across their platforms.

The data pipeline: child completes "age verification" → Persona runs facial recognition, assigns risk score, screens adverse media categories, cross-references government databases, potentially files SAR → retains biometric and behavioral data for 3 years → shares with 17 subprocessors.

Children born after approximately 2012 will never have had internet access without their biometric data entering this pipeline. They are enrolled at first use.

## The Thiel Network Connection

[[Peter Thiel]]'s [[Founders Fund]] backs Persona. Thiel co-founded [[Palantir Technologies]], which holds the $30M ICE contract for ImmigrationOS. Thiel funds [[JD Vance]], who as VP oversees the administration that is implementing [[Schedule F]] and the civil service purges for which Persona's FedRAMP workforce verification is the intake infrastructure.

The financial loop: Thiel funds the politicians → who implement the policies → that create federal contracts → that flow to Thiel's portfolio companies → whose valuations appreciate → generating returns that fund more politicians.

Persona is not a standalone product. It is a node in a network.

## The Integration Layer

Persona sits at the junction between the commercial surveillance apparatus and the state surveillance apparatus:

**Commercial side**: Persona verifies "you are who you say you are" → [[LiveRamp]] links that verified identity to RampID → RampID connects to behavioral data from every platform the user has touched → the dossier is assembled without any single actor holding all of it

**State side**: Persona files SARs directly with federal agencies → the FedRAMP government platform shares the same codebase as consumer implementations → verified identity flags propagate to 17 subprocessors with access to the full verification record

This is the **clean room made human**. Rather than combining datasets in a privacy-preserving technical environment, Persona is the point where a human being's verified identity is connected to every behavioral, financial, political, and biometric signal attached to them — and that connection is made reportable to the federal government through a mechanism the user consented to by tapping "Allow" to verify their age on Discord.

## Citations

- Founders Fund backing, $2B valuation, client list: vault previous research
- 2,456 source files exposed on FedRAMP server, 269 checks, 14 adverse media categories, SAR authority, 17 subprocessors, 3-year retention: vault previous research / Ken Klippenstein reporting
- Government platform and consumer platform share same codebase: vault previous research
- FedRAMP "workforce security" goal: vault previous research
- Roblox mandatory facial scans January 2026, 151M daily users, 40% under 13: vault previous research
- Discord global rollout March 2026: vault previous research
- Chainalysis/TRM Labs cryptocurrency checks: vault previous research
- Thiel → Founders Fund → Persona → FedRAMP → Schedule F pipeline: [[Peter Thiel]] vault note | [[Schedule F]] vault note
- LiveRamp RampID integration as pipeline completion: [[LiveRamp]] vault note (pending upgrade)
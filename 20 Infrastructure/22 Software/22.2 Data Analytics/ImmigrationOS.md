---
Category: Entity
Sub-category: Infrastructure
Type: Software
Sub-type: Immigration Enforcement AI
Status: Active
Confidence: Verified
Developer: "[[Palantir Technologies]]"
Connected-to:
  - "[[Palantir Technologies]]"
  - "[[ICE]]"
  - "[[Stephen Miller]]"
  - "[[AWS]]"
Links:
  - "[[Palantir Technologies]]"
  - "[[ICE]]"
  - "[[Stephen Miller]]"
  - "[[The Privatized Panopticon]]"
Tags:
  - infrastructure
  - software
  - immigration-enforcement
  - AI
  - data-fusion
  - Palantir
  - ICE
  - surveillance
  - deportation
Aliases:
  - ImmigrationOS
  - ICM
  - Investigative Case Management
---
# ImmigrationOS

Palantir Technologies' AI-powered immigration enforcement platform deployed for ICE under a $145 million sole-source contract. Automates targeting, location, and "lifecycle management" for immigration enforcement from identification through removal.

## Data Sources

ImmigrationOS fuses data from:
- IRS tax records
- Social Security Administration filings
- Passport and visa databases
- Phone extraction data
- HHS records including Medicaid enrollment
- Commercial ad-tech location data (including Venntel)
- License plate reader data (Flock Safety / FlockOS)

These are combined into unified investigative profiles, with the system performing automated "super queries" to detect mismatches or inconsistencies that trigger enforcement flags.

## ELITE (Enhanced Leads Identification and Targeting)

ELITE is the targeting component — populating a map interface with enforcement targets. For each target, it generates an "Address Confidence Score" by cross-referencing location data from multiple sources to identify the most likely current address.

The ELITE module was the subject of a March 2026 ACLU investigation documenting that its data sources include commercial ad-tech brokers and public benefits records — meaning Medicaid enrollment and commercial app location data feed the same system that generates deportation targets.

## Mobile Fortify

Field agent mobile application that provides facial recognition against a database of 200+ million images from DHS, FBI, and State Department — enabling real-time biometric verification during field operations.

## The Conflict of Interest

[[Stephen Miller]] — the primary architect of ICE's enforcement policy and quota system — holds $100,000–$250,000 in Palantir stock. Palantir holds a $30M+ contract with ICE for ImmigrationOS. Palantir's government revenue increased 45% in Q1 2025 versus Q1 2024, substantially driven by immigration enforcement contracts. Miller designs the policy; Palantir builds the tool to execute it; Miller profits from Palantir's stock appreciation.

## Hosting

ImmigrationOS runs on [[AWS]] GovCloud infrastructure — Amazon's government-accredited cloud environment — providing the uptime required for continuous enforcement monitoring.

## Citations

- $145M sole-source contract, data fusion, lifecycle management: [ACLU March 2024](https://www.aclu.org/news/privacy-technology/palantir-deportation-roundup)
- DHS AI use case inventory: [DHS AI Inventory February 2026](https://www.dhs.gov/ai/use-case-inventory/ice)
- ELITE address confidence scoring, HHS/Medicaid data: [American Immigration Council February 2026](https://www.americanimmigrationcouncil.org/blog/mission-creep-ai-surveillance-tracking-americans)
- Mobile Fortify facial recognition 200M+ images: [MacDonald Hoague & Bayless March 2026](https://www.mhb.com/news/ices-new-ai-system-to-monitor-immigrants-records-and-movements-what-you-need-to-do-now)
- Miller stock conflict: [[Stephen Miller]] vault note

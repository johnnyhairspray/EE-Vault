---
Category: Analysis
Sub-category: Map of Content
Type:
Sub-type:
Status: Established Pattern
Confidence: Verified
Date-range: "2018 - 2026"
Nodes:
  - "[[ICE]]"
  - "[[DHS]]"
  - "[[Venntel]]"
  - "[[Babel Street]]"
  - "[[PenLink]]"
  - "[[LiveRamp]]"
  - "[[Acxiom]]"
  - "[[Palantir Technologies]]"
  - "[[ImmigrationOS]]"
  - "[[Persona]]"
  - "[[Flock Cameras]]"
  - "[[Sparta]]"
  - "[[Stephen Miller]]"
  - "[[Oracle Corporation]]"
  - "[[Fusion Centers]]"
  - "[[DOGE]]"
  - "[[The Digital Shadow]]"
  - "[[Kash Patel]]"
tags:
  - Fourth-Amendment
  - data-broker
  - privatized-surveillance
  - warrant-bypass
  - location-data
  - Venntel
  - Babel-Street
  - PenLink
  - ICE
  - DHS
  - Carpenter
  - third-party-doctrine
  - commercial-surveillance
  - Palantir
  - fusion-centers
  - MOC
Aliases:
  - "The Fourth Amendment Bypass"
  - "Privatized Panopticon MOC"
  - "Government Data Broker Partnership"
---
# The Privatized Panopticon: How the U.S. Government Outsourced Surveillance

**Status: Established pattern. The purchases, contracts, Inspector General findings, and court documents are public record. The legal framework being exploited is documented by the Supreme Court itself. This is not a hypothesis — it is architecture.**

## The Constitutional Constraint

The **Fourth Amendment** prohibits unreasonable government search and seizure. Since 1967 (*Katz v. United States*), the standard has been whether an individual has a **"reasonable expectation of privacy"** in the information the government wants to access. If yes, the government needs a warrant — individualized, specific, judicially authorized.

The **third-party doctrine** is the loophole that predates the digital era: information voluntarily shared with a third party loses Fourth Amendment protection. You gave your bank your deposit records. The government can get them without a warrant.

**2018: *Carpenter v. United States*** — The Supreme Court ruled that the government needs a warrant to access cell phone location history from cellular service providers because such records reveal *"near perfect surveillance"* of *"the privacies of life."* The Court recognized that the third-party doctrine cannot extend to data that is involuntarily and continuously generated simply by carrying a phone. The ruling was supposed to close the digital surveillance loophole.

It did not close the loophole. It simply moved it one layer over.

## The Architecture of the Bypass

If the government cannot compel a phone carrier to provide location data without a warrant, it can **purchase** the same data from a broker who bought it from an app developer who collected it from the user's phone. The data is identical. The constitutional protection evaporates because it was purchased, not demanded.

This is not an edge case or an abuse of the system. It is the system. The **Electronic Frontier Foundation**, the **ACLU**, the **Brennan Center for Justice**, and the **Center for Democracy and Technology** have all independently concluded: when government agencies purchase commercial data about Americans, *"they are evading Fourth Amendment safeguards as recognized by the Supreme Court."*

Congress proposed a fix: the **Fourth Amendment Is Not For Sale Act** — which would require a court order before government agencies can obtain commercial data on Americans. It passed the House in 2024 with bipartisan support. The Senate did not take it up. As of 2026, no such restriction is law.

## The Data Flow
User downloads app → app embeds SDK →
SDK collects location, behavior, device identifiers →
SDK transmits data to data broker (Venntel, Gravy Analytics, X-Mode) →
Data broker aggregates, packages, sells →
Government agency purchases without warrant →
Government agency conducts surveillance
No warrant. No probable cause. No judicial oversight. A commercial transaction.

**Venntel** (subsidiary of Gravy Analytics) is the documented hub of this pipeline for DHS-related agencies. EFF documented Venntel's government clients: at minimum **IRS, DHS, ICE, CBP, DEA, and FBI**. Venntel collects **more than 15 billion location points from over 250 million cell phones and other mobile devices every day** — its own marketing materials sent to DHS, obtained through FOIA litigation.

**Babel Street** re-hosts Venntel data through its Locate X product. A DHS official described Babel Street as "basically re-hosting Venntel's data at a greater cost." Babel Street's terms of use for Locate X **ban clients from using the data as evidence or even mentioning it in legal proceedings** — a deliberate structure to keep the surveillance invisible to courts. Babel Street clients include: Air National Guard, U.S. Special Forces Command (SOCOM), CBP, ICE, Secret Service.

## The Documented Contracts

**Customs and Border Protection**:
- Venntel contracts 2019 and 2020: **$2 million+**
- Babel Street renewal 2020: **nearly $3 million**
- Uses: tracked phones to *"locations of law enforcement interest,"* monitored *"travel patterns,"* identified *"repeat visitors, frequented locations, pinpoint known associates"*

**Secret Service**:
- Babel Street 12-month contract 2019: **$600,000+**
- Use case: *"identify mobile devices carried near popular border crossing points into the U.S. and pull up the historical location data for those devices, viewing where they've been in the preceding months"*

**FBI**:
- Babel Street contract 2022: **$27 million** for 5,000 licenses

**ICE and PenLink (2025)**:
- January 2024: ICE pledged to stop purchasing *"commercial telemetry data"*
- 2025: ICE awarded a **no-bid contract** to PenLink for its Webloc/Tangles suite — updated daily with *"billions of pieces of location data from hundreds of millions of mobile phones"*
- PenLink had previously absorbed Israeli OSINT vendor Cobwebs, bundling open-source intelligence with location data
- ICE spending on PenLink-family capabilities: **$5 million+** since 2024
- Capability: *"forensic and predictive analytics"* — correlating movement with social media, capable of mapping visits to abortion clinics, churches, political meetings
- The contract reversed ICE's own stated policy. The Inspector General had found the practice illegal. ICE resumed it anyway

## The Inspector General Finding

**September 28, 2023**: DHS Inspector General published findings that CBP, ICE, and the Secret Service *"did not adhere to privacy policies"* before buying and using location data. Specific violations documented:
- **No required Privacy Impact Assessments** conducted before contracts
- **No Privacy Threshold Assessments** approved despite requirement
- DHS acting privacy officer issued a June 2019 order to *"stop all projects involving Venntel data"* — both CBP and ICE **signed new contracts with Venntel after that order**
- DHS internal email documented a DHS official **tracking co-workers** using the location data

CBP's retroactive privacy review (August 2024) claimed the purchased data was collected with user consent. The **FTC finalized an order against Venntel on January 14, 2025** — finding it had violated the FTC Act by selling location data without verifiable user consent. The CBP claim was false by the FTC's own determination.

As of March 2026, members of Congress wrote to the DHS Inspector General requesting a **second investigation** — noting ICE had resumed purchases despite the first investigation finding the practice illegal, and despite DHS having still not adopted required policies.

## The Third-Party Doctrine in Practice

The legal theory DHS used to justify these purchases: the data was *"anonymized"* and therefore not personally identifiable information, and therefore not protected by *Carpenter*. Two problems with this:

1. The FTC has explicitly stated that *"so-called anonymized data remains sensitive"* — because advertising IDs and device fingerprints can be relinked to individuals through standard commercial data matching
2. *Carpenter* was decided precisely because the Supreme Court recognized that continuous, comprehensive location data reveals the *"privacies of life"* regardless of technical anonymization claims

DHS internal emails acknowledged the problem: *"legal, policy, and privacy reviews have not always kept pace with the new and evolving technologies."* The surveillance continued anyway.

## The Integration Layer: Where Commercial Becomes Operational

The location data purchase is layer one. Layer two is how it connects to the enforcement infrastructure.

**[[Palantir Technologies]]** — [[ImmigrationOS]] provides *"near real-time visibility"* into immigrant movements, from *"identification to removal."* It ingests data from multiple sources including commercially purchased location information and merges it with federal law enforcement databases, court records, and biometric data. The purchased location data tells agents where someone is. ImmigrationOS tells them what to do about it.

**[[Fusion Centers]]** — The government's version of a data clean room. Approximately 80 federally supported fusion centers across the U.S. where commercial data purchases, law enforcement databases, federal records, and surveillance feeds are merged and analyzed. No warrant required because no single agency is conducting a search — the data is pooled and analyzed at the fusion center level, distributed to requesting agencies.

**[[Sparta]]** — ICE's secret watch list. Commercial location data tells you where someone is. Sparta tells you whether they're a target. The two systems are operational complements.

**[[Flock Cameras]]** — License plate readers generating location data independently of the commercial app ecosystem. Government purchases Flock data through law enforcement agreements rather than commercial data broker contracts — same result, different procurement pathway.

**[[DOGE]]** — Access to SSA, IRS, Treasury, and other federal financial and identity databases. The commercial surveillance layer provides behavioral and location data. DOGE's federal database access provides financial, employment, tax, and identity data. [[Palantir Technologies|Palantir]] and [[Oracle Corporation|Oracle]] provide the integration platforms. The combination is comprehensive population surveillance from multiple independent collection streams.

**[[Persona]]** — Identity verification that links the anonymous advertising ID (the commercial surveillance identifier) to verified biometric identity (the government surveillance identifier). Once Persona has linked the two, the commercial behavioral profile attaches permanently to the verified individual. [[LiveRamp]]'s RampID performs the same function in the commercial layer.

## The Consent Fiction

Every link in this chain is technically grounded in user consent. The app asked for location permission. The user tapped Allow. The terms of service — which no one reads — disclosed that data might be shared with *"partners."* The data broker's privacy policy — which no one reads — disclosed that data might be used for *"analytics and marketing."*

The FTC has made clear this consent is not meaningful: Venntel and Gravy Analytics were found to have sold data *"without obtaining verifiable user consent."* Mobilewalla was fined for selling data *"without taking reasonable steps to verify consumers' consent."* The consent framework that underlies the entire legal theory of the data broker marketplace is, by the FTC's own determination, largely fictitious.

The government knew this and purchased the data anyway. The legal argument was: the government bought it commercially, therefore the Fourth Amendment doesn't apply. The commercial transaction was invalid from a consent standpoint. But the surveillance happened.

## The Political Deployment

The pattern the vault documents in the immigration enforcement context illustrates how this architecture gets operationally deployed against a targeted population:

1. Commercial apps collect location data from immigrant communities
2. Venntel/Babel Street/PenLink aggregate and sell to ICE without warrant
3. ImmigrationOS integrates location with federal identity and enforcement records
4. [[Sparta]] identifies watch-list targets
5. [[Flock Cameras]] provide real-time license plate tracking
6. [[Stephen Miller]]'s 3,000/day arrest quota creates operational pressure to use all available data
7. Dragnet operations at churches, schools, courthouses where pattern-of-life analysis identified congregations

The system was designed for criminal investigation. It was deployed as an immigration dragnet. An ICE official in 2021 wrote that Venntel licenses *"should be used only in criminal investigations and are not intended for use as an immigration enforcement tool."* By 2025, the same data infrastructure was the primary operational layer of mass immigration enforcement.

## The Legislative Gap

**Fourth Amendment Is Not For Sale Act**: Passed the House 2024 with bipartisan support. Stalled in Senate. Not law.

**American Data Privacy and Protection Act**: Proposed federal privacy legislation. Not passed.

**State-level**: Montana enacted location data restrictions. California and Vermont require data broker registration. No state has comprehensively closed the government purchase loophole.

The result: the Fourth Amendment protection recognized by the Supreme Court in *Carpenter* is operationally hollow. The government cannot compel your carrier to give it your location history without a warrant. It can purchase equivalent or superior data from a broker without a warrant. The constitutional right exists on paper. The surveillance happens anyway.

## March 2026: Public Confirmation

**March 18, 2026** — [[Kash Patel]], FBI Director, testified under oath before the Senate Intelligence Committee's annual Worldwide Threats hearing. When pressed by Sen. Ron Wyden whether the FBI was purchasing Americans' location data, Patel confirmed it — reversing the stated position of predecessor Christopher Wray, who told the same committee in 2023 the practice had stopped.

Patel: *"The FBI uses all tools to do our mission. We do purchase commercially available information that's consistent with the Constitution and the laws under the Electronic Communications Privacy Act, and it has led to some valuable intelligence for us to be utilized with our private and partner sectors."*

DIA Director James Adams III confirmed at the same hearing that the Defense Intelligence Agency also purchases commercially available location data.

Wyden's response named the AI angle explicitly: *"It's particularly dangerous given the use of artificial intelligence to comb through massive amounts of private information."* — signaling the pipeline's next layer: bulk purchase + AI analysis = warrantless mass surveillance at scale.

The admission is significant not because it revealed new architecture — the vault documented this infrastructure years prior — but because it is the first **on-the-record, under-oath confirmation** from an FBI Director that the practice has resumed and will continue. The surveillance state no longer needs to hide what it's doing. It just calls it "commercially available information."

## What This Documents

The U.S. government did not build a surveillance state through a secret program. It **contracted** one — through commercial data broker relationships that are publicly documented, through contracts available in federal procurement records, through Inspector General investigations that found the practice illegal, through FTC actions that confirmed the underlying data collection was non-consensual.

The surveillance is not the consequence of a failure of law. It is the consequence of **law failing to adapt** to a commercial infrastructure that outpaced it. And the people who built that commercial infrastructure — the app SDKs, the data brokers, the identity resolution platforms, the analytics layers — built it to sell advertising. The government simply became a customer.

**Eyes up.**

## Citations

- *Katz v. United States* (1967), third-party doctrine: standard Fourth Amendment jurisprudence
- *Carpenter v. United States* (2018), warrant requirement for cell location history, *"privacies of life"*: [ACLU FOIA lawsuit](https://www.aclu.org/cases/aclu-v-department-homeland-security-commercial-location-data-foia)
- Venntel 15 billion daily location points, 250 million devices, government marketing materials: [ACLU](https://www.aclu.org/news/privacy-technology/new-records-detail-dhs-purchase-and-use-of-vast-quantities-of-cell-phone-location-data)
- Venntel government clients — IRS, DHS, ICE, CBP, DEA, FBI: [EFF](https://www.eff.org/deeplinks/2022/06/how-federal-government-buys-our-cell-phone-location-data)
- Babel Street "re-hosts Venntel data," Locate X terms ban evidence use, clients include SOCOM/Air National Guard/CBP/ICE/Secret Service: [EFF](https://www.eff.org/deeplinks/2022/06/how-federal-government-buys-our-cell-phone-location-data)
- CBP Venntel contracts $2M+, Babel Street $3M, Secret Service Babel Street $600K: [ACLU](https://www.aclu.org/news/privacy-technology/dhs-is-circumventing-constitution-by-buying-data-it-would-normally-need-a-warrant-to-access)
- FBI Babel Street $27M 5,000 licenses 2022: [The Record](https://therecord.media/ftc-location-data-brokers-gravy-venntel-mobilewalla)
- ICE January 2024 pledge to stop, 2025 no-bid PenLink contract, $5M spending, Cobwebs acquisition, forensic/predictive analytics: [The Daily Beast](https://www.thedailybeast.com/ice-buys-sinister-tool-built-to-map-your-everyday-movements/)
- DHS Inspector General September 2023 finding — CBP/ICE/Secret Service violated federal law, no PIAs, privacy officer order violated, co-workers tracked: [DHS IG report, cited in](https://www.aclu.org/news/privacy-technology/dhs-is-circumventing-constitution-by-buying-data-it-would-normally-need-a-warrant-to-access)
- FTC Venntel order January 14, 2025, sold without verifiable consent: [Senator Wyden letter to DHS OIG March 2026](https://www.wyden.senate.gov/imo/media/doc/wyden_letter_to_dhs_oig_on_ice_purchasing_location_datapdf.pdf)
- CBP retroactive privacy review false claim about consent, contradicted by FTC: [Wyden letter](https://www.wyden.senate.gov/imo/media/doc/wyden_letter_to_dhs_oig_on_ice_purchasing_location_datapdf.pdf)
- March 2026 congressional letter to DHS OIG requesting second investigation: [Wyden letter](https://www.wyden.senate.gov/imo/media/doc/wyden_letter_to_dhs_oig_on_ice_purchasing_location_datapdf.pdf)
- EFF/ACLU/Brennan Center/CDT conclusions on Fourth Amendment evasion: [EFF](https://www.eff.org/deeplinks/2022/06/how-federal-government-buys-our-cell-phone-location-data) | [ACLU](https://www.aclu.org/news/privacy-technology/dhs-is-circumventing-constitution-by-buying-data-it-would-normally-need-a-warrant-to-access) | [EPIC](https://epic.org/documents/closing-the-data-broker-loophole-government-evasion-of-the-fourth-amendment/)
- "Anonymized data remains sensitive" — FTC position: [Wyden letter](https://www.wyden.senate.gov/imo/media/doc/wyden_letter_to_dhs_oig_on_ice_purchasing_location_datapdf.pdf)
- FTC Mobilewalla action: [The Record](https://therecord.media/ftc-location-data-brokers-gravy-venntel-mobilewalla)
- Fourth Amendment Is Not For Sale Act passed House 2024: [ACLU](https://www.aclu.org/news/privacy-technology/dhs-is-circumventing-constitution-by-buying-data-it-would-normally-need-a-warrant-to-access)
- ICE official 2021 email Venntel "not intended for immigration enforcement": [Rolling Stone](https://www.rollingstone.com/politics/politics-news/ice-dhs-privacy-location-data-aclu-1384797/)
- CBP domestic flight records purchase from airline-owned broker: [EPIC](https://epic.org/documents/closing-the-data-broker-loophole-government-evasion-of-the-fourth-amendment/)
- Kash Patel Senate testimony March 18, 2026: [TechCrunch](https://techcrunch.com/2026/03/18/fbi-is-buying-location-data-to-track-us-citizens-kash-patel-wyden/) | [The Guardian](https://www.theguardian.com/us-news/2026/mar/18/kash-patel-fbi-location-data) | [The Register](https://www.theregister.com/2026/03/19/fbi_patel_location_data/) | [Gizmodo](https://gizmodo.com/kash-patel-admits-the-fbi-is-buying-private-data-on-americans-2000735317)

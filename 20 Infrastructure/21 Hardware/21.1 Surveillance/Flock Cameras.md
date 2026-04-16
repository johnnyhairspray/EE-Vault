---
Category: Entity
Sub-category: Infrastructure
Type: Hardware
Sub-type: Surveillance / ALPR
Status: Active
Confidence: Verified
Manufacturer: Flock Group Inc. (dba Flock Safety)
Connected-to:
  - "[[Palantir Technologies]]"
  - "[[ICE]]"
  - "[[The Privatized Panopticon]]"
Links:
  - "[[Palantir Technologies]]"
  - "[[ICE]]"
  - "[[The Privatized Panopticon]]"
Tags:
  - infrastructure
  - hardware
  - surveillance
  - ALPR
  - license-plate-reader
  - acoustic-surveillance
  - Fourth-Amendment
  - Flock-Safety
Aliases:
  - Flock Safety cameras
  - FlockOS
  - ALPR
---
# Flock Safety Cameras

Automated License Plate Recognition (ALPR) camera network operated by Flock Group Inc. (Flock Safety). As of 2026, the largest fixed ALPR network in the United States — processing billions of monthly plate reads across law enforcement agencies nationwide.

## Core Technology

**Vehicle Fingerprint® technology:** Flock cameras capture not just license plates but full vehicle profiles — make, model, color, roof racks, bumper stickers, visible damage. This creates a searchable "vehicle identity" that persists even when plates are obscured or changed.

**FreeForm™ Search:** Investigators can search the national Flock network for partial vehicle descriptions — "red pickup with a cracked windshield" — across all contributing agencies simultaneously, without a specific plate number.

**Raven acoustic sensors (upgraded 2026):** Beyond gunshot detection (90% documented accuracy), Raven now uses machine learning to identify "human distress" sounds including screaming and tire screeches. When triggered, the system automatically cross-references nearby ALPR timestamps to generate a suspect vehicle list from everyone in the vicinity at the time of the sound event.

**Condor PTZ cameras:** Solar-powered pan-tilt-zoom cameras for live-streaming and 30-day evidence storage.

**Drone as First Responder (DFR) integration (2026):** When a Flock camera or Raven sensor triggers an alert, the system can automatically dispatch a drone to follow the flagged vehicle from 400 feet, providing continuous visual tracking until ground units arrive.

## The Federal Data Sharing Problem

Flock markets primarily to local law enforcement agencies. The company has claimed it does not have direct federal contracts. February 2026 reporting (Mountain View, CA) revealed that Flock's "National Lookup" feature was sharing local ALPR data with hundreds of out-of-state agencies — including HSI (Homeland Security Investigations) and CBP — without explicit awareness or consent from the local agencies that had purchased the cameras.

This is the clean room pattern applied to physical surveillance infrastructure: local governments purchase cameras for local policing, federal agencies access the data through the shared network without direct contracts or warrants.

Data retention: most images deleted after 30 days, but any vehicle placed on a "Hotlist" generates a permanent investigative file that integrates with Palantir and LexisNexis Accurint systems.

## The Fourth Amendment Architecture

*Carpenter v. United States* (2018) established that cell carrier location data requires a warrant. License plate data collected by private companies on public roads occupies ambiguous legal territory — generally treated as publicly observable information not requiring a warrant, even when aggregated into a continuous location tracking record across a network of thousands of cameras.

Flock's network effectively creates citywide and now near-national continuous vehicle tracking without the legal protections that would apply to direct government surveillance.

## Citations

- Vehicle Fingerprint, FreeForm Search, DFR integration: [Flock Safety](https://www.flocksafety.com/products/license-plate-readers)
- Raven acoustic upgrade, human distress detection: [EFF October 2025](https://www.eff.org/deeplinks/2025/10/flocks-gunshot-detection-microphones-will-start-listening-human-voices)
- Federal data sharing without permission, Mountain View: [Malwarebytes February 2026](https://www.malwarebytes.com/blog/privacy/2026/02/flock-cameras-shared-license-plate-data-without-permission)
- Richmond Police Department federal abuse allegations: [The Richmonder March 2026](https://www.richmonder.org/rpd-has-spent-1-million-on-flock-license-plate-readers-with-those-contracts-up-for-renewal-anti-surveillance-activists-call-for-cancellation-while-mayor-council-demur/)

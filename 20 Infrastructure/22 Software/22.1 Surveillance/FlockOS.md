---
Category: Entity
Sub-category: Infrastructure
Type: Software
Sub-type: Surveillance Platform
Status: Active
Confidence: Verified
Developer: Flock Safety
Connected-to:
  - "[[Flock Cameras]]"
  - "[[Palantir Technologies]]"
  - "[[ICE]]"
Links:
  - "[[Flock Cameras]]"
  - "[[Palantir Technologies]]"
  - "[[The Privatized Panopticon]]"
Tags:
  - infrastructure
  - software
  - surveillance
  - ALPR
  - sensor-fusion
  - drone
  - federal-data-sharing
  - Fourth-Amendment
Aliases:
  - Flock OS
  - Flock Safety platform
---
# FlockOS

The software platform and operational dashboard for the Flock Safety surveillance ecosystem. Ingests real-time data from fixed ALPR cameras, Raven acoustic sensors, and drone feeds into a unified law enforcement interface.

## Core Functions

**Real-Time Crime Center (RTCC) integration:** FlockOS functions as a sensor fusion hub — combining live drone footage, license plate alerts, acoustic event triangulation, and Computer-Aided Dispatch data into a single operator dashboard. Integrates with Records Management Systems so flagged vehicles and identities automatically populate officer alerts.

**Drone as First Responder (DFR) automation:** When a Flock camera or Raven sensor triggers an alert, FlockOS can automatically dispatch linked drones (e.g., Skydio) to provide continuous aerial tracking of the flagged vehicle until ground units arrive. Video retained for up to 30 days unless marked for permanent storage.

**FreeForm vehicle search:** Operators can search the nationwide Flock network using partial vehicle descriptions across all contributing agencies simultaneously.

## The Federal Access Problem

Early 2026 investigation revealed FlockOS contained a setting enabling federal agencies — ATF, Air Force, GSA — to silently access local ALPR data without explicit local agency awareness or approval. This triggered a California class-action lawsuit.

Flock's response (January 2026): added a visible "Federal Sharing" toggle in admin settings allowing local agencies to disable federal access. The terms of service retain Flock's "perpetual, worldwide license" to use anonymized data for AI training — meaning even disabled federal sharing doesn't prevent the company from using the data commercially.

## The Legal Architecture

FlockOS sits at the intersection of the same Fourth Amendment gap exploited by commercial data brokers: locally purchased surveillance infrastructure, data aggregated into a national network, federal agencies accessing that network through the commercial platform rather than direct government operation — avoiding warrant requirements that would apply to direct government surveillance of the same data.

Berkeley Police Accountability Board (March 2026) issued recommendations specifically addressing the federal access discovery and recommending stronger access controls.

## Citations

- Drone integration, RTCC function: [Skydio/Flock integration](https://www.skydio.com/integrations-catalog/flock-safety) | [Flock Safety Blog](https://www.flocksafety.com/blog/law-enforcement-drones)
- Federal agency access discovery, California lawsuit, toggle response: [Berkeley PAB March 2026](https://berkeleyca.gov/sites/default/files/2026-03/March%2018%2C%202026%20PAB%20Recommendations_Surveillance%20Tech.pdf)

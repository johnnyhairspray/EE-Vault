---
type: Infrastructure
sub_type: Software
tags: [RTCC, surveillance, data-fusion, ALPR, DFR]
developer: "[[Flock Safety]]"
links:
  - "[[Flock Safety Cameras]]"
  - "[[National Vetting Center]]"
  - "[[Palantir Technologies]]"
  - "[[LexID]]"
status: "#evergreen"
---

# FlockOS

## 🔍 Summary
The central situational awareness platform and "Operating System" for the **[[Flock Safety]]** ecosystem. FlockOS ingests real-time data from fixed ALPR cameras, **[[Gait Analysis]]** sensors, audio-detection hardware (Raven), and live drone feeds (Skydio), merging them into a unified tactical dashboard for law enforcement and private security.

## 🧬 The "Operational" Piston

### 1. The Single Pane of Glass (RTCC)
* **Sensor Fusion:** In 2026, FlockOS acts as an RTCC hub, allowing operators to monitor live drone footage alongside license plate alerts and gunshot triangulation in one interface.
* **Interoperability:** It integrates with Computer-Aided Dispatch (CAD) and Record Management Systems (RMS), ensuring that any "extracted" identity or vehicle is automatically flagged for the responding officers.

### 2. The Drone as First Responder (DFR) Link
* **Automated Dispatch:** When a sensor (Camera or Raven) triggers an alert, FlockOS can automatically launch a linked drone (e.g., **Skydio**) to provide "Continuous Overwatch".
* **Evidence Reconstruction:** The software captures high-resolution video for crime scene reconstruction, which is then stored for up to 30 days unless marked for permanent extraction.

### 3. The "Federal Sharing" Toggle (2026 Friction)
* **The "Nationwide" Access Setting:** In early 2026, it was discovered that FlockOS had a "silent" setting that enabled federal agencies (ATF, Air Force, GSA) to access local data, leading to a class-action lawsuit in California.
* **The Kill-Switch:** As of January 2026, a "Single Toggle" was introduced in the Admin Settings to allow local agencies to disable Federal Sharing, though Flock retains a "perpetual, worldwide license" to use **Anonymized Data** for AI training.

---

## 🔗 The "Technate" Loop
* **The Identifier Link:** FlockOS is the primary environment where "Physical Identities" (vehicles/gait) are resolved into "Digital Identities" (**[[LexID]]** or **[[RampID]]**).
* **The Vetting Bridge:** When a vehicle on a **[[National Vetting Center]]** hotlist enters a protected zone, FlockOS triggers the automated extraction protocol.

---

## 📚 Citations
1. **Flock Safety - Skydio (2026):** [Integration of Drone Video into Flock OS RTCC](https://www.skydio.com/integrations-catalog/flock-safety)
2. **Berkeley Police Accountability Board (Mar 2026):** [Recommendations regarding Flock Surveillance and Federal Access](https://berkeleyca.gov/sites/default/files/2026-03/March%2018%2C%202026%20PAB%20Recommendations_Surveillance%20Tech.pdf)
3. **Flock Safety Blog (Feb 2026):** [Law Enforcement Drones and the Future of Policing](https://www.flocksafety.com/blog/law-enforcement-drones)

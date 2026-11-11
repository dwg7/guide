---
title: Monthly Snapshot
---

# Monthly Snapshot

A monthly snapshot translates the public record into a short chain of reasoning for readers who follow the work from a distance. Each entry follows the same chain that dwg7 uses in its issues, so that the snapshot and the record read the same way.

## 1. Entry template

Use one entry per thread. Replace each bracketed text with content from the public record.

### [Thread title and link]

- **Question.** [The question the thread asks, in one sentence.]
- **Experiment.** [What was run: device, software versions, data, load.]
- **Result with conditions.** [Measured values together with the conditions that produce them.]
- **Review and correction.** [Who repeated or reviewed the work, and what changed in the conclusion.]
- **Open items.** [What remains to be measured or decided, and where to contribute.]
- **Checked.** [Date on which you read the thread.]

### Month header

- **Period.** [YYYY-MM]
- **Threads covered.** [Number of entries and a link to the issue list filtered for the month.]
- **Reading order.** [Which entry to read first, and why.]

## 2. Worked example from the public record

### GeoServer / MapServer on a Raspberry Pi ([UNopenGIS/7#1003](https://github.com/UNopenGIS/7/issues/1003))

- **Question.** How do GeoServer and MapServer perform on a small, low-cost computer, and where does the hardware reach its limit?
- **Experiment.** GeoServer 2.28.4 and MapServer 8.4.0 on a Raspberry Pi 4B, with 5,000 random points and 4 workers sending 20 WMS GetMap requests each. A second test used GeoServer 3.0.1 with a public health-facilities dataset of 8,975 features, a mixed read–write workload, and a 30-hour soak.
- **Result with conditions.** MapServer under FastCGI reached 16.9–22.5 requests per second against 13.1–13.6 for GeoServer. MapServer under CGI reached 5.1–5.5 against 7.6–13.6, which the author explains with per-request process cost. In the second test, concurrent write edits and the soak completed with zero server-side errors, and the unfiltered full-dataset request was the one workload that saturated the device.
- **Review and correction.** A repeat on Ubuntu 24.04 and Debian 13 showed that the working configuration relied on MapServer's default config path. The first author confirmed this and corrected two earlier statements about environment inheritance and CGI hosting. The simulated 1 GB memory limit stayed above the memory in use, so the 1 GB question remains open.
- **Open items.** Measurements on a Raspberry Pi 3 with 1 GB memory, and a check of the MapServer configuration examples in the published hands-on guide.
- **Checked.** 2026-11-11.

## 3. Worked example: November 2026

The entry below comes from a comment posted in the weekly meetup thread [#1027](https://github.com/UNopenGIS/7/issues/1027) on 2026-11-11. Its author separates premises, facts, and interpretation, and the entry keeps that order.

### Connectivity around peacekeeping sites ([#1027](https://github.com/UNopenGIS/7/issues/1027))

- **Question.** Can an architecture built on stable fast internet serve every site of a United Nations peacekeeping mission?
- **Experiment.** A contributor surveyed public connectivity data around the sites of one mission, and asked two other contributors to review the findings.
- **Result with conditions.** The open data was uneven in coverage, and the author states the bias first. Around the sites, connections exist and speeds vary. In some areas a 100 MB PMTiles file takes about 30 minutes to download. In the host country, mobile subscriptions stood at 46.6 per 100 people in 2023, and that figure includes voice calls. Fixed broadband subscriptions stood at 0.00174 per 100 people in 2023.
- **Review and correction.** The author labels a quoted passage on resource-limited intelligence work as general background, and says that whether it applies to this mission is unknown to the author.
- **Interpretation.** A cloud-native design may cover some sites and leave others open. A portable device that serves tiles over local Wi-Fi fits places where fixed lines are absent, and it sits beside a design that downloads PMTiles into the browser's storage.
- **Open items.** A fuller data set, and a check at the sites themselves. The full report is linked from the thread.
- **Checked.** 2026-11-11.

### Also active in November 2026

- The 2026 training lectures for the surveying course ([#976](https://github.com/UNopenGIS/7/issues/976), [#1010](https://github.com/UNopenGIS/7/issues/1010)) run on 2026-11-25, 2026-11-26, and 2026-12-14.
- A semantic search over a large public catalogue is open for comment ([#1014](https://github.com/UNopenGIS/7/issues/1014)).
- A study of high-resolution drone imagery as PMTiles is open ([#1023](https://github.com/UNopenGIS/7/issues/1023)).

## 4. Writing rules for entries


- Link every entry to its thread.
- Keep conditions next to numbers.
- Report corrections as part of the result.
- Name a person only when the thread needs the name for credit, and prefer the role (for example "a contributor").
- Record the date of reading in every entry.

[Back to index](index.md)

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

### Filling gaps in official building data ([cvalda](https://github.com/dwg7/cvalda))

This entry comes from the decision log of an application repository, read on 2026-11-26. The viewer shows buildings from official vector tiles of a national mapping agency in Hokkaido, and adds buildings from an open global data set where the official data has none. All computation runs in the reader's browser, and the merged data set stays unpublished.

- **Question.** Where official building data is thin, can an open global data set fill the gaps, and can a page do so for the visible area only?
- **Experiment.** The owner and an assistant measured the tiles first: format, maximum zoom, layer names, and fields. At zoom 16, the repacked official tiles match the agency's own tiles in all 21 tiles tested, across 5 places. The open data set stops at zoom 14. At zooms 13 and 14, the official building layer holds about 15–20% of the area it holds at zoom 16. Buildings appear only from zoom 15 for this reason. Per building, the page computes the share of area that official polygons cover, and a slider sets the threshold; the default is 0.5.
- **Result with conditions.** In the tests at Niseko, the covered shares form two humps: many buildings are almost uncovered, many are covered above 0.8, and few lie between. The page offers three modes, and a reader can save the view as GeoJSON or FlatGeobuf. The released stages were published on 2026-11-21 and checked on the public page.
- **Review and correction.** On 2026-11-22 the owner's next stage found a defect in the released stages. Tiles carry buffers, so a building near a tile edge appears in two tiles, whole or as overlapping parts. After fusing, three blocks of 3×3 tiles hold 12.7%, 17.9%, and 14.6% fewer official buildings than the raw pieces. At Niseko station, zoom 17.2, official buildings fell from 391 to 325. Among open-data buildings, 40–60% of the copies near a coarse tile edge differ in shape. The log records the correction beside the earlier text.
- **Open items.** The exact credit wording for the agency's data, the licence notice for an export that mixes the two sources, the default threshold after a visual check, and a check on a low-memory laptop. The log lists each as a question for the owner.
- **Checked.** 2026-11-26, from the repository's `AGENTS.md`, `notes/decisions.md`, `notes/stage6.md`, and `notes/reachability.md`.

### Also active in November 2026

- The 2026 training lectures for the surveying course ran on 2026-11-25 ([#1010](https://github.com/UNopenGIS/7/issues/1010), closed on 2026-11-26 with the note "carried out"). The thread [#976](https://github.com/UNopenGIS/7/issues/976) stays open for 2026-11-26 and 2026-12-14, and lists the Raspberry Pi units assigned to the trainees' countries.
- A semantic search over a large public catalogue, and a companion that builds raster tiles from the same catalogue with user-defined functions, closed on 2026-11-26 at their author's decision ([#1014](https://github.com/UNopenGIS/7/issues/1014), [#1013](https://github.com/UNopenGIS/7/issues/1013)).
- A study of high-resolution drone imagery as PMTiles closed "for now" on 2026-11-26 ([#1023](https://github.com/UNopenGIS/7/issues/1023)). A candidate prompt for converting a national transformation-parameter file to a PROJ grid was posted in the open thread [#740](https://github.com/UNopenGIS/7/issues/740).
- A drone experiment on a purchased aircraft continues from [#1021](https://github.com/UNopenGIS/7/issues/1021) in [#1036](https://github.com/UNopenGIS/7/issues/1036).

## 4. Writing rules for entries


- Link every entry to its thread.
- Keep conditions next to numbers.
- Report corrections as part of the result.
- Name a person only when the thread needs the name for credit, and prefer the role (for example "a contributor").
- Record the date of reading in every entry.

[Back to index](index.md)

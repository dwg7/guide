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

## 3. Writing rules for entries

- Link every entry to its thread.
- Keep conditions next to numbers.
- Report corrections as part of the result.
- Name a person only when the thread needs the name for credit, and prefer the role (for example "a contributor").
- Record the date of reading in every entry.

[Back to index](index.md)

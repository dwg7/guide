---
title: dwg7 in 5 Minutes
---

# dwg7 in 5 Minutes

dwg7 is Domain Working Group 7 of the UN Open GIS Initiative. It works on "Smart Maps": web maps that stay open, so that anyone can build, test, and reuse them. Its method is a public record. Each piece of work leaves a thread that runs from a question to a result and a correction. This page describes that method as it appears in the [dwg7 issues](https://github.com/UNopenGIS/7/issues) on 2026-11-11. The issues are the source, and this page is a reading aid.

## The method

> question → experiment → result with conditions → review and correction → reuse

Read one thread, and the chain is visible. [#1003](https://github.com/UNopenGIS/7/issues/1003) compares two map servers on a Raspberry Pi.

1. **Question.** Where does a small, cheap computer reach its limit when it serves map data?
2. **Experiment.** A contributor ran both servers on a Raspberry Pi 4B. The load was 4 workers sending 20 map requests each, on 5,000 random points.
3. **Result with conditions.** One server in one mode served 16.9–22.5 requests per second. The other served 13.1–13.6. The thread gives versions and settings beside each number.
4. **Review and correction.** A second contributor repeated the test on other operating systems and found that the result depended on a default file path. The first contributor confirmed it and corrected two earlier statements in the same thread.
5. **Reuse.** A hands-on guide for an older, smaller Raspberry Pi followed. Its measurements are the open item.

## Ten habits behind the method

The record shows the same habits across ten themes and about a thousand threads. Each habit has one place where you can see it.

1. **Conditions beside numbers.** Hardware, versions, data, and load stand next to every figure ([#1003](https://github.com/UNopenGIS/7/issues/1003)).
2. **Hypothesis before test.** A thread says "my hypothesis is" and returns later with the verdict ([#567](https://github.com/UNopenGIS/7/issues/567)).
3. **Visible correction.** A fix appears next to the claim it repairs, often as struck-through text ([#642](https://github.com/UNopenGIS/7/issues/642)).
4. **Reasons in words.** A design choice comes with its reasons, in a short list or a decision record ([#642](https://github.com/UNopenGIS/7/issues/642), [#936](https://github.com/UNopenGIS/7/issues/936)).
5. **Invitation to repeat.** Code and steps are public, and readers repeat them and report back ([#642](https://github.com/UNopenGIS/7/issues/642)).
6. **Open items stay open.** A thread names what remains and the condition for resuming ([#567](https://github.com/UNopenGIS/7/issues/567)).
7. **Care for shared resources.** A copy is hosted so that nobody must hit the public source repeatedly ([#920](https://github.com/UNopenGIS/7/issues/920)).
8. **Decisions that settle.** A thread closes when the idea has become part of the work ([#936](https://github.com/UNopenGIS/7/issues/936)).
9. **Start from others' work.** A thread builds on a published article or on an issue in another project ([#361](https://github.com/UNopenGIS/7/issues/361), [#920](https://github.com/UNopenGIS/7/issues/920)).
10. **Quiet observation.** A thread watches a public source over time and compares two dates ([#857](https://github.com/UNopenGIS/7/issues/857)).

## Rhythm

- **Weekly meetup.** A 25-minute online session runs on Tuesdays at 12:30 JST. Each week is one issue. Presenters post their updates as comments beforehand, and the session moves through them in an agreed order. The record holds 277 meetup issues since 2022.
- **Labels.** `priority/MUST`, `priority/SHOULD`, and `priority/MAY` order attention. Closed threads carry them: the middle time to close is 14, 23, and 32 days. Other labels name a purpose: `information`, `adopt`, `in progress`, `request for comments`, `help wanted`, `event`, `meetup`.
- **Language.** Japanese appears in two of every three issues opened in 2025 and 2026. Machine translation reads technical threads well. A short English comment invites international readers.

## What the work looks like now

- Map tiles live in single PMTiles files. Public hosting, such as Source Cooperative, holds the original. Martin servers deliver tiles to readers ([#642](https://github.com/UNopenGIS/7/issues/642), [#999](https://github.com/UNopenGIS/7/issues/999)).
- Small computers carry maps into the field and the classroom ([#567](https://github.com/UNopenGIS/7/issues/567), [#575](https://github.com/UNopenGIS/7/issues/575)).
- Language models meet geospatial data in a design that separates a staff assistant from a map-making service ([#936](https://github.com/UNopenGIS/7/issues/936)). A neighbouring group, dwg5, works on Geo AI ([#995](https://github.com/UNopenGIS/7/issues/995)).
- Some themes are history. Between 2023 and 2024 the group tried distributing tiles through IPFS. Delivery has since moved to Martin servers, Source Cooperative, and GitHub Pages.

## Why this method fits

International and public-sector geospatial work needs claims that others can verify, choices that outlast staff changes, and data that stays open. A thread that keeps its conditions, corrections, and open items gives all three. Open repositories and issues carry all three as a matter of course.

## Your path in four steps

1. **Observe.** Read one thread from its question to its result.
2. **Choose.** Pick a friction from your own work that fits the chain.
3. **Try.** Run one experiment from [Good First Experiments](good-first-experiments.md). State your conditions.
4. **Share.** Post your record as a comment or an issue, and link the thread you started from.

[Onboarding Paths](onboarding-paths.md) matches these steps to your background.

[Back to index](index.md)

---
title: Onboarding Paths
---

# Onboarding Paths

Six paths lead into the same work: a question, an experiment, a record, a review. Each path names real threads in the [dwg7 issues](https://github.com/UNopenGIS/7/issues), checked on 2026-11-11, and one small action you can finish in a week.

The first steps come from the record. The small contribution and the one-week outcome on each path are this guide's suggestions. Open threads accept your comment today. Closed threads show how the work was done, and a new issue that links to them continues it.

## Geospatial Practitioner

### Who this path is for

People who map, validate, and publish spatial data.

### What you can bring

A trained eye for data quality, and knowledge of how maps get used in the field.

### Three first steps

1. Read [#857](https://github.com/UNopenGIS/7/issues/857), a thread that tracked a humanitarian mapping task from "mapped" toward "validated". Its author closed it on 2026-11-26 as finished, and it accepts comments.
2. Open the linked task and look at one small block in a corner of the area.
3. Compare what you see with the progress figures in the thread.

### A small first contribution

Comment on #857 with one observation about one block: what you checked, and what you found.

### What success may look like after one week

Your comment states its conditions, so a reader can repeat your check.

### Where to go next

[Good First Experiments](good-first-experiments.md), starting with the dataset checks. Projects to browse in the dwg7 organisation: [height-coverage](https://github.com/dwg7/height-coverage) (an awareness site on building-height entries in OpenStreetMap), [do-survey](https://github.com/dwg7/do-survey) (public survey information of one regional office, summed by municipality), and [snow-hokkaido](https://github.com/dwg7/snow-hokkaido) (a daily record of snow, cloud, and green cover on a zoom-18 grid).

## Software Engineer

### Who this path is for

People who build and measure software.

### What you can bring

Reproducible measurements and the habit of stating test conditions.

### Three first steps

1. Read [#1003](https://github.com/UNopenGIS/7/issues/1003), which compares two map servers on a Raspberry Pi.
2. Read the open item at the end of the thread: measurements on a Raspberry Pi 3 with 1 GB of memory. The thread closed "for now" on 2026-11-26 and accepts comments.
3. Read [#642](https://github.com/UNopenGIS/7/issues/642) to see a second experiment, a local tile cache, with its code.

### A small first contribution

Repeat one measurement from #1003 or #642 on your own machine. Post the hardware, the versions, the data, and the numbers.

### What success may look like after one week

Your result sits next to the original, and a reader can compare the two.

### Where to go next

The tile cache and range-request experiments in [Good First Experiments](good-first-experiments.md). For a whole application, read the decision log of the building viewer [cvalda](https://github.com/dwg7/cvalda/blob/main/notes/decisions.md): each decision lists its reason and what remains unknown, and a later stage corrects an earlier one in the open. Other projects to browse: [zukaku](https://github.com/dwg7/zukaku) (a print atlas generator with MapLibre and Martin) and [dorayaki](https://github.com/dwg7/dorayaki) (an experiment that carries surfels on map tiles).

## AI Builder

### Who this path is for

People who build with language models, search, and agents.

### What you can bring

Evaluation habits: a fixed task, a recorded input, a checked output.

### Three first steps

1. Read [#936](https://github.com/UNopenGIS/7/issues/936). It records a design decision as an ADR and then reports each step of the build.
2. Try the search in [#1014](https://github.com/UNopenGIS/7/issues/1014) with a question from your own work. It covers 1,921 collections of a public FAO catalogue and adds semantic search to the full-text search that the catalogue already offers. The thread was closed by its author on 2026-11-26.
3. Write down the question, the result, and your judgment of it.

### A small first contribution

Comment on #1014 with three queries, what came back, and whether it answered the question. The thread notes that the source code was in preparation on 2026-09-21.

### What success may look like after one week

Your comment separates what the system returned from what you verified.

### Where to go next

The [Field Guide](field-guide.md) entry on AI-assisted work. Projects to browse: [staccato-ecosystem](https://github.com/dwg7/staccato-ecosystem) (a cooperation method for education, disaster prevention, and surveying), [ferspas-html-demo](https://github.com/dwg7/ferspas-html-demo) (a move of a Jupyter workflow on FAO data into a transparent web app), and [kcai-un-docs](https://github.com/dwg7/kcai-un-docs) (geospatial traces from United Nations documents).

## International and Public-Sector Practitioner

### Who this path is for

People in governments, international organisations, and public programmes.

### What you can bring

The operational question, the real constraint, and the sense of what a decision needs.

### Three first steps

1. Read [#575](https://github.com/UNopenGIS/7/issues/575), which prepares one computer for each participant of an international training course.
2. Read [#254](https://github.com/UNopenGIS/7/issues/254), a first conversation with a mission's GIS staff, from scheduling to minutes.
3. Read [#976](https://github.com/UNopenGIS/7/issues/976), the open thread for the 2026 training lectures. The lecture of 2026-11-25 took place, and [#1010](https://github.com/UNopenGIS/7/issues/1010) closed on 2026-11-26 with the note "carried out".

### A small first contribution

Write one operational question in general terms, using information your institution has cleared for publication. Post it as an issue or a comment.

### What success may look like after one week

A technical contributor can read your question and propose an experiment.

### Where to go next

The responsibility entries in the [Field Guide](field-guide.md). Projects to browse: [m3xx-fleet](https://github.com/dwg7/m3xx-fleet) (a public monitoring dashboard for the Raspberry Pi fleet of a training course), [rpi3-server-guide](https://github.com/dwg7/rpi3-server-guide) (a hands-on guide to GeoServer and MapServer on a Raspberry Pi 3 with 1 GB), and [ferspas57](https://github.com/dwg7/ferspas57) (a link between FERSPAS and Staccato for the work of FAO and dwg5).

## Student or Researcher

### Who this path is for

People who learn by framing a question and testing it.

### What you can bring

Structured questions, literature, and time to read closely.

### Three first steps

1. Read [#361](https://github.com/UNopenGIS/7/issues/361), which builds global elevation tiles from published recipes.
2. Read [#740](https://github.com/UNopenGIS/7/issues/740). It lays out six steps for converting national coordinate-transformation parameters into open grid formats. A comment from September 2026 names a GeoTIFF grid for PROJ as the short-term route, and a comment from 2026-11-26 posts a candidate prompt that asks an AI assistant to write the converter and to verify it with PROJ test cases.
3. Choose one claim in either thread that you can check with public data.

### A small first contribution

Post a short log: the claim, your method, and what you observed. A review of the candidate prompt in #740 counts as well.

### What success may look like after one week

Another reader can repeat your method from the log.

### Where to go next

[Good First Experiments](good-first-experiments.md), then the Field Guide on disagreement and error. Projects to browse: [doverture](https://github.com/dwg7/doverture) (an exploratory comparison of building footprints from several sources), [plateau-juice](https://github.com/dwg7/plateau-juice) (attributes of buildings in a city 3D model, viewed apart from geometry), and [kcai-terrio](https://github.com/dwg7/kcai-terrio) (a knowledge instance that tracks one open-source project).

## Documentation, Data, or Community Contributor

### Who this path is for

People who write, curate, translate, and connect.

### What you can bring

Clear prose, careful data handling, and attention to what readers need.

### Three first steps

1. Read a recent weekly meetup issue, for example [#1031](https://github.com/UNopenGIS/7/issues/1031). Presenters post written updates there.
2. Choose one update and write two English sentences that summarise it for a reader who joined late.
3. Follow its links to the thread it comes from.

### A small first contribution

Post your English summary as a comment on the meetup issue, with the link to the source thread.

### What success may look like after one week

A reader who skipped the original update can state what was tried and what remains open.

### Where to go next

[Monthly Snapshot](monthly-snapshot.md), which turns threads into short records. Projects to browse: [kcai](https://github.com/dwg7/kcai) (principles for sharing knowledge made with AI as short, sourced Markdown traces), [miso-geo](https://github.com/dwg7/miso-geo) (geographic documentation in Markdown with a small map viewer), and [kikimimi](https://github.com/dwg7/kikimimi) (public-radio mentions of a volcano, treated as a social sensor).

[Back to index](index.md)

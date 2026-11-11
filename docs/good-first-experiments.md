---
title: Good First Experiments
---

# Good First Experiments

Each experiment below comes from a real thread in the dwg7 record, checked on 2026-11-11. You repeat one step of that thread, write down your conditions and your result, and share the record. A finished record counts as success.

Use open data, open tools, and files you may publish. Keep personal data and credentials out of every record.

## 1. Read one thread from question to result

<ul class="exp-meta"><li>20 minutes</li><li>Difficulty: easy</li></ul>

*For a reader of any background.*

- **Goal:** See the whole chain of question, experiment, result, and correction in one thread.
- **Inputs:** A browser and [#1003](https://github.com/UNopenGIS/7/issues/1003).
- **Steps:**

  1. Read the first post and state the question in one sentence.
  2. List the test conditions: hardware, software versions, data, load.
  3. Find the comment that corrects an earlier claim, and note what changed.

- **Visible outcome:** A five-line note: question, conditions, result, correction, open item.
- **What to record or share:** Your five lines, posted as a comment or kept as a file.
- **Next:** Experiment 9, which repeats a measurement.

## 2. Overlay two dates of one task

<ul class="exp-meta"><li>45 minutes in two sittings</li><li>Difficulty: easy</li></ul>

*For geospatial practitioners and data contributors.*

- **Goal:** Show a change over time from two public snapshots.
- **Inputs:** [#857](https://github.com/UNopenGIS/7/issues/857) and the public task page it links.
- **Steps:**

  1. Open the task page and note the progress figures with today's date.
  2. Return a week later and note them again.
  3. Place the two dates side by side in a table or a two-colour overlay.

- **Visible outcome:** One image or table that shows what changed between the two dates.
- **What to record or share:** The two dates, the source page, and the figures.
- **Next:** Experiment 3.

## 3. Observe one block of a mapping task

<ul class="exp-meta"><li>30 minutes</li><li>Difficulty: easy</li></ul>

*For geospatial practitioners.*

- **Goal:** Judge the quality of one small block, and say how you judged it.
- **Inputs:** [#857](https://github.com/UNopenGIS/7/issues/857) and the task it links.
- **Steps:**

  1. Choose one small block in a corner of the task area.
  2. Compare the map with the imagery behind it.
  3. List three features that match and three that differ.

- **Visible outcome:** A comment on #857 with your findings for that block.
- **What to record or share:** The block, the imagery you used, and the criteria you applied.
- **Next:** Experiment 2.

## 4. Check a download with a checksum

<ul class="exp-meta"><li>20 minutes</li><li>Difficulty: easy</li></ul>

*For anyone who handles large public files.*

- **Goal:** Confirm that two copies of a file are identical before one of them is removed.
- **Inputs:** Any public file that comes with a published SHA-256 value. [#999](https://github.com/UNopenGIS/7/issues/999) shows the practice at 400 GB scale.
- **Steps:**

  1. Download the file and its published checksum.
  2. Run `sha256sum` on the file.
  3. Compare the two values.

- **Visible outcome:** A match, or a mismatch with a note on where the copies diverge.
- **What to record or share:** The file name, the size, the checksum, and the date.
- **Next:** Experiment 5.

## 5. Serve a PMTiles file with range requests

<ul class="exp-meta"><li>45 minutes</li><li>Difficulty: moderate</li></ul>

*For software engineers.*

- **Goal:** Learn that a single PMTiles file serves tiles through HTTP range requests.
- **Inputs:** A small public PMTiles file, a static web server that supports range requests, and `curl`.
- **Steps:**

  1. Serve the file from a folder.
  2. Request bytes 0–511 with `curl -r 0-511` and read the response code.
  3. Open the file in a viewer that reads PMTiles over HTTP.

- **Visible outcome:** A response code 206 and a map in the viewer.
- **What to record or share:** The server, its version, and the response headers. [#567](https://github.com/UNopenGIS/7/issues/567) records a server switch made for this reason.
- **Next:** Experiment 6.

## 6. Compare a hosted PMTiles file with a local cache

<ul class="exp-meta"><li>90 minutes</li><li>Difficulty: moderate</li></ul>

*For software engineers.*

- **Goal:** Measure how a local cache changes the load time of tiles from a public host.
- **Inputs:** A public PMTiles file on a public host, Martin or Caddy, and the repository linked in [#642](https://github.com/UNopenGIS/7/issues/642).
- **Steps:**

  1. Load a map from the public host and record the time to first render.
  2. Start a local cache that points at the same file.
  3. Load the same map through the cache and record the time again.

- **Visible outcome:** Two timings for the same view, with the network noted.
- **What to record or share:** The host, the cache software and version, your network, and both timings.
- **Next:** Experiment 7.

## 7. Repeat a measurement from the Raspberry Pi thread

<ul class="exp-meta"><li>2 hours</li><li>Difficulty: moderate</li></ul>

*For software engineers.*

- **Goal:** Add your own hardware to a public comparison.
- **Inputs:** [#1003](https://github.com/UNopenGIS/7/issues/1003) and a small computer or a container with a memory limit.
- **Steps:**

  1. Read the setup and the load pattern in the thread.
  2. Run one server with the same kind of load.
  3. Record requests per second.

- **Visible outcome:** One row for your hardware next to the published rows.
- **What to record or share:** Hardware, versions, data size, load pattern, and results.
- **Next:** Experiment 1.

## 8. Make a PMTiles file from GeoJSON

<ul class="exp-meta"><li>60 minutes</li><li>Difficulty: moderate</li></ul>

*For GIS practitioners and software engineers.*

- **Goal:** Turn a small vector dataset into one PMTiles file.
- **Inputs:** A small open GeoJSON file, Docker, and the tutorial [Making PMTiles from GeoJSON with unvt](https://qiita.com/T-ubu/items/93d84b9d4bf5be608fda) (Japanese).
- **Steps:**

  1. Start the container from the tutorial.
  2. Run tippecanoe on your file with PMTiles output.
  3. Open the result in a PMTiles viewer.

- **Visible outcome:** A PMTiles file that displays your features.
- **What to record or share:** The input source and licence, the command, and the file size.
- **Next:** Experiment 5.

## 9. Style a vector tile map with charites

<ul class="exp-meta"><li>60 minutes</li><li>Difficulty: moderate</li></ul>

*For GIS practitioners and designers.*

- **Goal:** Edit a map style in readable files and see the result.
- **Inputs:** Node.js, `charites`, and the article [Using unvt/charites for Web Map Styling](https://qiita.com/k96mz/items/d43d89bad37f46d6b71c).
- **Steps:**

  1. Install charites and start from the sample style.
  2. Change the colour and width of one layer.
  3. Build the style and view it in a MapLibre page.

- **Visible outcome:** A rendered map with one layer restyled.
- **What to record or share:** The style files and a before-and-after screenshot.
- **Next:** Experiment 8.

## 10. Build a small elevation tile set

<ul class="exp-meta"><li>2 hours</li><li>Difficulty: challenging</li></ul>

*For software engineers and researchers.*

- **Goal:** Make open elevation tiles at a low zoom level, and check them against a known place.
- **Inputs:** Open elevation data, the article [Making small-scale RGB elevation tiles](https://qiita.com/T-ubu/items/ced8423e0ebeda8c9244) (Japanese), and [#361](https://github.com/UNopenGIS/7/issues/361) for the global version.
- **Steps:**

  1. Download a small open elevation dataset.
  2. Encode it as RGB tiles with the tool from the article.
  3. Display the tiles with terrain in a MapLibre page.

- **Visible outcome:** A 3D view of a known mountain or valley.
- **What to record or share:** The data source, licence, tool versions, and a screenshot.
- **Next:** repeat with a second elevation source and compare the two.

## 11. Summarise a weekly update

<ul class="exp-meta"><li>20 minutes</li><li>Difficulty: easy</li></ul>

*For documentation contributors and students.*

- **Goal:** Turn one written update into two clear sentences.
- **Inputs:** The latest weekly meetup issue, for example [#1027](https://github.com/UNopenGIS/7/issues/1027).
- **Steps:**

  1. Choose one update.
  2. Follow its link to the source thread.
  3. Write two sentences for a reader who joined late.

- **Visible outcome:** A comment on the meetup issue with your summary and the source link.
- **What to record or share:** The update you read and the thread it came from.
- **Next:** Experiment 1.

## 12. Write a one-page design note

<ul class="exp-meta"><li>60 minutes</li><li>Difficulty: moderate</li></ul>

*For AI builders and engineers.*

- **Goal:** State a design decision with its context, options, and consequences.
- **Inputs:** [#936](https://github.com/UNopenGIS/7/issues/936), which records a design as an ADR, and one decision from your own work.
- **Steps:**

  1. Read the ADR headings in #936.
  2. Write the same headings for your own decision.
  3. Ask one colleague to find the weakest sentence.

- **Visible outcome:** A one-page note with context, decision, options, and consequences.
- **What to record or share:** The note, and the change you made after the colleague's reading.
- **Next:** Experiment 1, applied to your own thread.

[Back to index](index.md)

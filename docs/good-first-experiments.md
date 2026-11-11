---
title: Good First Experiments
---

# Good First Experiments

Good first experiments are meant to be small, visible, reproducible, and low-pressure. They help people learn by doing with a small setup and an open role for everyone. The purpose is not to finish a major project in one session. It is to produce a small observation that can be shared, inspected, and discussed.

## 1. Compare two basemaps

<ul class="exp-meta"><li>20 minutes</li><li>Difficulty: easy</li></ul>

*For geospatial practitioners and curious newcomers.*

- **Goal:** Understand how map styling affects the readability of a familiar place.
- **Inputs or prerequisites:** a browser, a public mapping service, and a location you know well.
- **Steps:**

  1. Open two basemaps at the same location and zoom level.
  2. Compare labels, roads, terrain, and water features.
  3. Note which basemap makes the key information easier to read.

- **Visible outcome:** a short comparison note with screenshots or a description of the differences.
- **What to record or share:** what you were trying to read, which basemap was clearer, and why.
- **A natural next experiment:** test the same comparison on a second location or use case.


## 2. Open a public dataset and inspect its metadata

<ul class="exp-meta"><li>30 minutes</li><li>Difficulty: easy</li></ul>

*For people working with data, policy, or maps.*

- **Goal:** Learn how to assess whether a dataset is clear, usable, and documented enough for an experiment.
- **Inputs or prerequisites:** access to a public data portal or repository and a browser.
- **Steps:**

  1. Select a public dataset.
  2. Read its metadata: source, date coverage, license, and known limitations.
  3. Write a one-paragraph summary of what you verified and what remains unverified.

- **Visible outcome:** a short description of data quality and usefulness.
- **What to record or share:** what you could verify and what remains unclear.
- **A natural next experiment:** compare two datasets that address the same problem.


## 3. Plot a simple point layer

<ul class="exp-meta"><li>45 minutes</li><li>Difficulty: easy to moderate</li></ul>

*For software engineers, GIS practitioners, and beginners with limited setup.*

- **Goal:** See how a dataset transforms when it is displayed as a map layer.
- **Inputs or prerequisites:** a spreadsheet or CSV with coordinates, a basic GIS or mapping tool, and a browser.
- **Steps:**

  1. Prepare a small CSV with latitude and longitude columns, using public or invented coordinates.
  2. Load it in a mapping tool.
  3. Check the coordinate system and review the result on the map.

- **Visible outcome:** a map layer that shows points or features in a visible format.
- **What to record or share:** coordinate system choices, the number of features, and whether any records were missing or invalid.
- **A natural next experiment:** symbolize the same layer by category or time.


## 4. Recreate a familiar map view in a small notebook

<ul class="exp-meta"><li>60 minutes</li><li>Difficulty: moderate</li></ul>

*For people with coding experience and people testing lightweight tooling.*

- **Goal:** Learn whether a simple local workflow can quickly reproduce a familiar view.
- **Inputs or prerequisites:** a laptop, a notebook environment, a public example, and a small dataset.
- **Steps:**

  1. Take a small public map example.
  2. Reduce it to a single layer or style.
  3. Document each step needed to reproduce it locally.

- **Visible outcome:** a notebook or script that produces a local view.
- **What to record or share:** dependencies, assumptions, and what changed from the original example.
- **A natural next experiment:** compare a notebook workflow with a browser-based workflow.


## 5. Review a map for readability

<ul class="exp-meta"><li>30 minutes</li><li>Difficulty: easy</li></ul>

*For designers, practitioners, and documenters.*

- **Goal:** Check whether a map is understandable to non-specialist readers.
- **Inputs or prerequisites:** a map, a screenshot, or a published figure and a short rubric.
- **Steps:**

  1. Ask: Is the legend clear? Are labels legible? Is the map too dense?
  2. Write down the main message you take from the map.
  3. Compare it with the message the author intended, if known.

- **Visible outcome:** a short critique of readability and clarity.
- **What to record or share:** the main message, the areas of confusion, and recommended changes.
- **A natural next experiment:** compare the same map with an alternative legend or style.


## 6. Compare open APIs for a simple lookup

<ul class="exp-meta"><li>45 minutes</li><li>Difficulty: moderate</li></ul>

*For software engineers and technical practitioners.*

- **Goal:** Understand the difference between interfaces, data formats, and assumptions in practice.
- **Inputs or prerequisites:** access to public APIs, a browser or command line, and a simple request example.
- **Steps:**

  1. Pick a simple geospatial or public data API and read its terms of use and rate limits.
  2. Send the same small request to two APIs and inspect the responses.
  3. Compare required parameters, result formats, and documentation quality.

- **Visible outcome:** a short comparison sheet or notes on request syntax and results.
- **What to record or share:** pitfalls, error handling, and which API was easier to understand.
- **A natural next experiment:** build a very small script that normalizes the data from one of them.


## 7. Audit a public document for clarity

<ul class="exp-meta"><li>20 minutes</li><li>Difficulty: easy</li></ul>

*For documentation contributors, researchers, and analysts.*

- **Goal:** Learn how to identify unclear terminology, hidden assumptions, and missing context.
- **Inputs or prerequisites:** any public document, article, or note related to geospatial or technical work.
- **Steps:**

  1. Read a short section of the document.
  2. Mark terms that may be unfamiliar to a new reader.
  3. Note what the reader needs to know before interpreting the text.

- **Visible outcome:** a list of confusing phrases or missing explanations.
- **What to record or share:** specific wording changes and the problem they address.
- **A natural next experiment:** rewrite one paragraph to make it more accessible while keeping the technical meaning.


## 8. Check a dataset for obvious quality issues

<ul class="exp-meta"><li>30 to 60 minutes</li><li>Difficulty: easy to moderate</li></ul>

*For data contributors, researchers, and curious analysts.*

- **Goal:** Practice data validation with a single small script or a spreadsheet.
- **Inputs or prerequisites:** a small public dataset, a spreadsheet or script, and a clear question.
- **Steps:**

  1. Open the dataset and look for missing values, duplicate records, and coordinate anomalies.
  2. Check for obvious outliers.
  3. Summarize the findings and how you checked them.

- **Visible outcome:** a small data-quality note or table of issues found.
- **What to record or share:** the issue type, frequency, and whether it is likely to affect the analysis.
- **A natural next experiment:** compare quality issues across two related datasets.


## 9. Document one workflow as a plain-language checklist

<ul class="exp-meta"><li>20 minutes</li><li>Difficulty: easy</li></ul>

*For practitioners, technical contributors, and documentation-oriented participants.*

- **Goal:** Understand how much context is needed to make a repeatable process understandable to others.
- **Inputs or prerequisites:** a familiar workflow or task, a note-taking tool, and a few examples.
- **Steps:**

  1. Describe the task in plain language.
  2. List the assumptions it relies on.
  3. Write the sequence of actions from start to finish as a checklist.

- **Visible outcome:** a step-by-step checklist or process note.
- **What to record or share:** where the workflow is fragile, what assumptions are hidden, and what needs verification.
- **A natural next experiment:** ask another person to follow the checklist and note the confusion points.


## 10. Compare how different tools render the same dataset

<ul class="exp-meta"><li>45 to 90 minutes</li><li>Difficulty: moderate</li></ul>

*For technical practitioners and people exploring geospatial tooling.*

- **Goal:** Learn how the same dataset can look different across software due to styling, defaults, or processing assumptions.
- **Inputs or prerequisites:** one small public dataset and two tools with comparable functionality.
- **Steps:**

  1. Load the same data into two tools.
  2. Compare the resulting map appearance.
  3. Note differences in symbols, labels, and filtering.

- **Visible outcome:** a short comparison of rendering differences.
- **What to record or share:** default settings, visible differences, and whether the same interpretation holds across tools.
- **A natural next experiment:** compare the same dataset with a different projection or scale.


## 11. Record an observation from an open source issue or discussion

<ul class="exp-meta"><li>20 minutes</li><li>Difficulty: easy</li></ul>

*For contributors who want to participate through reading and writing first.*

- **Goal:** Learn how to turn an open question into an understandable summary with claims that match the evidence.
- **Inputs or prerequisites:** a public issue, a discussion thread, or a small open repository conversation.
- **Steps:**

  1. Read the initial comment and a few follow-ups.
  2. Identify the main question.
  3. Summarize the current state of the discussion in your own words.

- **Visible outcome:** a short summary with the key points and remaining uncertainty.
- **What to record or share:** the central question, assumptions, and any unresolved trade-offs.
- **A natural next experiment:** translate the summary into a more accessible plain-language note.


## 12. Run a very small reproducible check

<ul class="exp-meta"><li>15 to 40 minutes</li><li>Difficulty: easy to moderate</li></ul>

*For engineers, researchers, and anyone testing a local workflow.*

- **Goal:** Build confidence by verifying a small claim in a controlled way.
- **Inputs or prerequisites:** one existing tool or script, a reproducible example, and a clear expected result.
- **Steps:**

  1. Pick one small claim or task.
  2. Run it under known conditions.
  3. Compare the output with what you expected and record any difference.

- **Visible outcome:** a reproducible result, a screenshot, or a short log.
- **What to record or share:** the command, the result, and any unexpected differences.
- **A natural next experiment:** vary one input and see how the result changes.


These experiments are intentionally modest. The real value is in the observation, the verification, and the ability to share a result clearly enough for others to inspect.

[Back to index](index.md)

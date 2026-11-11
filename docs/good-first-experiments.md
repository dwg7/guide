# Good First Experiments

Good first experiments are meant to be small, visible, reproducible, and low-pressure. They help people learn by doing without requiring a large technical setup or a formal role in the group. The purpose is not to finish a major project in one session. It is to produce a small observation that can be shared, inspected, and discussed.

## 1. Compare two basemaps

- Title: Compare two basemaps
- For whom: geospatial practitioners and curious newcomers
- Estimated time: 20 minutes
- Difficulty: easy
- Goal: Understand how map styling affects the readability of a familiar place.
- Inputs or prerequisites: a browser, a public mapping service, and a location you know well.
- Steps: Open two basemaps with the same viewport, compare labels, roads, terrain, and water features, and note which makes the key information easier to read.
- Visible outcome: a short comparison note with screenshots or a description of the differences.
- What to record or share: what you were trying to read, which basemap was clearer, and why.
- A natural next experiment: test the same comparison on a second location or use case.

## 2. Open a public dataset and inspect its metadata

- Title: Inspect metadata in a public dataset
- For whom: people working with data, policy, or maps
- Estimated time: 30 minutes
- Difficulty: easy
- Goal: Learn how to assess whether a dataset is clear, usable, and documented enough for an experiment.
- Inputs or prerequisites: access to a public data portal or repository and a browser.
- Steps: Select a public dataset, read its metadata, identify its source, date coverage, license, and known limitations, and then write a one-paragraph summary.
- Visible outcome: a short description of data quality and usefulness.
- What to record or share: what you could verify and what remains unclear.
- A natural next experiment: compare two datasets that address the same problem.

## 3. Plot a simple point layer

- Title: Plot a simple point layer
- For whom: software engineers, GIS practitioners, and beginners with limited setup
- Estimated time: 45 minutes
- Difficulty: easy to moderate
- Goal: See how a dataset transforms when it is displayed as a map layer.
- Inputs or prerequisites: a spreadsheet or CSV with coordinates, a basic GIS or mapping tool, and a browser.
- Steps: Prepare a small CSV, load it in a mapping tool, verify the coordinate system, and review the map result.
- Visible outcome: a map layer that shows points or features in a visible format.
- What to record or share: coordinate system choices, the number of features, and whether any records were missing or invalid.
- A natural next experiment: symbolize the same layer by category or time.

## 4. Recreate a familiar map view in a small notebook

- Title: Recreate a familiar map in a notebook
- For whom: people with coding experience and people testing lightweight tooling
- Estimated time: 60 minutes
- Difficulty: moderate
- Goal: Learn whether a simple local workflow can quickly reproduce a familiar view.
- Inputs or prerequisites: a laptop, a notebook environment, a public example, and a small dataset.
- Steps: Take a small map example, reduce it to a single layer or style, and document the steps required to reproduce it locally.
- Visible outcome: a notebook or script that produces a local view.
- What to record or share: dependencies, assumptions, and what changed from the original example.
- A natural next experiment: compare a notebook workflow with a browser-based workflow.

## 5. Review a map for accessibility

- Title: Review map usability for non-expert readers
- For whom: designers, practitioners, and documenters
- Estimated time: 30 minutes
- Difficulty: easy
- Goal: Check whether a map is understandable to people who are not specialists.
- Inputs or prerequisites: a map, a screenshot, or a published figure and a short rubric.
- Steps: Ask a few basic questions: Is the legend clear? Are labels legible? Is the map too dense? What is the main message?
- Visible outcome: a short critique of readability and clarity.
- What to record or share: the main message, the areas of confusion, and recommended changes.
- A natural next experiment: compare the same map with an alternative legend or style.

## 6. Compare open APIs for a simple lookup

- Title: Compare two APIs with one small request
- For whom: software engineers and technical practitioners
- Estimated time: 45 minutes
- Difficulty: moderate
- Goal: Understand the difference between interfaces, data formats, and assumptions in practice.
- Inputs or prerequisites: access to public APIs, a browser or command line, and a simple request example.
- Steps: Pick a simple geospatial or public data API, inspect responses, note required parameters, and compare the result format and documentation quality.
- Visible outcome: a short comparison sheet or notes on request syntax and results.
- What to record or share: pitfalls, error handling, and which API was easier to understand.
- A natural next experiment: build a very small script that normalizes the data from one of them.

## 7. Audit a public document for clarity

- Title: Audit one public document for clarity
- For whom: documentation contributors, researchers, and analysts
- Estimated time: 20 minutes
- Difficulty: easy
- Goal: Learn how to identify unclear terminology, hidden assumptions, and missing context.
- Inputs or prerequisites: any public document, article, or note related to geospatial or technical work.
- Steps: Read a short section, identify terms that may be unfamiliar, and ask what the reader needs to know before interpreting the text.
- Visible outcome: a list of confusing phrases or missing explanations.
- What to record or share: specific wording changes and the problem they address.
- A natural next experiment: rewrite one paragraph to make it more accessible without changing the technical meaning.

## 8. Check a dataset for obvious quality issues

- Title: Check a public dataset for obvious quality issues
- For whom: data contributors, researchers, and curious analysts
- Estimated time: 30 to 60 minutes
- Difficulty: easy to moderate
- Goal: Practice data validation without needing a full pipeline.
- Inputs or prerequisites: a small public dataset, a spreadsheet or script, and a clear question.
- Steps: Look for missing values, coordinate anomalies, duplicate records, and obvious outliers; then summarize the findings.
- Visible outcome: a small data-quality note or table of issues found.
- What to record or share: the issue type, frequency, and whether it is likely to affect the analysis.
- A natural next experiment: compare quality issues across two related datasets.

## 9. Document one workflow as a plain-language checklist

- Title: Turn one workflow into a checklist
- For whom: practitioners, technical contributors, and documentation-oriented participants
- Estimated time: 20 minutes
- Difficulty: easy
- Goal: Understand how much context is needed to make a repeatable process understandable to others.
- Inputs or prerequisites: a familiar workflow or task, a note-taking tool, and a few examples.
- Steps: Describe the task in plain language, list assumptions, and then write the sequence of actions from start to finish.
- Visible outcome: a step-by-step checklist or process note.
- What to record or share: where the workflow is fragile, what assumptions are hidden, and what needs verification.
- A natural next experiment: ask another person to follow the checklist and note the confusion points.

## 10. Compare how different tools render the same dataset

- Title: Compare rendering in different tools
- For whom: technical practitioners and people exploring geospatial tooling
- Estimated time: 45 to 90 minutes
- Difficulty: moderate
- Goal: Learn how the same dataset can look different across software due to styling, defaults, or processing assumptions.
- Inputs or prerequisites: one small public dataset and two tools with comparable functionality.
- Steps: Load the same data into two tools, compare the resulting map appearance, and note differences in symbols, labels, and filtering.
- Visible outcome: a short comparison of rendering differences.
- What to record or share: default settings, visible differences, and whether the same interpretation holds across tools.
- A natural next experiment: compare the same dataset with a different projection or scale.

## 11. Record an observation from an open source issue or discussion

- Title: Read one public discussion and summarize it
- For whom: contributors who want to participate without changing code immediately
- Estimated time: 20 minutes
- Difficulty: easy
- Goal: Learn how to turn an open question into an understandable summary without overclaiming.
- Inputs or prerequisites: a public issue, a discussion thread, or a small open repository conversation.
- Steps: Read the initial comment and a few follow-ups, identify the main question, and summarize the current state of the discussion.
- Visible outcome: a short summary with the key points and remaining uncertainty.
- What to record or share: the central question, assumptions, and any unresolved trade-offs.
- A natural next experiment: translate the summary into a more accessible plain-language note.

## 12. Run a very small reproducible check

- Title: Reproduce one small and visible result
- For whom: engineers, researchers, and anyone testing a local workflow
- Estimated time: 15 to 40 minutes
- Difficulty: easy to moderate
- Goal: Build confidence by verifying a small claim in a controlled way.
- Inputs or prerequisites: one existing tool or script, a reproducible example, and a clear expected result.
- Steps: Pick one small claim or task, run it under known conditions, and compare the output to what was expected.
- Visible outcome: a reproducible result, a screenshot, or a short log.
- What to record or share: the command, the result, and any unexpected differences.
- A natural next experiment: vary one input and see how the result changes.

These experiments are intentionally modest. The real value is in the observation, the verification, and the ability to share a result clearly enough for others to inspect.

[Back to index](index.md)

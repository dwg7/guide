---
title: dwg7 Field Guide
---

# dwg7 Field Guide

This field guide explains how dwg7 works through the logic behind its habits. Each answer states the habit, the reason for it, and where to see it in the public record (checked 2026-11-11 at [UNopenGIS/7](https://github.com/UNopenGIS/7/issues)).

## The logic of the record

### 1. Why does the work happen in public issues and repositories?

A claim can be checked only when its evidence is visible. Public issues hold the question, the method, and the result in one place, so a reader can verify each step and a later contributor can continue from it.

### 2. What is dwg7?

dwg7 is Domain Working Group 7 of the UN Open GIS Initiative, working on "Smart Maps". The group works through a public record of questions, experiments, results, and corrections. Membership follows from contributing to that record.

### 3. How does dwg7 relate to standards, vendors, and funded programmes?

The record shows a working group that tests tools and data. It adopts or adapts existing open standards and software, and it publishes the evidence behind each choice. Statements about funding or institutional authority belong with the institution that holds them, and the guide links to the source.

### 4. Why do experiments appear before finished products?

An experiment states its conditions and gives a result that others can repeat. A finished product can grow from a sequence of such results. The early record shows why each design decision was taken.

### 5. What does a good claim look like?

A good claim names its conditions. For example, a throughput figure comes with the hardware, the software version, the data size, and the load pattern ([#1003](https://github.com/UNopenGIS/7/issues/1003)). Conditions let a reader decide whether the result applies to their own case.

### 6. How are errors handled?

An error is corrected in the same thread where it appeared, with the reason. In #1003, the author confirmed that an earlier explanation of environment variables was wrong, restated the finding, and fixed the written guide. Visible corrections raise the trust in the remaining claims.

### 7. What happens to unfinished questions?

They stay open and visible. In #1003 the Raspberry Pi 3 measurements are listed as the next step. An open item tells a newcomer exactly where a contribution helps.

## Rhythm and vocabulary

### 8. How does the weekly meetup work?

A weekly issue (titled with date and time, for example 12:30–12:55 JST) collects written updates from presenters as comments. The live session of about 25 minutes then moves through the updates in an agreed order. Written updates give remote participants and later readers the same information as the live audience.

### 9. What do the labels mean?

Labels organise the record by purpose: `meetup` for weekly sessions, `information` for items to share, `adopt` for candidates for adoption, `in progress` for active work, and `priority/MUST`, `priority/SHOULD`, `priority/MAY` for attention order. Check the issue itself for the exact use in each case.

### 10. In which language is the record written?

Many issues are written in Japanese, and some in English. Machine translation reads technical issues well, and an English summary comment helps international readers and is welcome.

### 11. How do I introduce a question?

Write the context, the practical problem, the evidence you have, and the kind of feedback you seek. A short, specific introduction with a link to related issues connects quickly to existing work.

### 12. How do I ask about unfamiliar terms?

Ask directly in the thread. A plain-language question exposes an undefined term, and the answer improves the record for the next reader.

## Contribution and roles

### 13. Which contributions help?

Clear questions, reproducible examples, data checks, documentation, translation, summaries, and reviews of other people's results all help. Each of them adds evidence or clarity to the chain from question to reuse.

### 14. Can I contribute without writing code?

Yes. Many steps of the chain are non-code work: stating a user need, checking a dataset, repeating an experiment on a different machine, and translating a thread. In #1003 the decisive review step came from repeating the test on other operating systems.

### 15. What gives a contribution influence?

Evidence and reproducibility give influence. A result that others can repeat shapes the discussion, whatever the title or affiliation of its author.

### 16. How should disagreement be expressed?

Point to the condition or the measurement that differs, and propose a test that settles it. The exchange in #1003 about FastCGI environments follows this pattern: hypothesis, check, confirmation.

## Responsibility and context

### 17. How are public-sector responsibilities respected?

Contributors from public institutions describe operational needs in general terms and publish only information cleared for publication. Open collaboration works with data classification and institutional rules.

### 18. How should AI-assisted work be handled?

State where AI contributed, and verify its output with the same checks as any other source. Several dwg7 threads combine AI assistants and geospatial data, and the neighbouring dwg5 focuses on Geo AI. A claim from an AI assistant enters the record once a person has checked it against evidence.

### 19. What can be published?

Publish open data, public information, and your own results. Keep personal data, private messages, credentials, and unpublished operational details in their own secure places. Cite the licence and source of every dataset you use.

### 20. What is a good next step?

Read one thread from question to result, then reproduce one small step from it. Post what you observed as a comment. That sequence already completes the chain once.

The chain turns attention into evidence, and evidence into reuse: observe, try, record, share.

[Back to index](index.md)

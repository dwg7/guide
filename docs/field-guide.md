---
title: dwg7 Field Guide
---

# dwg7 Field Guide

This guide explains how dwg7 works. Each answer names a habit, gives its reason, and points to a thread where you can see it. Threads come from the [dwg7 issues](https://github.com/UNopenGIS/7/issues), checked on 2026-11-11. Where the record is silent, the answer says so and offers a suggestion marked as this guide's own.

## Why the record is public

### 1. Why does the work happen in public issues?

A claim can be checked when its evidence is visible. An issue holds the question, the method, and the result together. A reader verifies each step, and a later contributor continues from the last one. Of the 967 closed issues, 919 carry at least one comment.

### 2. What is dwg7?

dwg7 is Domain Working Group 7 of the UN Open GIS Initiative, working on "Smart Maps". Its working surface is the [UNopenGIS/7](https://github.com/UNopenGIS/7) repository. The repository description states the purpose: keep web maps open for a better world.

### 3. How does dwg7 relate to standards, vendors, and funded programmes?

The record shows a group that tests open tools and open data and publishes the evidence. It adopts existing open software and formats, such as PMTiles and Martin, and works with outside projects, such as an elevation-tile project ([#920](https://github.com/UNopenGIS/7/issues/920)) and a humanitarian mapping network ([#857](https://github.com/UNopenGIS/7/issues/857)). For funding and institutional authority, the primary sources are the institutions themselves.

### 4. Why do experiments come before finished products?

An experiment states its conditions and yields a result that others can repeat. A product can grow from a sequence of such results. Thread [#642](https://github.com/UNopenGIS/7/issues/642) began as a question about a tile cache and ended as a working delivery design.

## The ten habits

### 5. What does a good claim look like?

It carries its conditions. In [#1003](https://github.com/UNopenGIS/7/issues/1003), each throughput figure comes with the hardware, the software version, the data size, and the load. Conditions let a reader decide whether the result applies to their case.

### 6. How do contributors state a hypothesis?

They label it. In [#567](https://github.com/UNopenGIS/7/issues/567), a contributor writes that a power shortage is the hypothesis for a failing disk, then swaps ports and reports that the setup became stable. The label separates a guess from a finding.

### 7. How are errors handled?

They are corrected in the thread where they appeared, with the reason. In #1003, the author confirmed that an earlier explanation about environment variables was wrong, restated the finding, and fixed the written guide. In #642, a superseded plan stays visible as struck-through text. A visible correction raises trust in the claims around it.

### 8. How do contributors explain a design?

They write the reasons. #642 explains a delivery design in a short chain: keep a public source at high availability, and add a local cache where speed is needed. #936 records a design as a decision record with context, options, and consequences.

### 9. How does a thread invite repetition?

It publishes code and steps. In #642 the experiment's repository and an article describe the steps, and another contributor followed them and asked a question about local files. A repeated experiment adds evidence, and a question exposes a gap.

### 10. What happens to unfinished questions?

They stay open and visible. #1003 lists a measurement on a smaller Raspberry Pi as the next step. #567 closed with the note that development paused until field use brings lessons. Both name where a contribution helps.

### 11. How do contributors treat shared resources?

They plan for the load they place on others. In [#920](https://github.com/UNopenGIS/7/issues/920) the stated reason for hosting a full copy of a public imagery tile set is to spare the public source from repeated bulk requests. In [#999](https://github.com/UNopenGIS/7/issues/999) a contributor checked a byte-for-byte match and left a week for comments before moving files.

### 12. When does a thread close?

When the idea has become part of the work. #936 closed with the note that the concept had settled. #642 closed after the result was reported elsewhere. Closed threads remain readable and open to comment.

### 13. How do contributors start?

From someone else's work. [#361](https://github.com/UNopenGIS/7/issues/361) builds on published articles about elevation tiles. #920 begins from an invitation in another project's issue. Later contributors, in turn, repeat earlier published exercises and record their own results.

### 14. How do contributors observe slowly?

They create a quiet place and compare dates. [#857](https://github.com/UNopenGIS/7/issues/857) collects observations on a mapping task, with two dates overlaid in colour and progress figures recorded in April and May 2026.

## Rhythm and vocabulary

### 15. How does the weekly meetup work?

Each week has one issue, titled with its date and time (Tuesdays, 12:30–12:55 JST). Presenters post written updates before the session, and the live session of about 25 minutes follows an agreed order. Written updates give remote participants and later readers the same information as the live audience. See [#1027](https://github.com/UNopenGIS/7/issues/1027).

### 16. What do the labels mean?

`priority/MUST`, `priority/SHOULD`, and `priority/MAY` order attention. Closed threads show it: the middle time to close is 14, 23, and 32 days. `information` marks items to share, `adopt` marks candidates for adoption, `in progress` marks active work, `request for comments` invites response, `help wanted` asks for hands, `event` marks events, and `meetup` marks weekly sessions. The meanings above come from how the labels are used, since the record holds no definition document.

### 17. In which language is the record written?

In 2025 and 2026, two of every three new issues contain Japanese in the title or the opening text, and the rest are mostly in English. Machine translation reads technical threads well. This guide suggests a short English comment when you want international readers to join.

## Who contributes and how

### 18. Which contributions help?

Clear questions, reproducible examples, data checks, repeated measurements, written summaries, and reviews of other people's results. In #1003 the decisive review came from repeating the test on other operating systems. In [#575](https://github.com/UNopenGIS/7/issues/575) the work was logistics: sixteen small computers, addresses, and a plan for a training room. Each contribution adds evidence or clarity to the chain.

### 19. How should AI-assisted work be handled?

The record gives examples. [#936](https://github.com/UNopenGIS/7/issues/936) designs how a language model hands a map request to a map-making service, and [#1014](https://github.com/UNopenGIS/7/issues/1014) offers a semantic search over a large public catalogue. This guide suggests naming where AI helped and checking its output as you would check any source.

### 20. What can be published?

Open data, public information, and your own results. This guide suggests keeping personal data, private messages, credentials, and unpublished operational details out of the thread, and citing the licence and source of each dataset. Contributors from public institutions can describe an operational question in general terms and publish what their institution has cleared.

## A good next step

Read one thread from question to result. Repeat one small step of it. Post what you observed. That sequence completes the chain once.

[Back to index](index.md)

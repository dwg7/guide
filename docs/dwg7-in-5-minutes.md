---
title: dwg7 in 5 Minutes
---

# dwg7 in 5 Minutes

dwg7 is Domain Working Group 7 of the UN Open GIS Initiative. It works on "Smart Maps": keeping web maps open so that people can build, test, and reuse them. Its working method is a chain of public records: a question, an experiment, a measured result, a review, and a correction. This page is a snapshot of that method as read from the public record on 2026-11-11. The issues are the primary source and this page is a reading aid.

## The method in one chain

> question → experiment → result with conditions → review and correction → reuse

Each link leaves a public trace, so any reader can follow the reasoning from the question to the conclusion.

## A worked example

The issue "GeoServer / MapServer on a Raspberry Pi" ([UNopenGIS/7#1003](https://github.com/UNopenGIS/7/issues/1003)) shows the whole chain in one thread:

1. **Question.** Where does a small, low-cost computer reach its limit when serving web map data? Low-cost deployments such as weather-station networks motivate the question.
2. **Experiment.** A contributor ran GeoServer and MapServer on a Raspberry Pi 4B with 5,000 random points and 4 workers sending 20 WMS GetMap requests each.
3. **Result with conditions.** MapServer under CGI reached 5.1–5.5 requests per second and GeoServer reached 7.6–13.6. MapServer under FastCGI reached 16.9–22.5 and GeoServer 13.1–13.6. The author attributed the first gap to per-request process cost in CGI.
4. **Review and correction.** A second contributor repeated the work on other operating systems and found that the working configuration depended on MapServer's default config path. The first contributor confirmed this and corrected two earlier statements in the same thread.
5. **Reuse and next step.** A hands-on guide for a Raspberry Pi 3 with 1 GB memory was published. Measurements on that device remain open.

Three habits of the method are visible here. A claim carries its test conditions. A correction appears next to the claim it fixes. An open item stays visible as an open item.

## Where the work happens

- **Weekly meetup.** A 25-minute online session (Tuesdays, 12:30–12:55 JST) is organised as a GitHub issue. Presenters post updates as comments before the session, and the session itself moves quickly through the written updates.
- **Issues as the working surface.** Labels such as `priority/MUST`, `priority/SHOULD`, `priority/MAY`, `information`, `adopt`, `in progress`, and `meetup` organise the record. Many issues are written in Japanese, and machine translation reads them well.
- **Neighbouring groups.** An issue tracks collaboration between dwg5 (Geo AI) and dwg7, for example around semantic access to datasets from AI assistants.

## Why the method fits the field

International and public-sector geospatial work values reproducible claims, clear provenance, and decisions that survive staff changes. Open technology supplies the tools to publish all three: repositories hold code and data, issues hold reasoning, and releases hold results. dwg7 sits where these two needs meet.

## Your path in four steps

1. **Observe.** Open the [issue list](https://github.com/UNopenGIS/7/issues) and read one thread from question to result.
2. **Choose a question.** Pick a friction from your own work that fits the chain above.
3. **Try.** Run a small experiment from [Good First Experiments](good-first-experiments.md) with the same habits: state conditions, record results.
4. **Share.** Post the record as an issue comment or in your own public place, linked from a related issue.

Continue with [Onboarding Paths](onboarding-paths.md) to find a route that matches your background.

[Back to index](index.md)

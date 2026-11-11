# Contributing to the dwg7 guide

This guide follows the method it describes: a question, an experiment, a result with conditions, a review, and a correction. A contribution to the guide uses the same chain, so every change leaves a record that the next reader can check.

## What helps

- **A repeated experiment.** Run one experiment from [Good First Experiments](docs/good-first-experiments.md). Report your conditions and your result. A changed step, a missing prerequisite, or a broken link becomes an edit.
- **A fresh check.** Open a thread cited in the guide, read it again, and report what changed since the date on the page.
- **A correction.** Point to the sentence, and to the thread or source that shows the right reading.
- **A clearer sentence.** Shorter and more concrete wins.
- **A new path or experiment.** Base it on a thread in the [dwg7 issues](https://github.com/UNopenGIS/7/issues) that you have read and repeated.
- **A translation.** Add the language beside the English page and keep the English page as the source.

Each of these counts as a full contribution, and code and prose count alike.

## How to propose a change

1. **Open an issue** that states the question: which page, which sentence, what you observed.
2. **Say how you know.** Link the thread, article, or measurement. Give the date you read it.
3. **Open a pull request** that changes one page or one idea. Name the issue in the description.
4. **Expect a review.** A reviewer may repeat your check. Corrections stay visible in the pull request.

## Rules for the pages in `docs/`

- **Cite the record.** Each claim about dwg7 links a thread in the [dwg7 issues](https://github.com/UNopenGIS/7/issues) and sits on a page that states the date of the check. The issues are the source, and the guide is a reading aid.
- **State conditions beside numbers.** Hardware, versions, data, and load stand next to every figure.
- **Mark suggestions.** Where the record is silent, write "This guide suggests" and keep the suggestion short.
- **Write dwg7 in lowercase.** Use the same form in headings and at the start of sentences.
- **Write plain international English.** Prefer short sentences, concrete nouns, and active verbs. Cut every word that adds nothing. State what the record shows.
- **Name roles.** Write "a contributor" and give the issue number. Add a name only when the thread requires credit.
- **Try every experiment.** Run it yourself before you add or change it, and record the date and your environment in the pull request.
- **Publish what you may.** Use open data, public information, and your own results. Keep personal data, private messages, and credentials out of every file.
- **Keep links relative** between pages in `docs/`, and link outside `docs/` with full URLs.
- **Keep five pages as the core.** Link any new page from the page it supports.

## Preview the site

The site is Jekyll with a small layout and stylesheet in `docs/`. From the repository root:

```bash
gem install jekyll jekyll-relative-links jekyll-optional-front-matter jekyll-seo-tag webrick
jekyll serve -s docs --baseurl ""
```

Open `http://localhost:4000/` and check the page you changed, on a narrow window as well as a wide one.

## Material behind the pages

- [`miso/dwg7.md`](miso/dwg7.md) collects the record in one Markdown file: statistics, representative threads, lessons, and open questions. Add to it first when you learn something new, and write the guide from it.
- `miso/scripts/` holds small scripts that summarise an export of the issues and index the articles used as background. Re-run them to refresh the figures.
- [`AGENTS.md`](AGENTS.md) holds the editorial principles for people and assistants who maintain the repository.

## Checks before you submit

1. Does the change help a first-time reader find a next step?
2. Does each claim link to the record, with the date of the check?
3. Do the links and the Markdown work on GitHub and on the published site?
4. Does the English read plainly, in the positive form?
5. Does the change contain only information that may be published?

## Recognition

A merged change appears in the repository history under your name. The guide credits the threads it draws on by issue number.

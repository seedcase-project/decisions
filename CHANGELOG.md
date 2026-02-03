# Changelog

Since we follow [Conventional
Commits](https://decisions.seedcase-project.org/why-conventional-commits),
we're able to automatically create formal "releases" of the website
based on our commit messages. Releases in the context of websites are
simply snapshots in time of the website content. We use
[Commitizen](https://decisions.seedcase-project.org/why-semantic-release-with-commitizen)
to automatically create these releases using
[SemVer](https://semverdoc.org) as the version numbering scheme.

Because releases are created based on commit messages, a new release is
created quite often---sometimes several times in a day. This also means
that any individual release will not have many changes within it. Below
is a list of the releases we've made so far, along with what was changed
within each release.

## 0.5.0 (2026-02-03)

### Feat

- :sparkles: post on iterative and incremental with Kanban development (#239)

## 0.4.0 (2026-01-28)

### Feat

- :sparkles: post on using Cyclopts for CLIs in Python (#237)

## 0.3.2 (2026-01-27)

### Refactor

- :wrench: standardise and simplify some of the categories (#242)

## 0.3.1 (2026-01-26)

### Refactor

- :arrow_up: update theme and files from template (#238)

## 0.3.0 (2025-12-18)

### Feat

- :sparkles: add why mypy post (#227)

## 0.3.0 (2025-12-18)

### Feat

- :sparkles: add why mypy post (#227)

## 0.2.0 (2025-09-12)

### Feat

- :sparkles: post on why we use Copier (#195)
- :sparkles: decision on why we use or recommend CC0 for data (#194)
- :sparkles: add alt labels to navbar logos
- :sparkles: added a category listing to the page (#74)
- add reference section
- :sparkles: add category listing to page
- :tada: Set up basic Quarto and Git repo standard files

### Fix

- :pencil2: wrong single quote character was used (#213)
- :pencil2: there was a double quote accidentally (#128)
- update link to values and principles
- change contents path so fit new folder structure
- remove whitespace
- shorten alt texts
- elaborate on alt labels
- add "Decisions" to logo alt
- :fire: remove old favicons
- remove duplicate categories from yaml header
- change headers to sentence case
- add missing "are"
- :pencil2: apply suggestions from code review
- :coffin: Remove unnecessary style code for column widths
- :globe_with_meridians: Fixed link to internal decision post
- :pencil2: The yaml header was incomplete.
- :globe_with_meridians: Fix links to internal and external files/content
- :rotating_light: Fixed URLs that we're resolving

### Refactor

- :recycle: decide on uv, not Poetry (#170)
- :recycle: reduce number of categories, remove redundant/unecessary ones

# Changelog

Since we follow [Conventional
Commits](https://decisions.seedcase-project.org/why-conventional-commits/),
we're able to automatically create formal "releases" of the website based on our
commit messages. Releases in the context of websites are simply snapshots in
time of the website content. We use
[Cocogitto](https://decisions.seedcase-project.org/why-semantic-release-with-cocogitto/)
to be able to automatically create these releases, which uses
[SemVar](https://semverdoc.org) as the version numbering scheme, and
[git-cliff](https://decisions.seedcase-project.org/why-changelog-with-git-cliff/)
to generate the changelog based on the commit messages.

Because releases are created based on commit messages, a new release is created
quite often---sometimes several times in a day. This also means that any
individual release will not have many changes within it. Below is a list of the
releases we've made so far, along with what was changed within each release.

Commits from bots, like `dependabot` or `pre-commit-ci`, are not included in the
changelog.

## [0.13.0](https://github.com/seedcase-project/decisions/compare/0.12.0..0.13.0) - 2026-08-13

### ✨ Features

- Post on using Python for data engineering
  [#280](https://github.com/seedcase-project/decisions/pull/280) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([32351c2](https://github.com/seedcase-project/decisions/commit/32351c2137bfa2957fbecfee19ed97cfbded8021))
- Post on why to use Rust for making software
  [#279](https://github.com/seedcase-project/decisions/pull/279) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([7eb432a](https://github.com/seedcase-project/decisions/commit/7eb432ab40919758bd1a91d1155ed862384fdf79))
- Add post on using pytask for workflow management
  [#306](https://github.com/seedcase-project/decisions/pull/306) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([74eeff2](https://github.com/seedcase-project/decisions/commit/74eeff25186a66032bb480b86665e4bc6a48cb1b))

### 🐛 Fixes

- Fix or remove old or broken URLs
  [#305](https://github.com/seedcase-project/decisions/pull/305) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([e2783fa](https://github.com/seedcase-project/decisions/commit/e2783fac5755d446ae57678f8c0598abcd8d11ff))

### ♻️ Refactor

- Convert 'Why Pandera' to previous decision
  [#304](https://github.com/seedcase-project/decisions/pull/304) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([82a1e2f](https://github.com/seedcase-project/decisions/commit/82a1e2f0a49b1318cbe15a79c8d5f9b226427489))
- Revise post to decide on Pyrefly, not mypy
  [#313](https://github.com/seedcase-project/decisions/pull/313) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([92008bc](https://github.com/seedcase-project/decisions/commit/92008bc154971ed282e2a6548d477caf146df06f))
- Update `.md`s from template
  [#325](https://github.com/seedcase-project/decisions/pull/325) by
  [`@signekb`](https://github.com/signekb)
  ([9493179](https://github.com/seedcase-project/decisions/commit/949317918b79ed3c4eddbf77b4ad86a601ef3977))

### 📝 Documentation

- Minor update to docs like README from template
  [#289](https://github.com/seedcase-project/decisions/pull/289) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([e26fa09](https://github.com/seedcase-project/decisions/commit/e26fa09cc639d2a6578860194253480ddb4382f4))

### 👷 CI/CD

- Switch to non-reusable workflows, from t-squared
  [#284](https://github.com/seedcase-project/decisions/pull/284) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([ff9a928](https://github.com/seedcase-project/decisions/commit/ff9a92842e43de32b12384c0a3b9eebcf9a07977))
- Only check commit messages from latest tag
  [#290](https://github.com/seedcase-project/decisions/pull/290) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([9580d18](https://github.com/seedcase-project/decisions/commit/9580d18dbd42068b0a13dd7e73ea82babeedc2c1))
- Switch to single quotes, workflows can't use double
  [#291](https://github.com/seedcase-project/decisions/pull/291) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([f684dfb](https://github.com/seedcase-project/decisions/commit/f684dfb5e2d90791da13257e3ad607d1117489ee))
- Remove Conventional Commit scope from dependabot
  [#294](https://github.com/seedcase-project/decisions/pull/294) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([ac5caa9](https://github.com/seedcase-project/decisions/commit/ac5caa9ecdb5daa6b568b4f6fd6c46d4808eff4b))
- Add if contributor guard in new contributors section in `cliff.toml`
  [#327](https://github.com/seedcase-project/decisions/pull/327) by
  [`@signekb`](https://github.com/signekb)
  ([cff491c](https://github.com/seedcase-project/decisions/commit/cff491c6aeeb8b3fdee3737ea1a6b6162d870789))

### 👩‍💻 Miscellaneous

- Add more config and move existing into `.config/`
  [#285](https://github.com/seedcase-project/decisions/pull/285) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([50ae44d](https://github.com/seedcase-project/decisions/commit/50ae44d11bdf2850ad72e1042967a9f2a054e91c))
- Match justfile to template changes
  [#292](https://github.com/seedcase-project/decisions/pull/292) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([eee892a](https://github.com/seedcase-project/decisions/commit/eee892a99704486ad76d8cf6b86c8821c869a625))
- Remove scopes and use panache in VS Code
  [#293](https://github.com/seedcase-project/decisions/pull/293) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([82abeb2](https://github.com/seedcase-project/decisions/commit/82abeb2e566708372088cbfe6e2006e03d3175c9))
- Remove leftover files and TODO items
  [#297](https://github.com/seedcase-project/decisions/pull/297) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([3426301](https://github.com/seedcase-project/decisions/commit/3426301efee1e5743ef95ea13d9eb90b5de54b05))
- Ignore cache folder in `.gitignore`
  [#296](https://github.com/seedcase-project/decisions/pull/296) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([a3c2919](https://github.com/seedcase-project/decisions/commit/a3c291952c5546dbb379d2af144a5c7946ad2eac))
- Use new team for CODEOWNER
  [#295](https://github.com/seedcase-project/decisions/pull/295) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([9d1252e](https://github.com/seedcase-project/decisions/commit/9d1252e88b2831f8ce54d6eee9afa65fcbb82336))
- Add navbar a part of Seedcase badge
  [#324](https://github.com/seedcase-project/decisions/pull/324) by
  [`@signekb`](https://github.com/signekb)
  ([fc81d67](https://github.com/seedcase-project/decisions/commit/fc81d67b52dde9aba172c87ce3da7f7e8f3ab55c))
- Update configs and tools from template
  [#322](https://github.com/seedcase-project/decisions/pull/322) by
  [`@signekb`](https://github.com/signekb)
  ([c0dd745](https://github.com/seedcase-project/decisions/commit/c0dd745190ae2fb43efa6fbe46ac54e1a1cfbf5f))
- Exclude URL checks of stackoverflow and stackexchange
  [#323](https://github.com/seedcase-project/decisions/pull/323) by
  [`@signekb`](https://github.com/signekb)
  ([bccfe1e](https://github.com/seedcase-project/decisions/commit/bccfe1e1cc2bc2acb36df13b520f648ca6822770))
- Add missing user and repo name to `cliff.toml`
  [#326](https://github.com/seedcase-project/decisions/pull/326) by
  [`@signekb`](https://github.com/signekb)
  ([eb6dea3](https://github.com/seedcase-project/decisions/commit/eb6dea325cfe9d76f1169c0449983495df551130))

### ❤️ New contributors

- `@dependabot[bot]` started making automated contributions

## [0.12.0](https://github.com/seedcase-project/decisions/compare/0.11.0..0.12.0) - 2026-06-08

### ✨ Features

- Decision on using Cocogitto for checking commit messages
  [#276](https://github.com/seedcase-project/decisions/pull/276) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([aecb301](https://github.com/seedcase-project/decisions/commit/aecb30163f3b98715aa1acd17aa74003636a5a4d))

## [0.11.0](https://github.com/seedcase-project/decisions/compare/0.10.0..0.11.0) - 2026-06-08

### ✨ Features

- Decision post on why to use Cocogitto
  [#277](https://github.com/seedcase-project/decisions/pull/277) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([b89889c](https://github.com/seedcase-project/decisions/commit/b89889c4a81bde8343f3efb8bc36bd3203a5bdd3))

## [0.10.0](https://github.com/seedcase-project/decisions/compare/0.9.0..0.10.0) - 2026-06-08

### ✨ Features

- Decision post on why to use git-cliff for changelogs
  [#273](https://github.com/seedcase-project/decisions/pull/273) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([0b8afb9](https://github.com/seedcase-project/decisions/commit/0b8afb9fc54e35e0f7dc519dcf6184ac32149939))

## [0.9.0](https://github.com/seedcase-project/decisions/compare/0.8.1..0.9.0) - 2026-06-02

### ✨ Features

- Refine instructions in decision-making template
  [#283](https://github.com/seedcase-project/decisions/pull/283) by
  [`@joelostblom`](https://github.com/joelostblom)
  ([4652998](https://github.com/seedcase-project/decisions/commit/465299802e8ade5b81553c0ae2b1aaa482d1e6e5))

### 👩‍💻 Miscellaneous

- Updated files from template
  [#257](https://github.com/seedcase-project/decisions/pull/257) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([245e04a](https://github.com/seedcase-project/decisions/commit/245e04a5e7cdde2587b59573be1126e354230bb7))
- Update Seedcase Quarto theme
  [#274](https://github.com/seedcase-project/decisions/pull/274) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([531f3d2](https://github.com/seedcase-project/decisions/commit/531f3d249dc51f9068c87a1769e4029e118b503e))

### ❤️ New contributors

- [`@joelostblom`](https://github.com/joelostblom) made their first contribution
  in [#283](https://github.com/seedcase-project/decisions/pull/283)

## [0.8.1](https://github.com/seedcase-project/decisions/compare/0.8.0..0.8.1) - 2026-03-03

### 🐛 Fixes

- Correct broken/redirected links
  [#256](https://github.com/seedcase-project/decisions/pull/256) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([8bf665a](https://github.com/seedcase-project/decisions/commit/8bf665a96ba12ef923a5befdde13cde191899b74))

## [0.8.0](https://github.com/seedcase-project/decisions/compare/0.7.0..0.8.0) - 2026-02-20

### ✨ Features

- Post on why we will use rumdl
  [#253](https://github.com/seedcase-project/decisions/pull/253) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([1522f12](https://github.com/seedcase-project/decisions/commit/1522f12f797680901e5dccc40f6a8e59b3d57cdb))

### 👩‍💻 Miscellaneous

- Upgrade `seedcase-theme`
  [#247](https://github.com/seedcase-project/decisions/pull/247) by
  [`@signekb`](https://github.com/signekb)
  ([9c62c71](https://github.com/seedcase-project/decisions/commit/9c62c71ea56adf890f6e40a9d1f100fafd1dadd7))
- Add Markdown `rumdl` formatter
  [#252](https://github.com/seedcase-project/decisions/pull/252) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([e8c9c7e](https://github.com/seedcase-project/decisions/commit/e8c9c7ee771e0732a5a7b1f1f70e7fa4e05d8dcb))

## [0.7.0](https://github.com/seedcase-project/decisions/compare/0.6.0..0.7.0) - 2026-02-04

### ✨ Features

- Add Why Git LFS post
  [#244](https://github.com/seedcase-project/decisions/pull/244) by
  [`@martonvago`](https://github.com/martonvago)
  ([92b0afb](https://github.com/seedcase-project/decisions/commit/92b0afb010a5821f6cc5ab43cb6fcff967f585d0))

## [0.6.0](https://github.com/seedcase-project/decisions/compare/0.5.0..0.6.0) - 2026-02-04

### ✨ Features

- Post on using Diataxis for docs
  [#241](https://github.com/seedcase-project/decisions/pull/241) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([d395b85](https://github.com/seedcase-project/decisions/commit/d395b85b4999e1dbeb58eddaf7ed9ea2dd779a02))

## [0.5.0](https://github.com/seedcase-project/decisions/compare/0.4.0..0.5.0) - 2026-02-03

### ✨ Features

- Post on iterative and incremental with Kanban development
  [#239](https://github.com/seedcase-project/decisions/pull/239) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([b5b1a18](https://github.com/seedcase-project/decisions/commit/b5b1a18ad87a2a7b076c251e4a9df7e3572801fc))

## [0.4.0](https://github.com/seedcase-project/decisions/compare/0.3.2..0.4.0) - 2026-01-28

### ✨ Features

- Post on using Cyclopts for CLIs in Python
  [#237](https://github.com/seedcase-project/decisions/pull/237) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([ce1db2a](https://github.com/seedcase-project/decisions/commit/ce1db2a2296684cf7d56438ebdae95d3388f1d57))

### 👩‍💻 Miscellaneous

- Upgrade `seedcase-theme`
  [#245](https://github.com/seedcase-project/decisions/pull/245) by
  [`@signekb`](https://github.com/signekb)
  ([a729dcb](https://github.com/seedcase-project/decisions/commit/a729dcb45a8609ebdc511508882ab155a4be5c8b))

## [0.3.2](https://github.com/seedcase-project/decisions/compare/0.3.1..0.3.2) - 2026-01-27

### ♻️ Refactor

- Standardise and simplify some of the categories
  [#242](https://github.com/seedcase-project/decisions/pull/242) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([0108515](https://github.com/seedcase-project/decisions/commit/0108515639e21f641a835ad3c40ec296ab172a8c))

### 👩‍💻 Miscellaneous

- These logos got missed when updating
  [#240](https://github.com/seedcase-project/decisions/pull/240) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([10abee9](https://github.com/seedcase-project/decisions/commit/10abee9c30a691dc93b07ff5974260589c55503b))

## [0.3.1](https://github.com/seedcase-project/decisions/compare/0.3.0..0.3.1) - 2026-01-26

### ♻️ Refactor

- Update theme and files from template
  [#238](https://github.com/seedcase-project/decisions/pull/238) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([7e0274b](https://github.com/seedcase-project/decisions/commit/7e0274b6a7e213e8797794944c54649e608c6a1e))

## [0.3.0](https://github.com/seedcase-project/decisions/compare/0.2.0..0.3.0) - 2025-12-18

### ✨ Features

- Add why mypy post
  [#227](https://github.com/seedcase-project/decisions/pull/227) by
  [`@martonvago`](https://github.com/martonvago)
  ([a6c8060](https://github.com/seedcase-project/decisions/commit/a6c80607b14d540b0d656ecf72cb4bed34972d57))

### 📝 Documentation

- Add the DOI from Zenodo
  [#217](https://github.com/seedcase-project/decisions/pull/217) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([4f826b4](https://github.com/seedcase-project/decisions/commit/4f826b4912c8961073a8ecacd4e078648e274bfa))

### 👷 CI/CD

- Add Dependabot workflow
  [#209](https://github.com/seedcase-project/decisions/pull/209) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([2ba4c45](https://github.com/seedcase-project/decisions/commit/2ba4c454ebf14c6eddcf35f683a6b6d3422c89cc))
- Improve workflow security (template updates)
  [#202](https://github.com/seedcase-project/decisions/pull/202) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([94df10f](https://github.com/seedcase-project/decisions/commit/94df10f78c665875d5df60db40a66a4f4c89281a))

### 👩‍💻 Miscellaneous

- Update justfile from template
  [#212](https://github.com/seedcase-project/decisions/pull/212) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([cac950f](https://github.com/seedcase-project/decisions/commit/cac950fcac35b3d5545d861538e1acb0b0e19ae3))
- Run `just run-all`
  [#228](https://github.com/seedcase-project/decisions/pull/228) by
  [`@martonvago`](https://github.com/martonvago)
  ([f2fcbd5](https://github.com/seedcase-project/decisions/commit/f2fcbd5f1459f3c74d014a39ddb4069b6a0b48df))

## [0.2.0] - 2025-09-12

### ✨ Features

- Set up basic Quarto and Git repo standard files by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([31c4669](https://github.com/seedcase-project/decisions/commit/31c466900ee449e250687ba0d4b857fc636aea5f))
- Add category listing to page by [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([031d578](https://github.com/seedcase-project/decisions/commit/031d578b45c3cfc9ecfc53174d143694c48af7c9))
- Add reference section by [`@signekb`](https://github.com/signekb)
  ([907db88](https://github.com/seedcase-project/decisions/commit/907db8893f4d51a29d226f573aba5c0f65d2168e))
- Added a category listing to the page
  [#74](https://github.com/seedcase-project/decisions/pull/74) by
  [`@signekb`](https://github.com/signekb)
  ([a2d9c1d](https://github.com/seedcase-project/decisions/commit/a2d9c1d1f04098a7470b7bc9abe2c5d404586094))
- Add alt labels to navbar logos by [`@signekb`](https://github.com/signekb)
  ([9c98d1c](https://github.com/seedcase-project/decisions/commit/9c98d1caea7f932a6b587778f02f8cf11d3b36ee))
- Decision on why we use or recommend CC0 for data
  [#194](https://github.com/seedcase-project/decisions/pull/194) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([45a4a22](https://github.com/seedcase-project/decisions/commit/45a4a22452ec663f9e2c2327f63a80c0e61d1596))
- Post on why we use Copier
  [#195](https://github.com/seedcase-project/decisions/pull/195) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([6a6581f](https://github.com/seedcase-project/decisions/commit/6a6581febfefc2231597716141f736b0528a848c))

### 🐛 Fixes

- Fixed URLs that we're resolving by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([3be1ed4](https://github.com/seedcase-project/decisions/commit/3be1ed46018b9b1498ff119ae88f4c805b301f14))
- Fix links to internal and external files/content by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([50af2ee](https://github.com/seedcase-project/decisions/commit/50af2eee5fe29996ee976b6eb484eddb562f5b67))
- The yaml header was incomplete. by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([1ef8bdb](https://github.com/seedcase-project/decisions/commit/1ef8bdbd212acaaf68eee325dc194443665d5124))
- Fixed link to internal decision post by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([8da76ba](https://github.com/seedcase-project/decisions/commit/8da76bacbd449cd3bae2615343876514347b9c0f))
- Remove unnecessary style code for column widths by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([e2058f5](https://github.com/seedcase-project/decisions/commit/e2058f554d1019c4e23b10ce018b567a43044e17))
- Apply suggestions from code review by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([91b776b](https://github.com/seedcase-project/decisions/commit/91b776b9667c759b8f2e8a25e6ff7871e8d28fb4))
- Add missing "are" by [`@signekb`](https://github.com/signekb)
  ([25a36f4](https://github.com/seedcase-project/decisions/commit/25a36f4b937a09fb2e920fd24decf3f17979056d))
- Change headers to sentence case by [`@signekb`](https://github.com/signekb)
  ([6c8239c](https://github.com/seedcase-project/decisions/commit/6c8239ce050edfc8316eea2a4c1f394e9b33d453))
- Remove duplicate categories from yaml header by
  [`@signekb`](https://github.com/signekb)
  ([551c1e9](https://github.com/seedcase-project/decisions/commit/551c1e9d72301cb99e86030199dbd678eb92ec98))
- Remove old favicons by [`@signekb`](https://github.com/signekb)
  ([bcc2aa0](https://github.com/seedcase-project/decisions/commit/bcc2aa031b59586231483f722ba9e67d2f84f906))
- Add "Decisions" to logo alt by [`@signekb`](https://github.com/signekb)
  ([94af378](https://github.com/seedcase-project/decisions/commit/94af378536b4a826a34e3a845c2b21b6e261dfb4))
- Elaborate on alt labels by [`@signekb`](https://github.com/signekb)
  ([d287444](https://github.com/seedcase-project/decisions/commit/d2874449f03eaef4afdaeb316e46a59a38463735))
- Shorten alt texts by [`@signekb`](https://github.com/signekb)
  ([869f86d](https://github.com/seedcase-project/decisions/commit/869f86d979a71dd319c800f1e08c81a3fafc108d))
- Remove whitespace by [`@signekb`](https://github.com/signekb)
  ([241cbbd](https://github.com/seedcase-project/decisions/commit/241cbbd97cc5f65a3d1b6432c6a42f9bf8900b03))
- Change contents path so fit new folder structure by
  [`@signekb`](https://github.com/signekb)
  ([1561db9](https://github.com/seedcase-project/decisions/commit/1561db921f94bf955f2f02ea25039492cef8a4fc))
- Update link to values and principles by
  [`@signekb`](https://github.com/signekb)
  ([e2a5c57](https://github.com/seedcase-project/decisions/commit/e2a5c576f9ac6cfbe337580d439e2519933fe0e1))
- There was a double quote accidentally
  [#128](https://github.com/seedcase-project/decisions/pull/128) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([190afb9](https://github.com/seedcase-project/decisions/commit/190afb919a84f017b9921ba4960ab1b0157a595b))
- Wrong single quote character was used
  [#213](https://github.com/seedcase-project/decisions/pull/213) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([56d9c5d](https://github.com/seedcase-project/decisions/commit/56d9c5dfcdb314f967498ca17f835f60a273fd86))

### ♻️ Refactor

- Reduce number of categories, remove redundant/unecessary ones by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([d90c32c](https://github.com/seedcase-project/decisions/commit/d90c32c96c82fb80a5621d7a8cf41dbd8fe1de20))
- Decide on uv, not Poetry
  [#170](https://github.com/seedcase-project/decisions/pull/170) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([93c02d0](https://github.com/seedcase-project/decisions/commit/93c02d0a512b6853a0698712d5ab1707de2395bf))

### 📝 Documentation

- *(review)* Apply suggestions from code review by
  [`@signekb`](https://github.com/signekb)
  ([96bc75f](https://github.com/seedcase-project/decisions/commit/96bc75ff624d0f29e5490702862d68b17186ef3a))
- Split the standardisation documentation by
  [`@K-Beicher`](https://github.com/K-Beicher)
  ([e859b2e](https://github.com/seedcase-project/decisions/commit/e859b2ef488af0cb3912a804984f782ce502d148))
- Update with comments from SKB by [`@K-Beicher`](https://github.com/K-Beicher)
  ([bd0dcea](https://github.com/seedcase-project/decisions/commit/bd0dcea9ceaec385b17d3ad3e427e2469dcddb66))
- Edits to "why GitHub Projects" by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([15a2a50](https://github.com/seedcase-project/decisions/commit/15a2a508af5f769ba3ed60232d709e8b7ff2cfd9))
- Edits and formatting fixes to the "why standard shortcuts" file by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([671e64a](https://github.com/seedcase-project/decisions/commit/671e64aabf0c513975a95ef80ba109cffb0f88e3))
- Start of post on decision to use code/text-based tools by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([a9b1d89](https://github.com/seedcase-project/decisions/commit/a9b1d89ebcf8327d72ee77ff43b453741f9e00c0))
- License decision should realistically be in community, not design by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([256ca28](https://github.com/seedcase-project/decisions/commit/256ca28d7f05b9334b768341fcc90719bf426e45))
- Small edits to why MIT by [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([027b80e](https://github.com/seedcase-project/decisions/commit/027b80ed6ad723636e117a1492fa9aadc0649832))
- Moved to community decisions by [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([dac43f8](https://github.com/seedcase-project/decisions/commit/dac43f8e0fe3a1b888958b807dfaf98174dd88af))
- Add template decision post to community folder by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([69d69b2](https://github.com/seedcase-project/decisions/commit/69d69b229323a8515486724ae410430e50058840))
- Edits to the decision post for linters/formatters by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([4000eab](https://github.com/seedcase-project/decisions/commit/4000eabdab221722e11f7f915816d28a3195ca89))
- Reviewed and edited post by [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([ca6b60a](https://github.com/seedcase-project/decisions/commit/ca6b60a09d888d7a65805eff5e253503a084e5a0))
- Mostly just reformats, small edits, and making it more consistent with other
  posts by [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([c2fbdbb](https://github.com/seedcase-project/decisions/commit/c2fbdbb588293471e3527471b952603230ac5521))
- Add instructions on how to create a decision post by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([b05b61d](https://github.com/seedcase-project/decisions/commit/b05b61d7247560fc647d6e1795ba472fde605c90))
- Add some notes for this draft post by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([62b8540](https://github.com/seedcase-project/decisions/commit/62b8540b0fc41623ee7fdc5de8ad6ea0bf620a2c))
- Start file to write about decision to use GitHub by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([66c4a17](https://github.com/seedcase-project/decisions/commit/66c4a1776b4cd896158fb2ac9d175b170a253080))
- Add description and link to guiding principles by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([fcbea42](https://github.com/seedcase-project/decisions/commit/fcbea4204f234aa82f534a8385a31cdd884c1d55))
- Switch to draft, we might not use REST APIs by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([b8062f0](https://github.com/seedcase-project/decisions/commit/b8062f0670db5e17d9a89a38eefef294e24ec301))
- Decision post on why to use poetry by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([361af06](https://github.com/seedcase-project/decisions/commit/361af0694b0ddbc5a0647334b45950f4e5498dcb))
- Edits based on the comments and feedback in the PR review by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([f21bad9](https://github.com/seedcase-project/decisions/commit/f21bad977aa7573400083c565654ff823c771509))
- Moved this post from the design docs. by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([d74baf2](https://github.com/seedcase-project/decisions/commit/d74baf2cfc2a5611ffff1c4d7b3d20421c152f25))
- Small edits by [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([5cc5f6c](https://github.com/seedcase-project/decisions/commit/5cc5f6cd22c74ca2488163a17dfd3bae3f4a898e))
- Complete update to why REST by [`@K-Beicher`](https://github.com/K-Beicher)
  ([ed35d56](https://github.com/seedcase-project/decisions/commit/ed35d567bba6539970cd61f8facddfa905701633))
- Format sub-set of files to comply with template-1 by
  [`@K-Beicher`](https://github.com/K-Beicher)
  ([c39ba00](https://github.com/seedcase-project/decisions/commit/c39ba00a85eba2d1fe682baca6ace2e38d85f0cd))
- Apply suggestions from review by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([0b9d209](https://github.com/seedcase-project/decisions/commit/0b9d2096c8a508c7e23d6181170fd8d45c4721ef))
- Format sub-set of files to comply with template-3 by
  [`@K-Beicher`](https://github.com/K-Beicher)
  ([b059afd](https://github.com/seedcase-project/decisions/commit/b059afd806cdf9ccc57e47f03680944d345781f9))
- Update why text based with template by
  [`@K-Beicher`](https://github.com/K-Beicher)
  ([fce7d7c](https://github.com/seedcase-project/decisions/commit/fce7d7cfdbfc2764bea273d1c3556ce48ebe0a7d))
- Format sub-set of files to comply with template-2 by
  [`@K-Beicher`](https://github.com/K-Beicher)
  ([8ff0507](https://github.com/seedcase-project/decisions/commit/8ff0507489d62939ab46531282534193534dd332))
- Update github projects with coding for benefits-drawbacks by
  [`@K-Beicher`](https://github.com/K-Beicher)
  ([846352e](https://github.com/seedcase-project/decisions/commit/846352e04f3862cf1ddc23407ecddd5eebc1f8fa))
- Complete update to why discord by [`@K-Beicher`](https://github.com/K-Beicher)
  ([a9412c0](https://github.com/seedcase-project/decisions/commit/a9412c0996b1a60bd1dbd4892481387d8b9f0cac))
- Apply suggestions from review by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([b20083c](https://github.com/seedcase-project/decisions/commit/b20083c284a10a311c56709ad0266db4d7d42ca7))
- Complete update to why django by [`@K-Beicher`](https://github.com/K-Beicher)
  ([d04406f](https://github.com/seedcase-project/decisions/commit/d04406ff02506e70641c60def07e3c360bf1abaa))
- Update with options code by [`@K-Beicher`](https://github.com/K-Beicher)
  ([0a9de39](https://github.com/seedcase-project/decisions/commit/0a9de39487db5e94207bdfbbd9d9979bf2cb95b1))
- Removed the ruby on rails, since it uses Ruby not Python by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([08554dc](https://github.com/seedcase-project/decisions/commit/08554dc4b6d3db70c388457f833797a980cc1e5b))
- Format sub-set of files to comply with template-3 by
  [`@K-Beicher`](https://github.com/K-Beicher)
  ([d1efe54](https://github.com/seedcase-project/decisions/commit/d1efe54684967eccab3135face9d07a363cea147))
- Include comparison of languages in Why Python post by
  [`@martonvago`](https://github.com/martonvago)
  ([52f1179](https://github.com/seedcase-project/decisions/commit/52f117957891834867874da17d8b83df1d3a0278))
- Apply suggestions from review by
  [`@martonvago`](https://github.com/martonvago)
  ([5c3845b](https://github.com/seedcase-project/decisions/commit/5c3845b49791b64f995043d791c717709d2f8234))
- Complete update to why quarto by [`@K-Beicher`](https://github.com/K-Beicher)
  ([9f86979](https://github.com/seedcase-project/decisions/commit/9f8697913a8532c4cde9ada70e361b793ba3069d))
- Add options for other website generators by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([b5aa2ec](https://github.com/seedcase-project/decisions/commit/b5aa2eca1972f8bfea77abd8aaa6551f962a2f47))
- Apply suggestions from review by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([36c18d7](https://github.com/seedcase-project/decisions/commit/36c18d70a3f739c2bb54e45313635720e6cdd097))
- Updates to quarto decision post based on comments from @signekb by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([cc759ef](https://github.com/seedcase-project/decisions/commit/cc759efaf8c14703a5f070380e615a96704392c6))
- Apply suggestions from review by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([49fcd64](https://github.com/seedcase-project/decisions/commit/49fcd645370df998175304ef03bfa20192da4bd4))
- Init why conventional commits decision post by
  [`@signekb`](https://github.com/signekb)
  ([b18e180](https://github.com/seedcase-project/decisions/commit/b18e180a2e474833fc3ef744ea49ca54bfb9efd8))
- Remove the Angular convention (too similar to Conventional) and rework post
  based on feedback by [`@signekb`](https://github.com/signekb)
  ([b4b20b0](https://github.com/seedcase-project/decisions/commit/b4b20b0ba73848cd99df6d863151ff2340e94d52))
- Fix typo - "Gitmojis" -> "Gitmoji" by [`@signekb`](https://github.com/signekb)
  ([8f5ec23](https://github.com/seedcase-project/decisions/commit/8f5ec23497ccd545784752e54f08cb9ee6f91ffc))
- Add categories to yaml header by [`@signekb`](https://github.com/signekb)
  ([daa5eb7](https://github.com/seedcase-project/decisions/commit/daa5eb7db61e86effe5e2bdf4dd7c39986dc8733))
- Add decision post on using SemVer by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([b8106dc](https://github.com/seedcase-project/decisions/commit/b8106dc4445785cfe1336eb2f08f661323a78969))
- Small typo, should be every 6 months, not 4 by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([b99f92b](https://github.com/seedcase-project/decisions/commit/b99f92b7b6d3aa1b620f281e731e5c3f1c91a0cc))
- Apply suggestions from review by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([fe61b23](https://github.com/seedcase-project/decisions/commit/fe61b239e5f86004a374d08b97ea43b9cb5396f2))
- Add examples of tools that work with SemVer by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([bcf825e](https://github.com/seedcase-project/decisions/commit/bcf825e8f6f61524d0cd2bc13d2347de05375a31))
- Make references to Seedcase software/products more uniform by
  [`@martonvago`](https://github.com/martonvago)
  ([0affa62](https://github.com/seedcase-project/decisions/commit/0affa626042c0195040910541423270a4f8b1ddd))
- Large update to why REST
  [#46](https://github.com/seedcase-project/decisions/pull/46) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([26016ec](https://github.com/seedcase-project/decisions/commit/26016ece3afcd58c9e3ee1418a20f10f7e7a6498))
- Add more context and comparison of frameworks to Why Django post by
  [`@martonvago`](https://github.com/martonvago)
  ([fb8b28c](https://github.com/seedcase-project/decisions/commit/fb8b28c478a23430522023c2efd4c65dd76c1e30))
- Format qmd file by [`@martonvago`](https://github.com/martonvago)
  ([888e720](https://github.com/seedcase-project/decisions/commit/888e7205137e1aa3a3a0a31661b19986681ddc3f))
- Very minor edits by [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([d281ae0](https://github.com/seedcase-project/decisions/commit/d281ae0b8e1800e3f9c03a2428e935e7c77ad406))
- Add why conventioanl branches post by [`@signekb`](https://github.com/signekb)
  ([a301fbd](https://github.com/seedcase-project/decisions/commit/a301fbd5907fcf40b1b44a98a055729d1f0f1333))
- Add references by [`@signekb`](https://github.com/signekb)
  ([8acde7e](https://github.com/seedcase-project/decisions/commit/8acde7ee09435d76b5d04b372196f01c46120d38))
- Add date to the yaml by [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([42e08e3](https://github.com/seedcase-project/decisions/commit/42e08e320dfc52a37b31a6d3520c01248dc097b9))
- Apply suggestions from review by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([6c5421d](https://github.com/seedcase-project/decisions/commit/6c5421d5bf0d50a334e3f6104dcbbfbcb02d381a))
- Write a why accessibility document by
  [`@K-Beicher`](https://github.com/K-Beicher)
  ([eac1e93](https://github.com/seedcase-project/decisions/commit/eac1e9365628b8ed66b27788ae5e9530767a958d))
- Update to a few more complex suggestions by
  [`@K-Beicher`](https://github.com/K-Beicher)
  ([9a2ce1d](https://github.com/seedcase-project/decisions/commit/9a2ce1d68390fd2f6af2967f4b96da646c61e9d2))
- Reformat to use benefits and drawbacks structure by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([948680d](https://github.com/seedcase-project/decisions/commit/948680d785145be3916410503a1bef9a8fac6a8f))
- Decision post on why to use the Frictionless Data standard
  [#100](https://github.com/seedcase-project/decisions/pull/100) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([c3ae7ca](https://github.com/seedcase-project/decisions/commit/c3ae7ca7344cbbbfb3ba3cf700abe67cac599a40))
- Decision post on why to use pytest
  [#102](https://github.com/seedcase-project/decisions/pull/102) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([b66138c](https://github.com/seedcase-project/decisions/commit/b66138c760cabe88ec0c7a974d7841f5e41477a1))
- Update README with correct instructions by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([79bc4b8](https://github.com/seedcase-project/decisions/commit/79bc4b8e014baf4b361647f6ffcc44d0f86f6238))
- Small clarification on text by [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([cddb529](https://github.com/seedcase-project/decisions/commit/cddb529b59214c64074ed1d0fe4f81ed1edcc4d2))
- Add why post for using quartodocs
  [#121](https://github.com/seedcase-project/decisions/pull/121) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([7daeae1](https://github.com/seedcase-project/decisions/commit/7daeae18887406e6ca2bea2c1521b6d154c1bdae))
- Decision post on using commitizen for commit linting
  [#127](https://github.com/seedcase-project/decisions/pull/127) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([d9cfc25](https://github.com/seedcase-project/decisions/commit/d9cfc25195f0f2621b01673700a9e91e90919de2))
- Why FigJam decision post
  [#120](https://github.com/seedcase-project/decisions/pull/120) by
  [`@K-Beicher`](https://github.com/K-Beicher)
  ([f525f7b](https://github.com/seedcase-project/decisions/commit/f525f7b24d59a54b792743b98908dbed48d27ae0))
- Decision post for versioning with Commitizen
  [#136](https://github.com/seedcase-project/decisions/pull/136) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([b35dc04](https://github.com/seedcase-project/decisions/commit/b35dc04d26e2107791b783bef7409f22275bae4a))
- Using `jsonschema` tool for checking metadata
  [#134](https://github.com/seedcase-project/decisions/pull/134) by
  [`@martonvago`](https://github.com/martonvago)
  ([576cfc0](https://github.com/seedcase-project/decisions/commit/576cfc032da79a6be8f3bd732baad90e1a36cbac))
- Why Pandera for data verification/validation
  [#135](https://github.com/seedcase-project/decisions/pull/135) by
  [`@martonvago`](https://github.com/martonvago)
  ([a7b0945](https://github.com/seedcase-project/decisions/commit/a7b09452000e17d675338fa88a4ece06d37ae89c))
- Add Why Commitizen for changelog generation post
  [#142](https://github.com/seedcase-project/decisions/pull/142) by
  [`@signekb`](https://github.com/signekb)
  ([48eed59](https://github.com/seedcase-project/decisions/commit/48eed5900ed664b58dbef60df35e1f60d3200ae1))
- Decision post on a data processing tool
  [#145](https://github.com/seedcase-project/decisions/pull/145) by
  [`@K-Beicher`](https://github.com/K-Beicher)
  ([6f087fd](https://github.com/seedcase-project/decisions/commit/6f087fd2a826a2dc541874cdc35941469b122dde))
- Add pages for current and previous decisions
  [#159](https://github.com/seedcase-project/decisions/pull/159) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([fce1dd1](https://github.com/seedcase-project/decisions/commit/fce1dd16b2bc25db230c6f685849d1c459832422))
- Update MIT license post
  [#164](https://github.com/seedcase-project/decisions/pull/164) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([19793eb](https://github.com/seedcase-project/decisions/commit/19793eb40ad5e24621a6efe8fe03cb4d43b3f3fb))
- Add why Markdown post
  [#167](https://github.com/seedcase-project/decisions/pull/167) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([e2f0dcf](https://github.com/seedcase-project/decisions/commit/e2f0dcff350af67b5e7fb63935a9387f0dfde40c))
- Decision post on using Parquet
  [#168](https://github.com/seedcase-project/decisions/pull/168) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([7edf281](https://github.com/seedcase-project/decisions/commit/7edf2817d5bd0d4a115dc1e1a4ca2c8ee8355fe0))
- Fix typos [#173](https://github.com/seedcase-project/decisions/pull/173) by
  [`@signekb`](https://github.com/signekb)
  ([cbfbbe4](https://github.com/seedcase-project/decisions/commit/cbfbbe44121abede6d3d9ff18f9f7da831d9621d))
- Convert LICENSE to Markdown version
  [#203](https://github.com/seedcase-project/decisions/pull/203) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([c468036](https://github.com/seedcase-project/decisions/commit/c468036ac215c116e4e1a39a05f501c7e38ae99d))
- Add Code of Conduct from template
  [#206](https://github.com/seedcase-project/decisions/pull/206) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([f337156](https://github.com/seedcase-project/decisions/commit/f337156e0dacbee125e5976387280c8380026c87))
- Add CONTRIBUTING page
  [#208](https://github.com/seedcase-project/decisions/pull/208) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([7e4cea6](https://github.com/seedcase-project/decisions/commit/7e4cea6a0f9add1ddcae940905ea03513c30d902))
- Update README based on template
  [#211](https://github.com/seedcase-project/decisions/pull/211) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([062c311](https://github.com/seedcase-project/decisions/commit/062c311aa6e4e5cfbb6fbe5e561641e0498cbb60))

### 💄 Styling

- Use a consistent format for the titles of the posts by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([7b59087](https://github.com/seedcase-project/decisions/commit/7b590877e20393d77a179eed218249cc031a967e))
- Renamed to match other files by [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([4c7eb76](https://github.com/seedcase-project/decisions/commit/4c7eb769dce85c77fb3f5be1ce3b523c96077851))
- Style changes to how posts are displayed, using a grid, box style by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([52e0bf9](https://github.com/seedcase-project/decisions/commit/52e0bf9ce293fe0b7950f4f64b5ac6dbfdb11193))
- Remove sidebar because it wasn't needed and didn't look good by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([e6b5969](https://github.com/seedcase-project/decisions/commit/e6b59698d6f24fcabbefa9d8883713ed388b0081))
- Use columns instead of linear lists for comparing benefits and drawback (in
  template) by [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([c28cdd6](https://github.com/seedcase-project/decisions/commit/c28cdd6383e0beb776b664a129089b042285a5e7))
- Format post by [`@signekb`](https://github.com/signekb)
  ([89639fc](https://github.com/seedcase-project/decisions/commit/89639fc1a54af79949002fd0556a31ccc23de1b4))
- Sentence case headers in all decision posts by
  [`@signekb`](https://github.com/signekb)
  ([ecc9646](https://github.com/seedcase-project/decisions/commit/ecc96463469272d6785cd2e400c262e597ce1ec4))
- Format post by [`@signekb`](https://github.com/signekb)
  ([eac6df8](https://github.com/seedcase-project/decisions/commit/eac6df8839cf99b7c239cbd9622561f2874e178f))
- Only reformat this file by [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([2695ca9](https://github.com/seedcase-project/decisions/commit/2695ca9ec563b0913191d092c7a3054bc6246b62))
- Add logo to navbar by [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([1dee7ea](https://github.com/seedcase-project/decisions/commit/1dee7ea1efd7dd32f9875f9859ab733068a6d77c))
- Make a landing page section, with illustration
  [#126](https://github.com/seedcase-project/decisions/pull/126) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([0ba6102](https://github.com/seedcase-project/decisions/commit/0ba6102cb9b5032f73a26cc638b6abe46d9e22af))
- Update Quarto extension theme
  [#214](https://github.com/seedcase-project/decisions/pull/214) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([5be8382](https://github.com/seedcase-project/decisions/commit/5be83824bcd3f87ddf4eca588172019f1429f9f4))

### 👷 CI/CD

- Set connection to Netlify to host the website by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([6081c25](https://github.com/seedcase-project/decisions/commit/6081c253d6b54e10e5ea349aa7b1fdac1fcd84eb))
- No longer need these by [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([e5037d2](https://github.com/seedcase-project/decisions/commit/e5037d2690d821d35edfd8cc9a63c8bf01010bb7))

### 👩‍💻 Miscellaneous

- *(sync)* Synced local '.github/pull_request_template.md' with remote
  '.github/pull_request_template.md' by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([28c96e1](https://github.com/seedcase-project/decisions/commit/28c96e151c78b451d067788aec0eedb2ce1b2cd6))

- *(sync)* Synced local '.vscode/settings.json' with remote
  '.vscode/settings.json' by [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([707fd9c](https://github.com/seedcase-project/decisions/commit/707fd9c5943bd6959d3a011f877082100b8daa6b))

- *(sync)* Synced file(s) with seedcase-project/.github
  [#103](https://github.com/seedcase-project/decisions/pull/103) by
  [`@signekb`](https://github.com/signekb)
  ([6ce4063](https://github.com/seedcase-project/decisions/commit/6ce406395b58f41907029c7fc9dcd26812e6d433))

- *(sync)* Synced local '.vscode/extensions.json' with remote
  '.vscode/extensions.json' by [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([ec683b1](https://github.com/seedcase-project/decisions/commit/ec683b1664c4844320215f902c5904b50a01da48))

- *(sync)* Synced local '.gitignore' with remote '.gitignore' by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([2bf3c5e](https://github.com/seedcase-project/decisions/commit/2bf3c5ee4beae447e4f7c25e3f41eb613ef0e03a))

- *(sync)* Synced local '.vscode/settings.json' with remote
  '.vscode/settings.json' by [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([99ef276](https://github.com/seedcase-project/decisions/commit/99ef2767e38624025a53e28cc73a8f9835c2085e))

- *(sync)* Synced local '.vscode/extensions.json' with remote
  '.vscode/extensions.json' by [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([9eec9d9](https://github.com/seedcase-project/decisions/commit/9eec9d90e9f37e269904ceeb5effbb165e769005))

- *(sync)* Synced local '.editorconfig' with remote '.editorconfig' by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([95d903e](https://github.com/seedcase-project/decisions/commit/95d903e10a894f9226c5c2d3cc14cfbead6548d6))

- *(sync)* Synced local '.github/pull_request_template.md' with remote
  '.github/pull_request_template.md' by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([e6317be](https://github.com/seedcase-project/decisions/commit/e6317beec2f14db92e6593b9b64dcd97412e84a9))

- *(sync)* Synced local '.vscode/' with remote '.vscode/' by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([5080494](https://github.com/seedcase-project/decisions/commit/50804945268dfda9d0cf63af5e2d3154351d5554))

- *(sync)* Synced local '.github/workflows/' with remote '.github/workflows/' by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([ad73149](https://github.com/seedcase-project/decisions/commit/ad73149598deb65cb6d526fc675557849a9c1a98))

- *(sync)* Synced local '\_extensions/seedcase-project/seedcase-theme/' with
  remote '\_extensions/seedcase-theme/' by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([5e7bbb6](https://github.com/seedcase-project/decisions/commit/5e7bbb6113f54633aefbc13e813ac8c672aba70b))

- *(sync)* Synced local '\_extensions/seedcase-project/seedcase-theme/' with
  remote '\_extensions/seedcase-theme/' by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([a795886](https://github.com/seedcase-project/decisions/commit/a79588688fa64982028ea9cafee606b99817d78b))

- *(sync)* Created local '404.qmd' from remote '404.qmd' by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([df9688e](https://github.com/seedcase-project/decisions/commit/df9688e7e8b31d05272ac1cad864fd0896da9b3b))

- *(sync)* Synced local '\_extensions/seedcase-project/seedcase-theme/' with
  remote '\_extensions/seedcase-theme/' by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([afa919f](https://github.com/seedcase-project/decisions/commit/afa919fe326526c85427e9ad1e946dfdefef5138))

- *(sync)* Synced local '\_extensions/seedcase-project/seedcase-theme/' with
  remote '\_extensions/seedcase-theme/' by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([72ac77d](https://github.com/seedcase-project/decisions/commit/72ac77df839b49bc3b47d8c2623028aa6f11af9c))

- *(sync)* Synced local '\_extensions/seedcase-project/seedcase-theme/' with
  remote '\_extensions/seedcase-theme/' by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([9938c3f](https://github.com/seedcase-project/decisions/commit/9938c3fbc2b0019ee3bb399507b9dd8c90640d09))

- *(sync)* Synced local '\_extensions/seedcase-project/seedcase-theme/' with
  remote '\_extensions/seedcase-theme/' by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([c3c6d1a](https://github.com/seedcase-project/decisions/commit/c3c6d1a35f5224de64a452638fffa56a16a3e381))

- *(sync)* Created local '\_extensions/debruine/' from remote
  '\_extensions/debruine/' by [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([85479c6](https://github.com/seedcase-project/decisions/commit/85479c6bb027f8eb764459b21e893f562eed2866))

- *(sync)* Synced local '.github/workflows/' with remote '.github/workflows/' by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([c89259d](https://github.com/seedcase-project/decisions/commit/c89259d3de2660c0e3e0ee04e487d221ea5163ca))

- *(sync)* Synced local '\_extensions/seedcase-project/seedcase-theme/' with
  remote '\_extensions/seedcase-theme/' by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([6a06ad5](https://github.com/seedcase-project/decisions/commit/6a06ad596d59406fe588254fdde6ea0eef130edf))

- *(sync)* Synced local '.github/pull_request_template.md' with remote
  '.github/pull_request_template.md' by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([7003025](https://github.com/seedcase-project/decisions/commit/7003025de36dbb90886239b2faad2d8b55c22887))

- *(sync)* Synced local 'justfile' with remote 'justfile' by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([720eff8](https://github.com/seedcase-project/decisions/commit/720eff843f684e97e3ba578fbbb3f6b0e0c49583))

- *(sync)* Synced local '.vscode/' with remote '.vscode/' by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([3314add](https://github.com/seedcase-project/decisions/commit/3314add414c9fa34752d7d94f73f707a7eaf6653))

- *(sync)* Synced local '\_extensions/seedcase-project/seedcase-theme/' with
  remote '\_extensions/seedcase-theme/' by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([9462736](https://github.com/seedcase-project/decisions/commit/9462736f64b1d89b29fe0d97c70b70fe68c17808))

- *(sync)* Synced local '\_extensions/seedcase-project/seedcase-theme/' with
  remote '\_extensions/seedcase-theme/' by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([e054744](https://github.com/seedcase-project/decisions/commit/e054744b6e1dbf24d32ea1de16b715b6bab3574a))

- *(sync)* Synced local 'justfile' with remote 'justfile' by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([421b9ab](https://github.com/seedcase-project/decisions/commit/421b9ab1e2de365a0a47d5acabdbdb0428addad4))

- *(sync)* Synced local '.vscode/' with remote '.vscode/' by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([d6d75fb](https://github.com/seedcase-project/decisions/commit/d6d75fb82932b114e17a52483b0e4921cc711e0d))

- *(sync)* Synced local '.github/workflows/' with remote '.github/workflows/' by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([e65b541](https://github.com/seedcase-project/decisions/commit/e65b541c112c9cb0b135bcc7548e71215cd5da7a))

- *(sync)* Synced local '\_extensions/seedcase-project/seedcase-theme/' with
  remote '\_extensions/seedcase-theme/' by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([cead380](https://github.com/seedcase-project/decisions/commit/cead380045a92389e4a7316843ade33deeb412a5))

- *(sync)* Synced local '.vscode/' with remote '.vscode/' by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([b82631e](https://github.com/seedcase-project/decisions/commit/b82631e2e42c1132e50b7616a183be42282d3c2e))

- *(sync)* Synced local '\_extensions/seedcase-project/seedcase-theme/' with
  remote '\_extensions/seedcase-theme/' by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([ce11336](https://github.com/seedcase-project/decisions/commit/ce113363c34a1311e492e72be62edf95dc6a7f6f))

- *(sync)* Synced local '.editorconfig' with remote '.editorconfig' by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([edad71d](https://github.com/seedcase-project/decisions/commit/edad71dc8665d897dd5c8fa585b8f117441308fd))

- *(sync)* Created local '.typos.toml' from remote '.typos.toml' by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([3c4bab7](https://github.com/seedcase-project/decisions/commit/3c4bab7a5c3f52c984150ca7003fb088e8c43816))

- *(sync)* Synced local 'justfile' with remote 'justfile' by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([cd3825c](https://github.com/seedcase-project/decisions/commit/cd3825c79feaf66aa5087c6eb21df38a19ba699a))

- *(sync)* Synced local '.vscode/' with remote '.vscode/' by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([25a6063](https://github.com/seedcase-project/decisions/commit/25a60639f5bde4e8a0e862105516eda69a6a0220))

- *(sync)* Synced local '.github/workflows/' with remote '.github/workflows/' by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([9bdca6d](https://github.com/seedcase-project/decisions/commit/9bdca6d50eff6c8d6d9feded322de12510ec2513))

- *(sync)* Synced local '\_extensions/seedcase-project/seedcase-theme/' with
  remote '\_extensions/seedcase-theme/' by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([0b17d39](https://github.com/seedcase-project/decisions/commit/0b17d391549a0ad5e1b6f79e3a4b6eef8557efee))

- *(sync)* Synced local '\_extensions/seedcase-project/seedcase-theme/' with
  remote '\_extensions/seedcase-theme/' by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([03db940](https://github.com/seedcase-project/decisions/commit/03db940999430bd556c9dd432080b3a60339ae4b))

- *(sync)* Synced local '.typos.toml' with remote '.typos.toml' by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([f41beee](https://github.com/seedcase-project/decisions/commit/f41beee5fa0b3e87f0f4e98485420d7b2e959ef4))

- *(sync)* Synced file(s) with seedcase-project/seedcase-theme by
  `@sync-files-token[bot]`
  ([5bf86fd](https://github.com/seedcase-project/decisions/commit/5bf86fd7b1edbbbdfe859a6f81b8559d84769eb8))

- *(sync)* Synced file(s) with seedcase-project/seedcase-theme by
  `@sync-files-token[bot]`
  ([9cce8c8](https://github.com/seedcase-project/decisions/commit/9cce8c88645325b166b53e8eb14a337876961fcb))

- *(sync)* Synced file(s) with seedcase-project/seedcase-theme by
  `@sync-files-token[bot]`
  ([f1cd946](https://github.com/seedcase-project/decisions/commit/f1cd946ac531d0fcdbd50142689a18ec6d4046e5))

- *(sync)* Synced file(s) with seedcase-project/seedcase-theme by
  `@sync-files-token[bot]`
  ([60270ac](https://github.com/seedcase-project/decisions/commit/60270acc501c809d7989e292a5ece00e22c84304))

- *(sync)* Synced file(s) with seedcase-project/seedcase-theme by
  `@sync-files-token[bot]`
  ([633d9b3](https://github.com/seedcase-project/decisions/commit/633d9b3306d5e83a07ddd2d7559880bbb128169c))

- *(sync)* Synced file(s) with seedcase-project/seedcase-theme by
  `@sync-files-token[bot]`
  ([77c9122](https://github.com/seedcase-project/decisions/commit/77c9122368f8ede3e8171b0664d3677c6f80a8e5))

- *(sync)* Synced file(s) with seedcase-project/seedcase-theme by
  `@sync-files-token[bot]`
  ([77ae1fe](https://github.com/seedcase-project/decisions/commit/77ae1feb27da929b5747abcf99c965b455d55e49))

- *(sync)* Synced file(s) with seedcase-project/seedcase-theme by
  `@sync-files-token[bot]`
  ([f3b378d](https://github.com/seedcase-project/decisions/commit/f3b378d842e5951fe63dc4082d89bd85d8a446d1))

- Move all design docs out, remove non-design files by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([864b938](https://github.com/seedcase-project/decisions/commit/864b93893a1e01c69da551d44dccc46fde9309e4))

- Moved files from folders into own files by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([951558d](https://github.com/seedcase-project/decisions/commit/951558d629457a308245a7819e74dc2b2658e418))

- Add todo item to update these posts to match template by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([b0260d5](https://github.com/seedcase-project/decisions/commit/b0260d5a7d7614de096555525a912a9f9487c6f9))

- Set draft as true so it doesn't get rendered by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([31dea58](https://github.com/seedcase-project/decisions/commit/31dea587f379b62504a24f1bb9cab860f6b9e6b0))

- Add Quarto website config files by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([819ca5b](https://github.com/seedcase-project/decisions/commit/819ca5bb00cdf2e0c0f05b10dd654288c961b8fa))

- Rename file to match other files by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([dbcdfae](https://github.com/seedcase-project/decisions/commit/dbcdfae34f6f119dde9701febacbec86566ad870))

- Move REST API decision to hidden for now, we aren't using it yet. by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([3155ee1](https://github.com/seedcase-project/decisions/commit/3155ee100011239fa82dfc6ddb198f47b3fc6b09))

- Renamed files so they don't get rendered, only for those incomplete by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([5d28a52](https://github.com/seedcase-project/decisions/commit/5d28a52ca37b0054c82f81a6c40ba0309148c9fe))

- Add empty decision post on why we use Markdown by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([5f4ce61](https://github.com/seedcase-project/decisions/commit/5f4ce6116a1c57fc5858b845482d3152e19f7559))

- Move why docs out into folders by [`@K-Beicher`](https://github.com/K-Beicher)
  ([5032f33](https://github.com/seedcase-project/decisions/commit/5032f3303de936186f6c0a4a90436ea84af0c1c6))

- Move \_why docs into folders by [`@K-Beicher`](https://github.com/K-Beicher)
  ([03b2774](https://github.com/seedcase-project/decisions/commit/03b2774196d3ea6e3f362eeea438eb2721cd059b))

- Last of the why files by [`@K-Beicher`](https://github.com/K-Beicher)
  ([65f096e](https://github.com/seedcase-project/decisions/commit/65f096e0e3d8a661672b1a22dc98b5e42ee922f9))

- Footer is in the extensions now by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([9431c3e](https://github.com/seedcase-project/decisions/commit/9431c3e1a45562ece2781c41e4c0c757ee1f0035))

- Hide these posts since we don't actually use these tools completely by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([a3a6cdf](https://github.com/seedcase-project/decisions/commit/a3a6cdfb2ae19298e000b839d0b3ace44358b811))

- Add website visit counter (non-personal data)
  [#125](https://github.com/seedcase-project/decisions/pull/125) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([8286530](https://github.com/seedcase-project/decisions/commit/828653082e8fb612f409e3a1a1e10c1c4f1136e1))

- No longer need these files by [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([0e79e30](https://github.com/seedcase-project/decisions/commit/0e79e30c94ae78c4f135e02a6264a5434d8d3d66))

- Few things needing tidying up
  [#124](https://github.com/seedcase-project/decisions/pull/124) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([31d789c](https://github.com/seedcase-project/decisions/commit/31d789c8df9f7621b02137a8870c567353e89da4))

- Remove left over Quarto extensions
  [#160](https://github.com/seedcase-project/decisions/pull/160) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([bd4563f](https://github.com/seedcase-project/decisions/commit/bd4563f87e1c4cff8c9af2b407bad2098fc222cd))

- Minor improvements
  [#161](https://github.com/seedcase-project/decisions/pull/161) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([a166552](https://github.com/seedcase-project/decisions/commit/a1665526384c8c754d3bb2e2a7adf2ffc006f63d))

- Move `site-counter` into `includes/` where it belongs
  [#201](https://github.com/seedcase-project/decisions/pull/201) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([2d96378](https://github.com/seedcase-project/decisions/commit/2d9637860242e1e250e75baf5cdcfad6781f7604))

- Add `.zenodo.json` file
  [#215](https://github.com/seedcase-project/decisions/pull/215) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([961cecc](https://github.com/seedcase-project/decisions/commit/961cecc790dc1190646b6de11ec6d7cc7a176032))

- Update pre-commit hooks from template
  [#204](https://github.com/seedcase-project/decisions/pull/204) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([cac1b85](https://github.com/seedcase-project/decisions/commit/cac1b850356a7657e480b42038d0cf8ad6d80099))

- Apply `template-website` copier to repo
  [#205](https://github.com/seedcase-project/decisions/pull/205) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([410c796](https://github.com/seedcase-project/decisions/commit/410c796bedcd3e9e86be9fa0a964ec4b8795949c))

- Update developer settings from template
  [#207](https://github.com/seedcase-project/decisions/pull/207) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([0901081](https://github.com/seedcase-project/decisions/commit/09010812a0e63b79f99651382b7e1c34bd325278))

- Add auto-release workflow and config files
  [#210](https://github.com/seedcase-project/decisions/pull/210) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([6e87d3e](https://github.com/seedcase-project/decisions/commit/6e87d3ed7d250529fea3565ed75fdfcf370ea941))

### ❤️ New contributors

- `@github-actions[bot]` started making automated contributions
- [`@lwjohnst86`](https://github.com/lwjohnst86) made their first contribution
  in [#213](https://github.com/seedcase-project/decisions/pull/213)
- `@pre-commit-ci[bot]` started making automated contributions
- `@sync-files-token[bot]` started making automated contributions
- [`@signekb`](https://github.com/signekb) made their first contribution in
  [#173](https://github.com/seedcase-project/decisions/pull/173)
- [`@K-Beicher`](https://github.com/K-Beicher) made their first contribution in
  [#145](https://github.com/seedcase-project/decisions/pull/145)
- [`@martonvago`](https://github.com/martonvago) made their first contribution
  in [#135](https://github.com/seedcase-project/decisions/pull/135)
- [`@philter87`](https://github.com/philter87) made their first contribution
- [`@pchmia`](https://github.com/pchmia) made their first contribution

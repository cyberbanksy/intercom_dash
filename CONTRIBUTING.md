# Contributing

Thanks for helping. Setup and test steps are in the [README](README.md#setup).

## Issues

- Search existing issues first.
- Bug reports need the version, Python version and OS, and steps to reproduce.
- Security problems go through private reporting, see [SECURITY.md](SECURITY.md).
- Everyone taking part follows the [code of conduct](CODE_OF_CONDUCT.md).

## Pull requests

- One fix or feature per pull request, with a short description of how you tested it.
- Add or update tests when behavior changes.
- Keep commit messages short and imperative ("Add PDF bookmarks", not "Added bookmarks").
- Pull requests are squash-merged; the branch is deleted after merge.
- User-visible changes get a line under `## Unreleased` in `CHANGELOG.md`.
- Never commit keys, signing files, tokens, private server URLs or personal data.

## Automation you will see

- **CI** builds and tests every pull request.
- **Dependency review** fails a pull request that adds a dependency with a known high-severity
  vulnerability or a license outside the repository's allow-list.
- **CodeQL** scans the code; **zizmor** audits the GitHub Actions workflows; **OpenSSF Scorecard**
  checks the repository setup weekly. Findings appear under Security > Code scanning.
- **Dependabot** opens grouped dependency and GitHub Actions updates every week, and security updates
  as soon as an advisory is published.
- **CODEOWNERS** requests a review from the maintainer on every pull request.

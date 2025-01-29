# sonarqube-issue-conversion

<!-- markdownlint-disable -->
[![Linting & Formatting](https://github.com/philips-software/sonarqube-issue-conversion/actions/workflows/linting-formatting.yml/badge.svg)](https://github.com/philips-software/sonarqube-issue-conversion/actions/workflows/linting-formatting.yml) [![Continuous Integration](https://github.com/philips-software/sonarqube-issue-conversion/actions/workflows/ci.yml/badge.svg)](https://github.com/philips-software/sonarqube-issue-conversion/actions/workflows/ci.yml)
<!-- markdownlint enable -->

## Overview

sonarqube-issue-conversion is a GitHub Action that can convert the output of several tools into issues that can be ingested into SonarQube.

The currently supported conversions are:

- [gtest-to-generic-execution](#gtest-to-generic-execution): converts [GoogleTest](https://github.com/google/googletest) output to [Generic Execution](https://docs.sonarsource.com/sonarqube-server/latest/analyzing-source-code/test-coverage/generic-test-data/#generic-test-execution)

## State

This repository is under active development; see [pulse](https://github.com/philips-software/sonarqube-issue-conversion/pulse) for more details.

## Usage

### gtest-to-generic-execution

To use this conversion in your workflow, add the following steps. Adapting to your build system where necessary. Please note that GoogleTest needs to be instructed to write XML output files:

```yaml
jobs:
  transform-issues:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout
      - uses: lukka/run-cmake
        with:
          workflowPreset: "configure-build-test"
        env:
          GTEST_OUTPUT: "xml:${{ github.workspace }}/testresults/"
      - uses: philips-software/sonarqube-issue-conversion
        with:
          input: ${{ github.workspace }}/testresults/*.xml
          output: gtest-generic-execution.xml
          transformation: 'gtest-to-generic-execution'
```

You can now import this information using `sonar.testExecutionReportPaths` in your sonar-project.config.

## Community

This project uses a [code of conduct](.github/CODE_OF_CONDUCT.md) to define expected conduct in our community. Instances of
abusive, harassing, or otherwise unacceptable behavior may be reported to the repository administrators by using the [Report content](https://docs.github.com/en/communities/maintaining-your-safety-on-github/reporting-abuse-or-spam) functionality of GitHub.

## Changelog

See the [changelog](./CHANGELOG.md) for more info on what's been changed.

## Contributing

This project uses [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html) and [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/) please see the [contributing](.github/CONTRIBUTING.md) guideline for more information.

## Reporting vulnerabilities

If you find a vulnerability, please report it to us!
See [security](.github/SECURITY.md) for more information.

## Licenses

See [license](./LICENSE).

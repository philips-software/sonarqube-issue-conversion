# sonarqube-issue-conversion

This GitHub Action can convert several issue types into issues that can be ingested into SonarQube.

## Usage

To use this reusable GitHub Action in your workflow, add the following step:

```yaml
jobs:
  transform-issues:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - uses: philips-software/sonarqube-issue-conversion
        with:
          input: 'input'
          output: 'output'
          transformation: 'gtest-to-generic-execution'
```

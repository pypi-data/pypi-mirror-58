# tap-pivotal-tracker
[![PyPI version](https://badge.fury.io/py/tap-pivotal-tracker.svg)](https://badge.fury.io/py/tap-pivotal-tracker)
![PyPI - Status](https://img.shields.io/pypi/status/tap-pivotal-tracker)
[![Build Status](https://travis-ci.com/goodeggs/tap-pivotal-tracker.svg?branch=master)](https://travis-ci.com/goodeggs/tap-pivotal-tracker.svg?branch=master)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/tap-pivotal-tracker)

A [Singer](https://www.singer.io/) tap for extracting data from the [Pivotal Tracker REST API](https://www.pivotaltracker.com/help/api/rest/v5#top).

## Installation

Since package dependencies tend to conflict between various taps and targets, Singer [recommends](https://github.com/singer-io/getting-started/blob/master/docs/RUNNING_AND_DEVELOPING.md#running-singer-with-python) installing taps and targets into their own isolated virtual environments:

### Install Pivotal Tracker Tap

```bash
$ python3 -m venv ~/.venvs/tap-pivotal-tracker
$ source ~/.venvs/tap-pivotal-tracker/bin/activate
$ pip3 install tap-pivotal-tracker
$ deactivate
```

### Install Stitch Target (optional)

```bash
$ python3 -m venv ~/.venvs/target-stitch
$ source ~/.venvs/target-stitch/bin/activate
$ pip3 install target-stitch
$ deactivate
```

## Configuration

The tap accepts a JSON-formatted configuration file as arguments. This configuration file has s single required field:

1. `api_token`: A valid Pivotal Tracker API token.

A token for the Pivotal Tracker API can be obtained following the instructions [here](https://www.pivotaltracker.com/help/articles/api_token/). A bare-bones tap configuration may file may look like the following:

```json
{
  "api_token": "foobar",
}
```

### Granular Stream Configuration

Additionally, you may specify more granular configurations for individual streams. Each key under a stream should represent a valid API request parameter for that endpoint. A more fleshed-out configuration file may look similar to the following:

```json
{
  "api_token": "foobar",
  "api_version": "v5",
  "streams": {
    "stories": {
      "created_after": "2019-01-01T00:00:00",
      "limit": 500,
      "with_story_type": "bug",
      "with_state": "accepted",
      "with_label": "data-team"
    },
    "project_memberships": {
      "role": "owner"
    }
  }
}
```

## Streams

The current version of the tap syncs five distinct [Streams](https://github.com/singer-io/getting-started/blob/master/docs/SYNC_MODE.md#streams):
1. `Accounts`: [Endpoint Documentation](https://www.pivotaltracker.com/help/api/rest/v5#Account)
2. `Labels`: [Endpoint Documentation](https://www.pivotaltracker.com/help/api/rest/v5#Labels)
3. `Projects`: [Endpoint Documentation](https://www.pivotaltracker.com/help/api/rest/v5#Projects)
4. `Project Memberships`: [Endpoint Documentation](https://www.pivotaltracker.com/help/api/rest/v5#Project_Memberships)
5. `Stories`: [Endpoint Documentation](https://www.pivotaltracker.com/help/api/rest/v5#Stories)

## Discovery

Singer taps describe the data that a stream supports via a [Discovery](https://github.com/singer-io/getting-started/blob/master/docs/DISCOVERY_MODE.md#discovery-mode) process. You can run the Dayforce tap in Discovery mode by passing the `--discover` flag at runtime:

```bash
$ ~/.venvs/tap-pivotal-tracker/bin/tap-pivotal-tracker --config=config/pivotal.config.json --discover
```

The tap will generate a [Catalog](https://github.com/singer-io/getting-started/blob/master/docs/DISCOVERY_MODE.md#the-catalog) to stdout. To pass the Catalog to a file instead, simply redirect it to a file:s

```bash
$ ~/.venvs/tap-pivotal-tracker/bin/tap-pivotal-tracker --config=config/pivotal.config.json --discover > catalog.json
```

## Sync to stdout

Running a tap in [Sync mode](https://github.com/singer-io/getting-started/blob/master/docs/SYNC_MODE.md#sync-mode) will extract data from the various selected Streams. In order to run a tap in Sync mode and have messages emitted to stdout, pass a valid configuration file and catalog file:

```bash
$ ~/.venvs/tap-pivotal-tracker/bin/tap-pivotal-tracker --config=config/pivotal.config.json --catalog=catalog.json
```

The tap will emit occasional [Metric](https://github.com/singer-io/getting-started/blob/master/docs/SYNC_MODE.md#metric-messages), [Schema](https://github.com/singer-io/getting-started/blob/master/docs/SPEC.md#schema-message), [Record](https://github.com/singer-io/getting-started/blob/master/docs/SPEC.md#record-message), and [State messages](https://github.com/singer-io/getting-started/blob/master/docs/SPEC.md#state-message). You can persist State between runs by redirecting messages to a file:

```bash
$ ~/.venvs/tap-pivotal-tracker/bin/tap-pivotal-tracker --config=config/pivotal.config.json --catalog=catalog.json >> state.json
$ tail -1 state.json > state.json.tmp
$ mv state.json.tmp state.json
```

## Sync to Stitch

You can also send the output of the tap to [Stitch Data](https://www.stitchdata.com/) for loading into the data warehouse. To do this, first create a JSON-formatted configuration for Stitch.

An example configuration file will look as follows:

```json
{
  "client_id": 1234,
  "token": "foobar",
  "small_batch_url": "https://api.stitchdata.com/v2/import/batch",
  "big_batch_url": "https://api.stitchdata.com/v2/import/batch",
  "batch_size_preferences": {}
}
```

Once the configuration file is created, simply pipe the output of the tap to the Stitch Data target and supply the target with the newly created configuration file:

```bash
$ ~/.venvs/tap-pivotal-tracker/bin/tap-pivotal-tracker --config=config/dayforce.config.json --catalog=catalog.json --state=state.json | ~/.venvs/target-stitch/bin/target-stitch --config=config/stitch.config.json >> state.json
$ tail -1 state.json > state.json.tmp
$ mv state.json.tmp state.json
```

## Contributing

The first step to contributing is getting a copy of the source code. First, [fork `tap-pivotal-tracker` on GitHub](https://github.com/goodeggs/tap-pivotal-tracker/fork). Then, `cd` into the directory where you want your copy of the source code to live and clone the source code:

```bash
$ git clone git@github.com:YourGitHubName/tap-pivotal-tracker.git
```

Now that you have a copy of the source code on your local machine, you can leverage [Pipenv](https://docs.pipenv.org/en/latest/) and the corresponding `Pipfile` to install of the development dependencies within a virtual environment:

```bash
$ pipenv install --three --dev
```

This command will create an isolated virtual environment for your `tap-pivotal-tracker` project and install all the development dependencies defined within the `Pipfile` inside of the environment. You can then enter a shell within the environment:

```bash
$ pipenv shell
```

Or, you can run individual commands within the environment without entering the shell:

```bash
$ pipenv run <command>
```

For example, to format your code using [isort](https://github.com/timothycrosley/isort) and [flake8](http://flake8.pycqa.org/en/latest/index.html) before commiting changes, run the following commands:

```bash
$ pipenv run make isort
$ pipenv run make flake8
```

You can also run the entire testing suite before committing using [tox](https://tox.readthedocs.io/en/latest/):

```bash
$ pipenv run tox
```

Finally, you can run your local version of the tap within the virtual environment using a command like the following:

```bash
$ pipenv run tap-pivotal-tracker --config=config/pivotal.config.json --catalog=catalog.json
```

Once you've confirmed that your changes work and the testing suite passes, feel free to put out a PR!

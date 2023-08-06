changelogfromtags ![Git Logo](images/git.png)
[![pipeline status](https://gitlab.com/cdlr75/changelogfromtags/badges/master/pipeline.svg)](https://gitlab.com/cdlr75/changelogfromtags/commits/master)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-green.svg)](https://www.python.org/dev/peps/pep-0008/)
[![Downloads](https://pepy.tech/badge/changelogfromtags)](https://pepy.tech/project/changelogfromtags)
===

### Changelog generation has never been so easy

**Fully automated changelog generation** - This package generates a changelog file based on **git tags**.

Since you don't have to fill your `CHANGELOG.md` manually now: just run the script, relax and take a cup of :coffee: before your next release! :tada:

### *What’s the point of a changelog?*

To make it easier for users and contributors to see precisely what notable changes have been made between each release (or version) of the project.

### *Why should I care?*

Because software tools are for _people_. "Changelogs make it easier for users and
contributors to see precisely what notable changes have been made between each
release (or version) of the project."

→ *[https://keepachangelog.com](https://keepachangelog.com)*

## Installation

Install the python package like:

    $ pip install changelogfromtags


## Usage


### Running with CLI:

    $ changelogfromtags


### Running with Docker

TBA

## Output example

- Look at **[CHANGELOG.md](https://cdlr75.gitlab.io/changelogfromtags/CHANGELOG.html)** for this project


## Features and advantages of this project

- Changelog entries are directly taken from git tags messages
- No requirements except python and git
- Generate canonical, neat changelog file, with default sections that follow [basic changelog guidelines](http://keepachangelog.com)


### Alternatives

Here is a [wikipage list of alternatives](https://github.com/github-changelog-generator/Github-Changelog-Generator/wiki/Alternatives) that I found. But none satisfied my requirements.

*If you know other projects, feel free to edit this Wiki page!*


## License

changelogfromtags is released under the [MIT License](http://www.opensource.org/licenses/MIT).


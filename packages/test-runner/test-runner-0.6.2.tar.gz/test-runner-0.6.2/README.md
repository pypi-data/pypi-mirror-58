# test-runner—A Runner for Python Tests

[![Build Status](https://travis-ci.com/pytesting/test-runner.svg?token=ZgCiES6Mybgq3a2Jbw2K&branch=master)](https://travis-ci.com/pytesting/test-runner)
[![codecov](https://codecov.io/gh/pytesting/test-runner/branch/master/graph/badge.svg?token=yLu7itEVep)](https://codecov.io/gh/pytesting/test-runner)
[![License GPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![PyPI version](https://badge.fury.io/py/test-runner.svg)](https://badge.fury.io/py/test-runner)
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/test-runner.svg)](https://github.com/pytesting/test-runner)

Running Python tests is a complicated task, as it seems that there is not
standard way of doing it.
`test-runner` implements some heuristics that try to run tests with or without
coverage measuring, independent of the used testing framework.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- You have installed Python at least in version 3.6.
- You have a recent Linux machine.
  The library is most likely to not work on another operating system since it is
  depending on [`benchexec`](https://github.com/sosy-lab/benchexec) for resource
  handling, which currently only runs on recent versions of Linux.
- For development it is necessary to have the [`poetry`](https://poetry.eustace.io)
 packaging and dependency management system.
 
## Installing Test Runner

Test Runner can be easily installed from [PyPI](https://pypi.org) using the
 `pip` utility:
```bash
pip install test-runner
```

## Contributing to Test Runner

To contribute to Test Runner, follow these steps:
1. Fork this repository.
2. Setup a virtual environment for development using `poetry`: `poetry install`.
3. Create a branch: `git checkout -b <branch_name>`.
4. Make your changes and commit them `git commit -m '<commit_message>'`.
5. Push to the original branch: `git push origin <project_name>/<location>`.
6. Create the pull request.

Please note that we require you to meet the following criteria:
- Write unit tests for your code.
- Run linting with `flake8` and `pylint`
- Run type checking using `mypy`
- Format your code according to the `black` code style

To ease the execution of the tools, we provide a `Makefile` with various targets.
The easiest way to execute all checks is to run `make check` on a `poetry shell`.
Push your commits only if they pass all checks!
These tools are also executed in continuous integration on TravisCI and will also
 check you pull request.
Failing a check will block your pull request from being merged!

## Contributors

See the [Contributors page](https://github.com/pytesting/test-runner/graphs/contributors)
for a list of contributors.
Thanks to all contributors!


## License

`test-runner` is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

`test-runner` is distributed in the hope that it will be useful
but WITHOUT ANY WARRANT; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a [copy](LICENSE.txt) of the
GNU Lesser General Public License
along with `test-runner`.  If not, see
[https://www.gnu.org/licenses/](https://www.gnu.org/licenses/).

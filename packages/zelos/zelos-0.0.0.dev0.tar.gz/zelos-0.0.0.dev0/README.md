[![Build Status](https://dev.azure.com/kevin0853/zelos/_apis/build/status/zeropointdynamics.zelos?branchName=master)](https://dev.azure.com/kevin0853/zelos/_build/latest?definitionId=1&branchName=master)
[![codecov](https://codecov.io/gh/zeropointdynamics/zelos/branch/master/graph/badge.svg)](https://codecov.io/gh/zeropointdynamics/zelos)
[![Documentation Status](https://readthedocs.org/projects/zelos/badge/?version=latest)](https://zelos.readthedocs.io/en/latest/?badge=latest)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

# zelos
Zelos is a Python-based binary emulation platform.

*Work in Progress*: We are working towards open sourcing the zelos emulation platform. There is no code here *yet*.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install zelos.

```bash
pip install zelos
```

## Basic Usage

Command-line usage:
```bash
$ zelos run my_binary
```

Programmatic usage:
```python
import zelos

z = zelos.Engine("static_elf_helloworld")
z.start(timeout=3)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[AGPL v3](https://www.gnu.org/licenses/agpl-3.0.en.html)

# Learn Pipenv

**Python Tutorial: Pipenv - Easily Manage Packages and Virtual Environments**<br>
https://www.youtube.com/watch?v=zDYL22QNiWk&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU

New way to combine package management with virtual environments. <br>
Basically it combines `pip` and `virtualenv`

## Content

- [Prerequisite](#prerequisite)
- [Installation](#installation)
- [Getting Started](#getting-started)
  - [Install a dependency](#install-a-dependency)
  - [`Pipfile`](#pipfile)
- [Activate virtual environment](#activate-virtual-environment)
  - [`exit`](#exit-pipenv-and-deactivate-virtual-environment)
- [Run commands without activating virtual environment](#run-commands-without-activating-virtual-environment)
- [Using existing `requirements.txt` with `pipenv`](#using-an-existing-requirementstxt-with-pipenv)
- [Install dev dependency](#install-a-dev-dependency)
- [Show dependency graph](#showing-a-dependency-graph)
- [Locate virtual environment](#location-of-virtual-environment)
- [Removing virtual environment](#removing-a-virtual-environment)
- [Reinstall virtual environment](#reinstall-virtual-environment)
- [Reinstall for Starting Development](#reinstall-for-development)
- [Checking for package vulnerabilities](#checking-for-vulnerabilities)
- [Ready for Production](#ready-for-production)
- [`pipenv` Help](#help)

## Prerequisite

- Python 3 (3.12+) installed and `pip`
- Blank directory (_empty folder_) for starting your project
- Knowledge about `virtualenv` and `pip`.

### Bonus

- Knowledge on [Node.js][node]

[node]: https://nodejs.org/

```bash
pip list
```

```bash
Package      Version
------------ ---------
pip          24.0
```

## Installation

```bash
pip install pipenv
```

```bash
Package      Version
------------ ---------
certifi      2024.2.2
distlib      0.3.8
filelock     3.13.1
pip          24.0
pipenv       2023.12.1
platformdirs 4.2.0
setuptools   69.1.1
virtualenv   20.25.1
```

## Getting Started

### Install a dependency

At this point, we **do NOT need** to create a virtual environment
as `pipenv` would automatically create it for us whenever we install packages.

In this example, we'll choose a random Python package (`requests`).

The command for installing a dependency is: `pipenv install <package_name>`

```bash
pipenv install requests
```

Upon installation, you would notice that it will **automatically** create a virtual environment for us.

(`learn-python` is the folder name of our current working directory)

```bash
Creating a virtualenv for this project...
Pipfile: path\to\learn-python\Pipfile
Using default python from path\to\user\AppData\Local\Programs\Python\Python312\python.exe (3.12.2) to create virtualenv...
[ ===] Creating virtual environment...created virtual environment CPython3.12.2.final.0-64 in 13462ms
  creator CPython3Windows(dest=path\to\user\.virtualenvs\learn-python-pZkRk3FM, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, via=copy, app_data_dir=path\to\user\AppData\Local\pypa\virtualenv)
    added seed packages: pip==24.0
  activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

Successfully created virtual environment!
Virtualenv location: path\to\user\.virtualenvs\learn-python-pZkRk3FM
Creating a Pipfile for this project...
Installing requests...
Resolving requests...
Added requests to Pipfile's [packages] ...
Installation Succeeded
Pipfile.lock not found, creating...
Locking [packages] dependencies...
Building requirements...
Resolving dependencies...
Success!
Locking [dev-packages] dependencies...
Updated Pipfile.lock (1977acb1ba9778abb66054090e2618a0a1f1759b1b3b32afd8a7d404ba18b4fb)!
Installing dependencies from Pipfile.lock (18b4fb)...
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
```

The virtual environment it created is the same one when you manually create using `virtualenv`.

Notice that it also generated 2 files: `Pipfile` and `Pipfile.lock`

- `Pipfile` - is similar to `package.json` in [Node.js][node].
- `Pipfile.lock` - is similar to `package-lock.json` in [Node.js][node]

### `Pipfile`

a replacement for `requirements.txt`

```toml
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
requests = "*"

[dev-packages]

[requires]
python_version = "3.12"
```

Observe that it only provided `*` in the `requests` package, means that we did not specify any version
during the installation. So whenever we install it again, it will now look for a latest version.

In the terminal, after installing the Python package,
you would also read an instruction for the following steps:

```bash
To activate this project's virtualenv, run `pipenv shell`.
Alternatively, run a command inside the virtualenv with `pipenv run`.
```

## Activate Virtual Environment

```bash
pipenv shell
```

### Exit `pipenv` and deactivate virtual environment

To **exit** `pipenv shell` and **deactivate** the virtual environment, run the following command:

```bash
exit
```

## Run commands without activating virtual environment

Without the need to activate the virtual environment,
you can actually execute python scripts or commands,
as if you were inside the virtual environment.

In case when you just simply want to run a command,
so there is no need of activating or going inside the virtual environment.

```bash
pipenv run <command>
```

Example:

```bash
pipenv run pip list
```

This will display a list of packages installed in the virtual environment

More examples

```bash
pipenv run python main.py
```

## Using an existing `requirements.txt` with `pipenv`

You can use `pipenv` to install the Python packages or dependencies
from your existing Python project that contains a `requirements.txt`

```bash
pipenv install -r requirements.txt
```

After the `-r` flag, you must then provide the path and filename to your `requirements.txt`

## Install a dev dependency

The command on installing a dev dependency is: `pipenv install <package_name> --dev`

In this example, we'll install the `pytest` package.

```bash
pipenv install pytest --dev
```

`Pipfile` should automatically be updated:

```diff
 [[source]]
 url = "https://pypi.org/simple"
 verify_ssl = true
 name = "pypi"

 [packages]
 requests = "*"

 [dev-packages]
+pytest = "*"

 [requires]
 python_version = "3.12"
```

## Showing a dependency graph

```bash
pipenv graph
```

**Result**

```bash
pytest==8.0.2
├── colorama [required: Any, installed: 0.4.6]
├── iniconfig [required: Any, installed: 2.0.0]
├── packaging [required: Any, installed: 23.2]
└── pluggy [required: >=1.3.0,<2.0, installed: 1.4.0]
requests==2.31.0
├── certifi [required: >=2017.4.17, installed: 2024.2.2]
├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
├── idna [required: >=2.5,<4, installed: 3.6]
└── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
```

## Location of virtual environment

```bash
pipenv --venv
```

## Removing a virtual environment

```bash
pipenv --rm
```

## Reinstall virtual environment

From any existing project with `Pipfile` can easily reinstall all packages (depencies and dev-dependencies) and create virtual environment

```bash
pipenv install
```

## Reinstall FOR DEVELOPMENT

```bash
pipenv install --dev
```

This will install all dependencies including dev.

### Clean reinstall FOR DEVELOPMENT

```bash
pipenv install --dev --ignore-pipfile
```

## Checking for vulnerabilities

```bash
pipenv check
```

## Ready for Production

```bash
pipenv lock
```

Then tell Production environment to install everything from the `Pipfile.lock`

```bash
pipenv install --ignore-pipfile
```

(_Similar with `npm ci` in [Node.js][node]
which installs packages with versions defined in `package-lock.json`_)

## Help

You can always see more available options

```bash
pipenv --help
```

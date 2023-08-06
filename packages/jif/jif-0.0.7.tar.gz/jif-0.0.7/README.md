# jif

jif is a small CLI tool inspired by NPM, more specifically the `npm run` and `npm install` commands. There are no plans to make jif anything more. It is a small tool with a handful of commands that solve pain points I face on a daily basis.

### Why jif?

I've used a package.json to run my Python scripts before. This works fine for me as I have NPM already installed locally. However, it becomes an issue if I want to run a script on a CI/CD machine, a VM created for Python apps or if a collegue who doesn't use Node is working on the application.

**TLDR;** jif started out as a simple CLI tool built in Python to run scripts similar to NPM.

---

## Installation

`python -m pip install jif`

\*I recommend installing and using jif in a virtualenv. It'll probably work fine globally but it is built with the assumption it is running in a virtualenv.

## Commands

You can view all the commands with the CLI by running `jif --help`.
If you want more details about a specific command, run `jif <COMMAND> --help`.

### `init`

The `init` command creates the jif file (`jif.json`) that the other commands use. The file will be saved in the dir that the command is run.

##### Optional flags

| Flag            | Description                                                                          | Default                                  |
| --------------- | ------------------------------------------------------------------------------------ | ---------------------------------------- |
| `--entry-point` | Use this flag to point to the module that should run when calling the start command. | `app.py`                                 |
| `--lint-dir`    | Use this flag to tell jif which directory should be linted.                          | `.`                                      |
| `--version`     | Which version your package should begin at.                                          | `0.0.1`                                  |
| `--author`      | Credits author.                                                                      | None, omitted unless value is specified. |
| `--package`     | Name of your package.                                                                | None, omitted unless value is specified. |

_examples_: `jif init`, `jif init --lint-dir src --entry-point src/main.py`

### `run`

The jif file let's you store scripts which can be executed using the `run` command.
The following scripts can omit the `run` keyword: `start`, `lint` and `test`.

_examples_: `jif start`, `jif run my_script`

### `install`

The `install` command uses pip to install packages and then automatically manages them for you in your jif file. If the `requirements_file` is present, requirements will be duplicated there so your application isn't dependent on jif. 

##### Optional flags

There are two optional flags that can be added to the end of your install command - `--no-save` and `--dev`. By default, when package(s) are installed they will be added to the requirements array in the jif file. If you add `--dev`, it will save all those packages to the dev requirements array. If you want to install a package without saving it anywhere, add `--no-save` to the end of your install command.

_examples_: `jif install flask`, `jif install black autopep8 --dev`, `jif install black --no-save`

### `uninstall`

The `uninstall` command will uninstall all packages specified then check to see if they are listed in either the requirements or dev requirements in the jif file. If they are in either, they will be removed. If the `dev_requirements_file` is present, requirements will be duplicated there so your application isn't dependent on jif.

_examples_: `jif uninstall flask black autopep`

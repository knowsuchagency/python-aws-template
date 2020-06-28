# {{cookiecutter.project}}

## Features

* [poetry][poetry]
* [invoke][invoke]
* [aws cdk][aws cdk]
* [chalice][chalice]
* [pre-commit][pre-commit]

## Setup

```bash
# set up python

brew install python@3.8

ln -s /usr/local/opt/python@3.8/bin/python3.8 /usr/local/bin/python3.8

python3.8 -m pip install -U pip

python3.8 -m pip install pipx # I recommend installing poetry this way

# You may need to run the following on your local machine, and then launch a new shell.

pipx ensurepath

# install poetry and other dev clis

pipx install poetry

# setup npm and the aws-cdk cli

npm install -g aws-cdk


# clone the repo and cd into it

git clone ...

cd {{cookiecutter.project}}

# create a virtual environment and activate it (poetry will create one for you if you don't do it explicity)

python3.8 -m venv .venv

. .venv/bin/activate

# install project dependencies

poetry install

# see what commands are available in tasks.py

inv -l

# install git hooks

inv install-hooks

# deploy

inv deploy
```

[poetry]: https://python-poetry.org
[invoke]: http://www.pyinvoke.org
[aws cdk]: https://docs.aws.amazon.com/cdk/api/latest/
[chalice]: https://github.com/aws/chalice
[pre-commit]: https://pre-commit.com
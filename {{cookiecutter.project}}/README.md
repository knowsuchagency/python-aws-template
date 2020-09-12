# {{cookiecutter.project}}

## Requires
* Python >= 3.8
* [aws cdk][cdk installation]

## Setup

```bash
# clone the repo and cd into it

git clone ...

cd {{cookiecutter.project}}

# create a virtual environment and activate it (poetry will create one for you if you don't do it explicity)

python3.8 -m venv .venv

. .venv/bin/activate

# install project dependencies

pip install -U pip

pip install flit

flit install

# see what commands are available in tasks.py

inv -l

# install git hooks

inv install-hooks

# deploy

inv deploy
```

## Features

* [poetry][poetry]
* [invoke][invoke]
* [aws cdk][aws cdk]
* [chalice][chalice]
* [pre-commit][pre-commit]

[poetry]: https://python-poetry.org
[invoke]: http://www.pyinvoke.org
[aws cdk]: https://docs.aws.amazon.com/cdk/api/latest/
[chalice]: https://github.com/aws/chalice
[pre-commit]: https://pre-commit.com
[cdk installation]: https://docs.aws.amazon.com/cdk/latest/guide/cli.html

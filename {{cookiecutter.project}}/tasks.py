import os
import tempfile
from pathlib import Path

import toml
from invoke import task


@task
def clean(c):
    """Delete potentially stale python bytecode."""
    c.run("find . -name \*.pyc -delete")


@task
def install_hooks(c):
    """Install git hooks."""
    c.run("pre-commit install")
    c.run("pre-commit install -t pre-push")


@task(aliases=["black"])
def format(c):
    """Auto-format Python modules."""
    c.run("black tasks.py app.py cdk_app.py {{cookiecutter.project}}/")


@task(aliases=["check-black"])
def check_formatting(c):
    """Check that files conform to black standards."""
    c.run("black --check tasks.py app.py cdk_app.py {{cookiecutter.project}}/")


@task(clean)
def test(c):
    """Run unit tests."""
    c.run("pytest test_{{cookiecutter.project}}/ -vv", pty=True)


@task(aliases=["build"])
def package(c):
    """Render chalice package for deployment."""

    package_config = toml.load("poetry.lock")

    dependencies = package_config["package"]

    vendor_path = Path("vendor")

    chalice_output = Path("chalice.out")

    c.run(f"rm -rf {vendor_path} {chalice_output}",)

    with tempfile.NamedTemporaryFile(suffix=".txt") as tf:

        lines = []

        for dep in dependencies:
            name = dep["name"]
            version = dep["version"]
            category = dep["category"]

            if category != "main":
                continue
            else:
                lines.append((f"{name}=={version}" + os.linesep).encode())

        tf.writelines(lines)

        tf.seek(0)

        c.run(f"pip install -r {tf.name} --no-binary=:none: -t {vendor_path}",)

    c.run(f"cp -r {{cookiecutter.project}} {vendor_path}",)

    c.run(f"chalice package {chalice_output}",)

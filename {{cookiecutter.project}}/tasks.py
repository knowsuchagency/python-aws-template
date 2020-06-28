from invoke import Responder, task


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

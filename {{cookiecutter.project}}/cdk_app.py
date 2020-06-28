import os
import subprocess as sp
import tempfile
from pathlib import Path

import toml
from aws_cdk import core
from cdk_chalice_lite import Chalice


class ProjectStack(core.Stack):
    def _setup_chalice_deployment(self):
        package_config = toml.load("poetry.lock")

        dependencies = package_config["package"]

        vendor_path = Path("vendor")

        chalice_output = Path("chalice.out")

        sp.run(
            f"rm -rf {vendor_path} {chalice_output}",
            shell=True,
            capture_output=True,
        )

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

            sp.run(
                f"pip install -r {tf.name} --no-binary=:none: -t {vendor_path}",
                shell=True,
                capture_output=True,
            )

        sp.run(
            f"cp -r {{cookiecutter.project}} {vendor_path}",
            shell=True,
            capture_output=True,
        )

        sp.run(
            f"chalice package {chalice_output}",
            shell=True,
            capture_output=True,
        )

        return chalice_output

    def __init__(self, scope, id, **kwargs):
        super().__init__(scope, id, **kwargs)

        chalice_output = self._setup_chalice_deployment()

        self.chalice = Chalice(self, "chalice-app", f"{chalice_output}",)


app = core.App()

stack = ProjectStack(app, "{{cookiecutter.project}}")


app.synth()

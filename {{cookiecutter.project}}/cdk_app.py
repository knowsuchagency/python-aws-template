from aws_cdk import core
from cdk_chalice_lite import Chalice


class ProjectStack(core.Stack):
    def __init__(self, scope, id, **kwargs):
        super().__init__(scope, id, **kwargs)

        self.chalice = Chalice(self, "chalice-app", "chalice.out",)


app = core.App()

stack = ProjectStack(app, "{{cookiecutter.project}}")


app.synth()

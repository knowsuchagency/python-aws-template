import chalice


app = chalice.Chalice(app_name="{{cookiecutter.project}}")


@app.route("/")
def index():
    """This is just an initial test endpoint."""
    # TODO: delete this method once finished testing
    return {"hello": "{{cookiecutter.project}}"}

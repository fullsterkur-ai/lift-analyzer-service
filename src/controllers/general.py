import tomllib


def index():
    with open("pyproject.toml", "rb") as file:
        project_details = tomllib.load(file)["project"]

    return {
        "service": project_details["name"],
        "version": project_details["version"],
    }


def health():
    return {"status": "healthy"}

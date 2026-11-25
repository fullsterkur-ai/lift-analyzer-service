import tomllib

def index():
  project_details = tomllib.load(open("pyproject.toml", "rb"))["project"]
  return {
    "service": "lift-analyzer-service",
    "version": project_details["version"],
  }

def health():
  return {
    "status": "healthy"
  }
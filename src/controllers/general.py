from importlib import metadata

def index():
  return {
    "service": "lift-analyzer-service",
    "version": metadata.version
  }

def health():
  return {
    "status": "healthy"
  }
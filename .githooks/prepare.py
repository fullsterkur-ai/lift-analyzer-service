from pathlib import Path

source = Path(".githooks/pre-commit")
destination = Path(".git/hooks/pre-commit")

destination.write_text(source.read_text())
destination.chmod(0o755)

print("Git hooks installed successfully")

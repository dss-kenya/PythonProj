import os
from pathlib import Path

REPO_ROOT = Path(os.path.dirname(os.path.abspath(__file__))).parent
FILE_PLAYGROUND_INPUT_DIRECTORY: Path = REPO_ROOT / "playground"
FILE_PLAYGROUND_OUTPUT_DIRECTORY: Path = REPO_ROOT / "playground/output"

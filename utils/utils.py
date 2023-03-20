import os
from shutil import rmtree
from utils.constants import (
    FILE_PLAYGROUND_INPUT_DIRECTORY,
    FILE_PLAYGROUND_OUTPUT_DIRECTORY,
)


def read_file_contents() -> list[str]:
    print(str(FILE_PLAYGROUND_OUTPUT_DIRECTORY))
    with open(
        os.path.join(str(FILE_PLAYGROUND_INPUT_DIRECTORY), "input_file.txt")
    ) as file:
        return file.readlines()


def clean_output_directory():
    if FILE_PLAYGROUND_OUTPUT_DIRECTORY.exists():
        rmtree(FILE_PLAYGROUND_OUTPUT_DIRECTORY)
    FILE_PLAYGROUND_OUTPUT_DIRECTORY.mkdir(parents=True, exist_ok=True)

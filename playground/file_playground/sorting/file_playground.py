import os
from utils.constants import FILE_PLAYGROUND_OUTPUT_DIRECTORY
from utils.utils import read_file_contents


class FilePlayground:
    def sort_file():
        input_list = read_file_contents()
        input_list.sort(key=str.casefold)

        with open(
            os.path.join(str(FILE_PLAYGROUND_OUTPUT_DIRECTORY), "output_file.txt"), "w"
        ) as file:
            file.writelines(output for output in input_list)

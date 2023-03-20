from utils.utils import clean_output_directory
from playground.file_playground.sorting.file_playground import FilePlayground


def execute_all():
    clean_output_directory()
    FilePlayground.sort_file()

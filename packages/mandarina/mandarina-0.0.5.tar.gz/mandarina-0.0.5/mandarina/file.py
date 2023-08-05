"""
This module provides functionality to work with files and folders.
"""
import math
import os


def create_dir_if_doesnt_exist(folderpath):
    """
    Creates a folder if it doesn't exist.

    :param folderpath:
    :return: True if folder was created, else False

    """
    if not os.path.exists(folderpath):
        os.makedirs(folderpath)
        return True
    return False


def delete_file(filepath):
    """
    Deletes the specified file if the file exists.

    :param filepath: Path of the file to be deleted
    :return: True if the file was deleted, else False

    """
    if os.path.isfile(filepath):
        os.remove(filepath)
        return True
    else:
        print("Error: %s file not found" % filepath)
        return False


def delete_dir(dirpath):
    """
    Deletes the specified directory if it exists

    :param dirpath: Path to the directory
    :return: True if the directory was deleted, else False

    """
    if os.path.isdir(dirpath):
        os.rmdir(dirpath)
        return True
    else:
        print("Error: %s directory not found" % dirpath)
        return False


def count_files_in_dir(dirpath):
    """
    Counts the number of files contained in the specified
    directory.

    :param dirpath: Path to the directory
    :return: Number of files

    """
    return len(
        [
            name
            for name in os.listdir(dirpath)
            if os.path.isfile(os.path.join(dirpath, name))
        ]
    )


def convert_size_bytes_to_human_readable_format(size_bytes):
    """
    Converts a size in bytes to a human readable format.

    :param size_bytes: The size in bytes
    :return: Bytes converted to readable format
    """
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KiB", "MiB", "GiB", "TiB", "PiB", "EiB", "ZiB", "YiB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"

import os

def find_spartan_edb():
    # set the root directory to search from
    root_dir = os.path.expanduser("~")

    # set the search pattern for the file
    file_pattern = "spartan.edb"

    # walk the directory tree and search for the file
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename == file_pattern:
                # return the full path to the file if found
                return os.path.join(dirpath, filename)

    # return None if the file was not found
    return None

print(find_spartan_edb())
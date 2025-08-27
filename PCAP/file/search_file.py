import os

def search_file_in_dir(dir_path, file_name):
    """Search for a file in a directory and its subdirectories.

    Args:
        dir_path (str): The path of the directory to search in.
        file_name (str): The name of the file to search for.

    Returns:
        str: The full path of the found file, or None if not found.
    """
    for root, dirs, files in os.walk(dir_path):
        if file_name in files:
            return os.path.join(root, file_name)
    return None

if __name__ == "__main__":
    directory = input("Enter the directory path to search in: ")
    filename = input("Enter the filename to search for: ")
    result = search_file_in_dir(directory, filename)
    if result:
        print(f"File found: {result}")
    else:
        print("File not found.")

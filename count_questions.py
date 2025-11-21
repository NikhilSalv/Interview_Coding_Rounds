# import os

# def count_all_files(path='.'):
#     """Count all unique files inside a directory, including subfolders."""
#     file_paths = set()  # use a set to ensure uniqueness

#     for root, _, files in os.walk(path):
#         for file in files:
#             full_path = os.path.join(root, file)
#             file_paths.add(os.path.abspath(full_path))  # store absolute path

#     return len(file_paths), file_paths


# if __name__ == "__main__":
#     cwd = os.getcwd()  # current working directory
#     total_files, file_list = count_all_files(cwd)

#     print(f"📂 Scanning directory: {cwd}")
#     print(f"🧾 Total unique files found: {total_files}")

#     # Optional: Uncomment to print all file paths
#     # for file in sorted(file_list):
#     #     print(file)

import os

def count_python_files(path='.'):
    """Count all unique .py files inside a directory (including subfolders)."""
    python_files = set()  # ensure uniqueness

    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith('.py'):  # only count .py files
                full_path = os.path.join(root, file)
                python_files.add(os.path.abspath(full_path))

    return len(python_files), python_files


if __name__ == "__main__":
    cwd = os.getcwd()  # current working directory
    total_files, file_list = count_python_files(cwd)

    print(f"📂 Scanning directory: {cwd}")
    print(f"🐍 Total unique Python (.py) files found: {total_files}")

    # Optional: Uncomment to print all file paths
    # for file in sorted(file_list):
    #     print(file)


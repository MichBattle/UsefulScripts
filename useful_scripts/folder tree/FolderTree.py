import os

def print_tree(startpath, include_files=False):
    def _print_tree(current_path, prefix, is_last):
        nonlocal tree_str
        basename = os.path.basename(current_path)
        connector = '└── ' if is_last else '├── '
        tree_str += f"{prefix}{connector}{basename}/\n"

        # Update prefix for subdirectories
        if is_last:
            new_prefix = prefix + "    "
        else:
            new_prefix = prefix + "│   "

        # Get directories and, if requested, files
        try:
            entries = os.listdir(current_path)
        except PermissionError:
            return  # Skip directories we don't have permission for

        # Filter out hidden `.git` directories and sort
        dirs = sorted([d for d in entries if os.path.isdir(os.path.join(current_path, d)) and not d.startswith('.git')])
        files = sorted([f for f in entries if os.path.isfile(os.path.join(current_path, f))])

        total_dirs = len(dirs)
        for idx, directory in enumerate(dirs):
            is_last_dir = (idx == total_dirs - 1) and (not include_files or not files)
            _print_tree(os.path.join(current_path, directory), new_prefix, is_last_dir)

        if include_files:
            total_files = len(files)
            for idx, file in enumerate(files):
                is_last_file = (idx == total_files - 1)
                connector_file = '└── ' if is_last_file else '├── '
                tree_str += f"{new_prefix}{connector_file}{file}\n"

    tree_str = ""
    _print_tree(startpath, "", True)
    return tree_str

# Menu
def menu():
    print("Menu:")
    print("1 - Include files")
    print("2 - Exclude files")
    choice = input("Input: ")
    return choice

# Main
if __name__ == "__main__":
    folder = '/your/path/here/'  # Replace with the desired path
    choice = menu()

    if choice == '1':
        directory_structure_string = print_tree(folder, include_files=True)
        print(directory_structure_string)
    elif choice == '2':
        directory_structure_string = print_tree(folder, include_files=False)
        print(directory_structure_string)
    else:
        print("Error: invalid choice.")
        
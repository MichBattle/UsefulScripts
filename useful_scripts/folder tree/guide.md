# Guide to Using the `print_tree` Script

This script allows you to print the directory structure of a folder, either including or excluding the files. It mimics the tree-like output you often see in file managers, but offers additional flexibility.

## Features
- Print the folder structure of any directory on your system.
- Option to include or exclude files.
- Filter out `.git` folders and any hidden files or directories starting with `.git`.

## Requirements
- Python 3.x
- OS module (comes pre-installed with Python)

## Usage

### 1. Structure of the Script

The script is divided into two main parts:

- **`print_tree` function**: Recursively prints the directory structure.
- **Menu**: Allows you to choose between including or excluding files.

### 2. How the `print_tree` Function Works

The `print_tree` function takes two parameters:
- `startpath`: The directory you want to explore.
- `include_files`: A boolean flag that controls whether files should be included in the output. Set to `True` to include files, `False` to exclude them.

### 3. Running the Script

- First, update the `folder` variable in the `main` section of the code with the path of the directory you want to explore.
  
Example:
```python
folder = '/your/path/here/'
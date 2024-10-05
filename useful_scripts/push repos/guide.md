# Guide to Using the Git Add, Commit, and Push Script

This bash script automates the process of adding, committing, and pushing changes to multiple Git repositories specified as arguments. It checks if each specified directory is a valid Git repository and performs the operations accordingly.

## Features
- Accepts multiple Git repository paths as arguments.
- Executes `git add .`, `git commit`, and `git push` for each repository.
- Reports success or failure for each operation.

## Usage

### 1. How the Script Works

- The script first checks if at least one argument (repository path) is provided. If not, it displays usage instructions.
- It then iterates through each provided argument and checks if the directory contains a `.git` folder, indicating that it is a valid Git repository.

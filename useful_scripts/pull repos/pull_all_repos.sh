#!/bin/bash

# Directory containing all local repositories
BASE_DIR="/your/base/directory/here"

# Find all directories that contain a .git folder
REPOS=$(find $BASE_DIR -name ".git" | sed 's/\\/\\.git//')

# Run git pull in each repository and print those that were pulled
for REPO in $REPOS; do
  echo "Running git pull in $REPO"
  cd $REPO
  git pull
  if [ $? -eq 0 ]; then
    echo "Successfully pulled $REPO"
  else
    echo "Error pulling $REPO"
  fi
done

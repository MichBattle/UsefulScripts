#!/bin/bash

# Check if arguments were passed
if [ "$#" -lt 1 ]; then
  echo "Usage: $0 repo1 repo2 ... repoN"
  exit 1
fi

# Iterate through each specified repository
for REPO in "$@"; do
  if [ -d "$REPO/.git" ]; then
    echo "Running add, commit, and push in $REPO"
    cd $REPO

    # Execute git add .
    git add .
    if [ $? -eq 0 ]; then
      echo "Add executed successfully for $REPO"
    else
      echo "Error during git add for $REPO"
      cd - # Go back to the starting directory
      continue
    fi

    # Execute git commit -m "push all"
    git commit -m "push all"
    if [ $? -eq 0 ]; then
      echo "Commit executed successfully for $REPO"
    else
      echo "Error during commit for $REPO"
      cd - # Go back to the starting directory
      continue
    fi

    # Execute git push
    git push
    if [ $? -eq 0 ]; then
      echo "Push executed successfully for $REPO"
    else
      echo "Error during push for $REPO"
    fi

    # Go back to the starting directory
    cd -
  else
    echo "Directory $REPO is not a valid git repository"
  fi
done

#!/bin/bash

repository_location="$1"
name_for_repo="repo"

# get student code
if [ -d "$name_for_repo" ]; then
	read -p "Repository already exists; want to delete it? (y/n) " delete_repo

	if [ "$delete_repo" = "y" ]; then
		echo "Deleting repository"
		rm -rf "$name_for_repo"
		echo "Creating new repository"
		git clone "$repository_location" "$name_for_repo"
	else
		# exit with error status
		exit 1
	fi

else
	git clone "$repository_location" "$name_for_repo"
fi

# the tests to perform works with a package
touch "$name_for_repo"/__init__.py

# run tests
pytest

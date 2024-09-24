#!/bin/bash

search_term="Zettelkasten"

# Define the directory to search
directory_to_search="/Users/will/Dropbox/zettelkasten"

# Use find to list all files in the directory (without traversing subdirectories)
# and grep to search for the search term in lines that begin with "Subatomic:"
find "$directory_to_search" -maxdepth 1 -type f -exec grep -H -E "^Subatomic:.*$search_term" {} \;
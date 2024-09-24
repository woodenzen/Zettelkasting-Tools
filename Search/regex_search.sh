#!/bin/bash

# Directory to search
directory="/Users/will/Dropbox/zettelkasten"

# Regex pattern (passed as the first argument to the script)
regex="$1"

# Find and search all .md files in the specified directory only (no subdirectories)
find "$directory" -maxdepth 1 -name "*.md" -exec grep -H -E "$regex" {} \; | while read -r line; do
    file_path=$(echo "$line" | cut -d: -f1)
    file_name=$(basename "$file_path")
    part1=$(echo "$file_name" | rev | cut -c 17- | rev)
    part2=$(echo "$file_name" | rev | cut -c 4-15 | rev)
    echo "$part1 $part2"
done
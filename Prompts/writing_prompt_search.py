import fileinput
from pathlib import Path

def search_term_in_directory(term):
    # define which directory to scan
    p = Path('/Users/will/Dropbox/Projects/Capture DB/')

    # iterate over all .md files in the directory
    for file_path in p.glob('*.md'):
        # select lines that contain the term
        lines = list(fileinput.input(str(file_path)))
        matching_lines = [line for line in lines if term in line]

        # if there are any matching lines, print the file name and the lines
        if matching_lines:
            print(f"## Search results for \"{term}\" in the list of {file_path.stem}.\n")
            for x in matching_lines:
                x = x.replace("\n", "")
                print(f"{x}")
            print("\n")

# Usage
search_term_in_directory('the')
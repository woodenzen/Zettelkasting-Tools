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


def search_term_in_zettelkasten(term):
    # define which directory to scan
    p = Path('/Users/will/Dropbox/zettelkasten/')

    # iterate over all .md files in the directory
    for file_path in p.glob('*.md'):
        # read all lines from the file
        lines = list(fileinput.input(str(file_path)))

        # check if '#collection-list' is in any of the lines
        if any('#collection-list' in line for line in lines):
            # select lines that contain the term
            matching_lines = [line for line in lines if term in line]

            # if there are any matching lines, print the file name and the lines
            if matching_lines:
                print(f"## Search results for \"{term}\" in the list of {file_path.stem[:-13]}.\n")
                for x in matching_lines:
                    x = x.replace("\n", "")
                    print(f"{x}")
                print("\n")

term = 'disagree'
search_term_in_zettelkasten(term)
search_term_in_directory(term)
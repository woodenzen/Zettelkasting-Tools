import fileinput
import os
from pathlib import Path

#TODO - make the search case insensitive
#TODO - test quoted text and multi-word search terms
#TODO - add the ability to search for multiple terms at oncewhere terms only appear on the same line or on different lines
#TODO - setup Keyboard Maestro to run this script with highlighted text as the search term and display the results in a Textedit window

def search_term_in_directories(directories, term):
    term = term.lower()  # convert term to lower case
    for directory in directories:
        p = Path(directory)
        for file_path in p.glob('*.md'):
            lines = list(fileinput.input(str(file_path)))
            matching_lines = [line for line in lines if term in line.lower()]  # convert line to lower case
            if matching_lines:
                print(f"## Search results for \"{term}\" in the list of {file_path.stem}.\n")
                for x in matching_lines:
                    x = x.replace("\n", "")
                    print(f"{x}")
                print("\n")

def search_term_in_zettelkasten(term):
    term = term.lower()  # convert term to lower case
    p = Path('/Users/will/Dropbox/zettelkasten/')
    for file_path in p.glob('*.md'):
        lines = list(fileinput.input(str(file_path)))
        if any('#collection-list' in line for line in lines):
            matching_lines = [line for line in lines if term in line.lower()]  # convert line to lower case
            if matching_lines:
                print(f"## Search results for \"{term}\" in the list of {file_path.stem[:-13]}.\n")
                for x in matching_lines:
                    x = x.replace("\n", "")
                    print(f"{x}")
                print("\n")

# Usage
term = os.environ.get("KMVAR_List_Search_Term", "belly")
directories = [
    '/Users/will/Dropbox/Writing Tools/', 
    '/Users/will/Dropbox/Projects/Capture DB/', 
    '/Users/will/Dropbox/Writing Tools/Better than Great'
]   
search_term_in_zettelkasten(term)
search_term_in_directories(directories, term)

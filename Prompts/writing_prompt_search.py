import fileinput
import os
from pathlib import Path

#TODO - test quoted text and multi-word search terms
#TODO - add the ability to search for multiple terms at oncewhere terms only appear on the same line or on different lines
#TODO - setup Keyboard Maestro to run this script display the results in a Textedit window
#TODO - put a line feed between each search result and 2 between each file search result
#TODO - Report that program couldn't find any results if no results are found

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

def beautiful_language_search(term):
    term = term.lower()  # convert term to lower case
    p = Path('/Users/will/Dropbox/zettelkasten/')
    # results = []  # define an empty list to store the results
    results = {}  # define an empty dictionary to store the results
    for file_path in p.glob('*.md'):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for i in range(len(lines) - 1):  # subtract 1 to avoid IndexError for last line
                if '#beautiful-language' in lines[i]:
                    if term in lines[i + 1]: 
                        x = lines[i + 1].replace("\n", "")
                        if file_path.stem[:-13] in results:
                            results[file_path.stem[:-13]].append(x)
                        else:
                            results[file_path.stem[:-13]] = [x]

    # print the results
    for file, lines in results.items():
        print(f"## Beautiful Language results for \"{term}\" in the file {file}.\n")
        for line in lines:
            print(f"{line}")
        print("\n")
    return results

# Usage
term = os.environ.get("KMVAR_List_Search_Term", "word")
directories = [
    '/Users/will/Dropbox/Writing Tools/', 
    '/Users/will/Dropbox/Projects/Capture DB/', 
    '/Users/will/Dropbox/Writing Tools/Better than Great'
]   
search_term_in_zettelkasten(term)
search_term_in_directories(directories, term)
beautiful_language_search(term)

import fileinput
import os
from pathlib import Path


def search_term_in_directories(directories, terms):
    found = False
    for directory in directories:
        p = Path(directory)
        for file_path in p.glob('*.md'):
            lines = list(fileinput.input(str(file_path)))
            matching_lines = [line for line in lines if all(term.lower() in line.lower() for term in terms)]  # check if all terms are in line
            if matching_lines:
                found = True
                print(f"## Search results for '{' and '.join(terms)}' in the file containing the list of {file_path.stem}.\n")
                for x in matching_lines:
                    x = x.replace("\n", "")
                    print(f"{x}")
                print("\n")
    if not found:
        print(f"### No results were found for '{' and '.join(terms)}' in the Lists.\n")

def search_term_in_zettelkasten(terms):
    p = Path('/Users/will/Dropbox/zettelkasten/')
    found = False
    for file_path in p.glob('*.md'):
        lines = list(fileinput.input(str(file_path)))
        if any('#collection-list' in line for line in lines):
            matching_lines = [line for line in lines if all(term.lower() in line.lower() for term in terms)]  # check if all terms are in line
            if matching_lines:
                found = True
                print(f"## Search results for '{' and '.join(terms)}' in the list\n[{file_path.stem[:-13]}](thearchive://match/›[[{file_path.stem[-12:]}]]).\n")
                for x in matching_lines:
                    x = x.replace("\n", "")
                    print(f"{x}")
                print("\n")
    if not found:
        print(f"### No results were found for '{' and '.join(terms)}' in the Zettelkasten.\n")

def beautiful_language_search(terms):
    p = Path('/Users/will/Dropbox/zettelkasten/')
    results = {}  # define an empty dictionary to store the results
    for file_path in p.glob('*.md'):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for i in range(len(lines) - 1):  # subtract 1 to avoid IndexError for last line
                if '#beautiful-language' in lines[i]:
                    if all(term.lower() in lines[i + 1].lower() for term in terms):  # check if all terms are in line
                        x = lines[i + 1].replace("\n", "")
                        if file_path.stem[:-13] in results:
                            results[file_path.stem[:-13]].append(x)
                        else:
                            results[file_path.stem[:-13]] = [x]

    # print the results
    if results:
        for file, lines in results.items():
            print(f"## Search results for '{' and '.join(terms)}' in the note\n[{file}](thearchive://match/›[[{file_path.stem[-12:]}]]).\n")
            for line in lines:
                print(f"{line}")
            print("\n")
    else:
        print(f"### No Beautiful Language results were found for '{' and '.join(terms)}'.\n")
    return results

# Usage
terms = os.environ.get("KMVAR_List_Search_Term", "word").split()  # split the string into a list of terms
directories = [
    '/Users/will/Dropbox/Writing Tools/', 
    '/Users/will/Dropbox/Projects/Capture DB/', 
    '/Users/will/Dropbox/Writing Tools/Better than Great'
]   
search_term_in_zettelkasten(terms)
search_term_in_directories(directories, terms)
beautiful_language_search(terms)
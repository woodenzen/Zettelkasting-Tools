import os
import re
import pathlib
import fileinput
from TheArchivePath import TheArchivePath

zettelkasten = pathlib.Path(TheArchivePath())
print(zettelkasten)

def search_in_zettelkasten(search_term):
    zettelkasten = pathlib.Path(TheArchivePath())
    results = []

    for file_path in zettelkasten.glob('*.md'):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for i in range(len(lines) - 1):  # subtract 1 to avoid IndexError for last line
                if '#beautiful-language' in lines[i]:
                    if search_term in lines[i + 1]:
                        results.append((str(file_path), lines[i + 1]))

    return results

# Usage
print(search_in_zettelkasten("words"))
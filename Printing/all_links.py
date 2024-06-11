import os
import re
import pathlib
from TheArchivePath import TheArchivePath

zettelkasten = pathlib.Path(TheArchivePath())

def all_links(target):
    links = []
    target_file = None
    for note in os.listdir(zettelkasten):
        if target in note:
            target_file = os.path.join(zettelkasten, note)
            break

    if target_file is not None:
        # Process the target file
        with open(target_file, 'r') as f:
            for line in f:
                matches = re.findall(r'\b\d{12}\b', line)
                links.extend(matches)
    else:
        print(f"No file found with target '{target}'")
    return links

def append_combined_md(links):
    appended_links = set()
    with open('combined.md', 'a') as combined_md_file:
        for i, link in enumerate(links):
            if link not in appended_links:
                for note in os.listdir(zettelkasten):
                    if link in note:
                        with open(os.path.join(zettelkasten, note), 'r') as f:
                            if i != 0:  # Don't prepend separator to the first file
                                combined_md_file.write('\n\n★★★★★\n\n')
                            combined_md_file.write(f.read())
                            appended_links.add(link)
                            break  # Stop searching once the link is found and appended

if __name__ == "__main__":
    # Empty the combined.md file
    with open('./combined.md', 'w') as combined_md_file:
        combined_md_file.write('')
    
    links = all_links('202406072026')
    append_combined_md(links)
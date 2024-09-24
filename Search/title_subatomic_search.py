import os
import pathlib
from plistlib import load
from urllib.parse import urlparse, unquote

def TheArchivePath():
    """
    Find the path to The Archive's plist file.

    Returns:
        A string representing the path to The Archive.
    """
    bundle_id = "de.zettelkasten.TheArchive"
    team_id = "FRMDA3XRGC"
    fileName = os.path.expanduser(
        "~/Library/Group Containers/{0}.{1}.prefs/Library/Preferences/{0}.{1}.prefs.plist".format(team_id, bundle_id))
    with open(fileName, 'rb') as fp:
        pl = load(fp)
        path = urlparse(pl['archiveURL']).path
    return unquote(path)

zettelkasten = pathlib.Path(TheArchivePath())
search_term = " humo".lower()  # Convert search term to lowercase
unique_hits = set()

# Search for the term in filenames and lines starting with "Subatomic:"
for item in os.listdir(zettelkasten):
    if item.endswith('.md'):
        file_path = zettelkasten / item
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.readlines()
                subatomic_line = None
                # Check lines starting with "Subatomic:"
                for line in content:
                    if line.lower().startswith("subatomic:"):  # Convert line to lowercase for comparison
                        subatomic_line = line.strip()
                        if search_term in line.lower():  # Convert line to lowercase for comparison
                            uid = item[-15:-3]
                            truncated_filename = item[:-16]
                            unique_hits.add((truncated_filename, uid, line.strip()))
                # Check if the filename contains the search term
                if search_term in item.lower() and subatomic_line:
                    uid = item[-16:-3]
                    truncated_filename = item[:-16]
                    unique_hits.add((truncated_filename, uid, subatomic_line))
        except Exception as e:
            print(f"Error reading {file_path}: {e}")

# Print the report
if unique_hits:
    for hit in unique_hits:
        print(f"Note Name: {hit[0]}\nUID: [[{hit[1]}]]\n{hit[2]}\n")
else:
    print("No matches found.")
import os
import pathlib
import pandas as pd
import regex as re
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

def parse_boolean_search_term(search_term, near_distance=10):
    """
    Parse the boolean search term into a regex pattern.

    Args:
        search_term (str): The boolean search term.
        near_distance (int): The number of characters to allow between terms for the NEAR operator.

    Returns:
        str: The regex pattern.
    """
    # Replace boolean operators with regex equivalents
    search_term = search_term.replace("AND", ".*")
    search_term = search_term.replace("OR", "|")
    search_term = search_term.replace("NEAR", f".{{0,{near_distance}}}")
    # Replace wildcards with regex equivalents
    search_term = search_term.replace("*", ".*")
    # Add word boundaries to ensure whole word matches
    search_term = r"\b" + search_term + r"\b"
    return search_term

def search_filenames(directory, pattern):
    """
    Search the filenames in the directory for matches.

    Args:
        directory (str): The directory containing the markdown files.
        pattern (str): The regex pattern.

    Returns:
        list: The list of matching filenames.
    """
    matches = []
    for item in os.listdir(directory):
        if item.endswith('.md') and re.search(pattern, item, re.IGNORECASE):
            matches.append(item)
    return matches

def search_file_contents(directory, pattern):
    """
    Search the contents of the files in the directory for matches.

    Args:
        directory (str): The directory containing the markdown files.
        pattern (str): The regex pattern.

    Returns:
        list: The list of tuples containing the filename and the matching line.
    """
    matches = []
    for item in os.listdir(directory):
        if item.endswith('.md'):
            file_path = os.path.join(directory, item)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    for line in file:
                        if re.search(pattern, line, re.IGNORECASE):
                            matches.append((item, line.strip()))  # Append filename and matching line
                            # Uncomment the next line for debugging
                            # print(f"Match found in file: {item}, Line: {line.strip()}")  # Debug statement
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
    return matches

def main():
    # Define the search term and directory
    search_term = "loo* NEAR (notes OR easiest)"
    directory = pathlib.Path(TheArchivePath())

    # Parse the search term into a regex pattern with a custom NEAR distance
    pattern = parse_boolean_search_term(search_term, near_distance=75)
    print(f"Regex Pattern: {pattern}")

    # Search filenames
    filename_matches = search_filenames(directory, pattern)
    print("Filename Matches:")
    for match in filename_matches:
        print(match)

    # Search file contents
    content_matches = search_file_contents(directory, pattern)
    print("\nContent Matches:")
    for match in content_matches:
        print(f"Filename: {match[0]}\nLine: {match[1]}\n")

    # Create DataFrames from the matches
    filename_df = pd.DataFrame({'Filename': filename_matches})
    content_df = pd.DataFrame(content_matches, columns=['Filename', 'Line'])

    # Concatenate the DataFrames
    zk_df = pd.concat([filename_df, content_df], ignore_index=True)

    # Convert the DataFrame to an HTML table with the specified formatters
    html_table = zk_df.to_html(index=False, escape=False, formatters=dict(Filename=lambda x: '<a href="{}">{}</a>'.format(x, x)))
    print(html_table)

if __name__ == "__main__":
    main()
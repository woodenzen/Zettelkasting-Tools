#!/usr/local/bin/python3.9 

import os
from plistlib import load
from urllib.parse import urlparse

def main(zettel):
    def TheArchivePath():
    #  Variables that ultimately revel The Archive's plist file.
        bundle_id = "de.zettelkasten.TheArchive"
        team_id = "FRMDA3XRGC"
        fileName = os.path.expanduser(
            "~/Library/Group Containers/{0}.{1}.prefs/Library/Preferences/{0}.{1}.prefs.plist".format(team_id, bundle_id))
        with open(fileName, 'rb') as fp:
            pl = load(fp) # load is a special function for use with a plist
            path = urlparse(pl['archiveURL']) # 'archiveURL' is the key that pairs with the zk path
        return (path.path) # path is the part of the path that is formatted for use as a path.

    zettelkasten = TheArchivePath()
    blog = "/Users/will/Dropbox/Projects/blog/"
    
    def create_hard_link(source_file, target_directory):
        """
        Create a hard link for the source file in the target directory.

        Args:
            source_file (str): The path to the source file.
            target_directory (str): The path to the target directory.

        Returns:
            None
        """
        # Get the file name from the source file path
        source_file = zettelkasten + zettel+".md"
        # Construct the target file path
        target_file = os.path.join(blog, zettel+".md")
        
        try:
            # Create the hard link
            os.link(source_file, target_file)
            print(f"Hard link created: {target_file}")
        except FileExistsError:
            print(f"Hard link already exists: {target_file}")
        except Exception as e:
            print(f"Error creating hard link: {e}")

if __name__ == "__main__":
    # Print all environment variables for debugging
    print("Environment Variables:")
    for key, value in os.environ.items():
        print(f"{key}: {value}")
    
    target = os.environ.get("KMVAR_target")
    if target:
        main(target)
    else:
        print("No target provided in 'KMVAR_target'")
        exit(1)


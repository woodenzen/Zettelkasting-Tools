import os
import logging
import subprocess
from urllib.parse import urlparse
from plistlib import load

def TheArchivePath():
    """
    Find the path to The Archive's plist file.

    Returns:
        str: The path to The Archive.
    """
    bundle_id = "de.zettelkasten.TheArchive"
    team_id = "FRMDA3XRGC"
    fileName = os.path.expanduser(
        "~/Library/Group Containers/{0}.{1}.prefs/Library/Preferences/{0}.{1}.prefs.plist".format(team_id, bundle_id))
    with open(fileName, 'rb') as fp:
        pl = load(fp)  # load is a special function for use with a plist
        path = urlparse(pl['archiveURL'])  # 'archiveURL' is the key that pairs with the zk path
    return path.path  # path is the part of the path that is formatted for use as a path.

zettelkasten = TheArchivePath()
blog = "/Users/will/Dropbox/Projects/blog/"

# Configure logging to console
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_hard_link(source, target_directory):
    """
    Create a hard link for the source file in the target directory.

    Args:
        source_file (str): The path to the source file.
        target_directory (str): The path to the target directory.

    Returns:
        None
    """
    # Get the file name from the source file path
    file_name = os.path.basename(source)
    # Remove the timestamp from the file name
    base_name = file_name.rsplit(' ', 1)[0] + '.md'
    # Construct the target file path
    target_file = os.path.join(target_directory, base_name)
    
    # Debugging statements to print the paths
    logging.info(f"Source file: {source}")
    logging.info(f"Target file: {target_file}")
    
    try:
        # Create the hard link
        os.link(source, target_file)
        logging.info(f"Hard link created: {target_file}")
    except FileExistsError:
        logging.warning(f"Hard link already exists: {target_file}")
    except Exception as e:
        logging.error(f"Error creating hard link: {e}")


def sync_to_github(blog_dir):
    """
    Sync the blog directory to GitHub.

    Args:
        blog_dir (str): The path to the blog directory.

    Returns:
        None
    """
    try:
        # Run git status
        result = subprocess.run(
            ['git', 'status'], cwd=blog_dir, capture_output=True, text=True
        )
        logging.info(f"Git status: {result.stdout.strip()}")

        # Run git add .
        subprocess.run(['git', 'add', '.'], cwd=blog_dir, capture_output=True, text=True)
        logging.info("Files staged")

        # Run git commit (don't fail if nothing to commit)
        result = subprocess.run(
            ['git', 'commit', '-m', 'Add new notes.'], 
            cwd=blog_dir, capture_output=True, text=True
        )
        if result.returncode == 0:
            logging.info("Changes committed")
        else:
            logging.info(f"Commit skipped: {result.stdout.strip()}")

        # Run git push
        result = subprocess.run(
            ['git', 'push'], cwd=blog_dir, capture_output=True, text=True
        )
        if result.returncode == 0:
            logging.info("Changes pushed to GitHub")
        else:
            logging.error(f"Push failed: {result.stderr}")

    except Exception as e:
        logging.error(f"Error syncing to GitHub: {e}")

if __name__ == "__main__":
    # Retrieve the file name from the environment variable set by Keyboard Maestro
    source = os.environ.get('KMVAR_baseName')
    
    if source:
        # Create the hard link in the blog directory
        create_hard_link(source, blog)
        # Sync the blog directory to GitHub
        sync_to_github(blog)
    else:
        logging.error("No file name provided in 'KMVAR_baseName'")
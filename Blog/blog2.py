import os
import logging
import subprocess
import shutil
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
log_log = "/Users/will/Dropbox/Projects/Zettelkasting Tools/Blog/link.log"

# Configure logging to file
logging.basicConfig(filename=log_log, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_hard_link(source, target_directory):
    """
    Create a hard link for the source file in the target directory.

    Args:
        source (str): The source file name.
        target_directory (str): The path to the target directory.

    Returns:
        str: The path to the source Markdown file.
    """
    # Ensure target directory exists
    os.makedirs(target_directory, exist_ok=True)
    
    # Get the file name from the source file path
    file_name = os.path.basename(source)
    # Remove the timestamp from the file name
    base_name = file_name.rsplit(' ', 1)[0] + '.md'
    # Construct the target file path
    target_file = os.path.join(target_directory, base_name)
    # Construct the full source path by joining with zettelkasten directory
    source_file = os.path.join(zettelkasten, file_name)
    
    # Debugging statements to print the paths
    logging.info(f"Source file: {source_file}")
    logging.info(f"Target file: {target_file}")
    
    try:
        # Create the hard link
        os.link(source_file, target_file)
        logging.info(f"Hard link created: {target_file}")
    except FileExistsError:
        logging.warning(f"Hard link already exists: {target_file}")
    except Exception as e:
        logging.error(f"Error creating hard link: {e}")
    return source_file


def copy_media_files(source_file, target_directory):
    """
    Copy media files referenced by the source Markdown file to the blog media directory.

    Args:
        source_file (str): The path to the source Markdown file.
        target_directory (str): The path to the blog directory.

    Returns:
        None
    """
    media_prefix = "![](media/"
    source_directory = os.path.dirname(source_file)
    target_media_directory = os.path.join(target_directory, "media")
    copied_count = 0

    logging.info(f"Scanning for media references in: {source_file}")

    try:
        with open(source_file, "r", encoding="utf-8") as fp:
            for line_number, line in enumerate(fp, start=1):
                line = line.rstrip()
                if not line.startswith(media_prefix):
                    continue

                media_path = line[len("![]("):].split(")", 1)[0]
                normalized_media_path = os.path.normpath(media_path)

                if (
                    os.path.isabs(normalized_media_path)
                    or normalized_media_path.startswith("..")
                    or not normalized_media_path.startswith(f"media{os.sep}")
                ):
                    logging.warning(
                        f"Skipping unsafe media path on line {line_number}: {media_path}"
                    )
                    continue

                source_media_file = os.path.join(source_directory, normalized_media_path)
                target_media_file = os.path.join(target_directory, normalized_media_path)

                if not os.path.isfile(source_media_file):
                    logging.error(
                        f"Media file not found on line {line_number}: {source_media_file}"
                    )
                    continue

                os.makedirs(os.path.dirname(target_media_file), exist_ok=True)
                shutil.copy2(source_media_file, target_media_file)
                copied_count += 1
                logging.info(f"Copied media file: {source_media_file} -> {target_media_file}")

        logging.info(f"Media scan complete. Copied {copied_count} file(s) to {target_media_directory}")
    except Exception as e:
        logging.error(f"Error copying media files from {source_file}: {e}")


def sync_to_github(blog_dir):
    """
    Sync the blog directory to GitHub.

    Args:
        blog_dir (str): The path to the blog directory.

    Returns:
        None
    """
    logging.info(f"Starting GitHub sync for: {blog_dir}")
    
    # Check if directory is a git repository
    git_dir = os.path.join(blog_dir, '.git')
    if not os.path.isdir(git_dir):
        logging.error(f"Not a git repository: {blog_dir}")
        return
    
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
    try:
        logging.info("=== Script started ===")
        
        # Retrieve the file name from the environment variable set by Keyboard Maestro
        source = os.environ.get('KMVAR_baseName')
        
        logging.info(f"KMVAR_baseName raw: {repr(source)}")
        
        if source:
            # Strip any trailing whitespace/newlines
            source = source.strip()
            logging.info(f"Received file: {source}")
            # Create the hard link in the blog directory
            source_file = create_hard_link(source, blog)
            # Copy media referenced in the source file before syncing to GitHub
            copy_media_files(source_file, blog)
            # Sync the blog directory to GitHub
            logging.info("Calling sync_to_github...")
            sync_to_github(blog)
            logging.info("=== Script completed ===")
        else:
            logging.error("No file name provided in 'KMVAR_baseName'")
            logging.error("Environment variables received:")
            for key, value in os.environ.items():
                if 'KMVAR' in key:
                    logging.error(f"  {key}: {repr(value)}")
    except Exception as e:
        # Last resort error capture
        logging.error(f"Fatal error: {e}")
        import traceback
        logging.error(traceback.format_exc())

import os
import logging

log_log = "/Users/will/Dropbox/Projects/Zettelkasting Tools/tests/link.log"

# Configure logging to file
logging.basicConfig(filename=log_log, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

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
    file_name = os.path.basename(source_file)
    # Construct the target file path
    target_file = os.path.join(target_directory, file_name)
    
    try:
        # Create the hard link
        os.link(source_file, target_file)
        logging.info(f"Hard link created: {target_file}")
    except FileExistsError:
        logging.warning(f"Hard link already exists: {target_file}")
    except Exception as e:
        logging.error(f"Error creating hard link: {e}")

if __name__ == "__main__":
    # Print all environment variables for debugging
    logging.info("Environment Variables:")
    for key, value in os.environ.items():
        logging.debug(f"{key}: {value}")
    
    # Retrieve the file name from the environment variable set by Keyboard Maestro
    # source_file = os.environ.get("KMVAR_fileName")
    source_file = "/Users/will/Dropbox/zettelkasten/Pitch Cover Letter 202411231914.md"
    
    if source_file:
        logging.info(f"Source file: {source_file}")
        # Define the target directory
        target_directory = '/Users/will/Dropbox/Projects/blog'
        # Create the hard link
        create_hard_link(source_file, target_directory)
    else:
        logging.error("No file name provided in 'KMVAR_FileName'")
        exit(1)
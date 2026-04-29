import os

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
    
    # Retrieve the file name from the environment variable set by Keyboard Maestro
    # source_file = os.environ.get("KMVAR_fileName")
    source_file = "/Users/will/Dropbox/zettelkasten/Pitch Cover Letter 202411231914.md"
    
    if source_file:
        print(f"KMVAR_FileName: {source_file}")
        # Define the target directory
        target_directory = '/Users/will/Dropbox/Projects/blog'
        # Create the hard link
        create_hard_link(source_file, target_directory)
    else:
        print("No file name provided in 'KMVAR_FileName'")
        exit(1)
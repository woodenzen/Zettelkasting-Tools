import os

def check_utf8_in_directory(directory):
    """
    Check if all files in the specified directory contain valid UTF-8 characters.

    Args:
        directory (str): The path to the directory.
    """
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as f:
                content = f.read()
            try:
                content.decode('utf-8')
                print(f"All characters in {filename} are valid UTF-8")
            except UnicodeDecodeError as e:
                print(f"Non-UTF-8 character found in {filename}: {e}")

# Example usage
directory_path = '/Users/will/Dropbox/Projects/Write-Right-Journal/assets/js'
check_utf8_in_directory(directory_path)
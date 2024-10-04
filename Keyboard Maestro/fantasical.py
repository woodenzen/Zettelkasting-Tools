import os

def remove_blank_lines(text):
    """
    Remove blank lines from the given text.
    
    Args:
        text (str): The input text.
    
    Returns:
        str: The text with blank lines removed.
    """
    lines = text.split('\n')
    non_blank_lines = [line for line in lines if line.strip() != '']
    return '\n'.join(non_blank_lines)

def remove_lines_containing(text, substring):
    """
    Remove lines containing a specific substring from the given text.
    
    Args:
        text (str): The input text.
        substring (str): The substring to search for in lines.
    
    Returns:
        str: The text with lines containing the substring removed.
    """
    lines = text.split('\n')
    filtered_lines = [line for line in lines if substring not in line]
    return '\n'.join(filtered_lines)

if __name__ == "__main__":
    # Retrieve the 'schedule' Keyboard Maestro variable
    input_text = os.environ.get('KMVAR_schedule')
    
    if input_text:
        # Remove blank lines
        cleaned_text = remove_blank_lines(input_text)
        # Remove lines containing 'all-day'
        cleaned_text = remove_lines_containing(cleaned_text, 'all-day')
        print(cleaned_text)
    else:
        print("No input text found in 'KMVAR_schedule'")
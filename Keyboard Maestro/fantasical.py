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

def reformat_first_line(text):
    """
    Reformat the first line of the text by replacing it with "----".
    
    Args:
        text (str): The input text.
    
    Returns:
        str: The text with the first line reformatted.
    """
    lines = text.split('\n')
    if lines:
        lines[0] = "----"
    return '\n'.join(lines)

def prepend_to_lines(text, prefix, starts_with):
    """
    Prepend a prefix to lines that start with a specific substring.
    
    Args:
        text (str): The input text.
        prefix (str): The prefix to prepend.
        starts_with (str): The substring that lines should start with to have the prefix prepended.
    
    Returns:
        str: The text with the prefix prepended to matching lines.
    """
    lines = text.split('\n')
    modified_lines = [f"{prefix}{line}" if line.startswith(starts_with) else line for line in lines]
    return '\n'.join(modified_lines)

if __name__ == "__main__":
    # Retrieve the 'schedule' Keyboard Maestro variable
    input_text = os.environ.get('KMVAR_schedule')
    
    if input_text:
        # Remove blank lines
        cleaned_text = remove_blank_lines(input_text)
        # Remove lines containing 'all-day'
        cleaned_text = remove_lines_containing(cleaned_text, 'all-day')
        # Reformat the first line
        cleaned_text = reformat_first_line(cleaned_text)
        # Prepend "- " to lines starting with "[ ] "
        cleaned_text = prepend_to_lines(cleaned_text, "- ", "[ ] ")
        print(cleaned_text)
    else:
        print("No input text found in 'KMVAR_schedule'")
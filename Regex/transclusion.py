import re

def find_lines_with_12_digit_number(text):
    """
    Find lines containing a 12-digit number in the given text, excluding lines that start with "UUID".

    Args:
        text (str): The input text.

    Returns:
        list: A list of lines containing a 12-digit number, excluding lines that start with "UUID".
    """
    # Regex pattern to find lines with a 12-digit number
    pattern = r'.*\b\d{12}\b.*'
    # Find all lines with a 12-digit number
    lines_with_12_digit_number = re.findall(pattern, text, re.MULTILINE)
    # Filter out lines that start with "UUID"
    filtered_lines = [line for line in lines_with_12_digit_number if not line.startswith("UUID")]
    # Remove "- ", "[[", and "]]" from each line
    cleaned_lines = [line.replace("- ", "").replace("[[", "").replace("]]", "") for line in filtered_lines]
    return cleaned_lines

# Read the markdown file
with open('/Users/will/Dropbox/zettelkasten/Transclusion Template 202410300516.md', 'r') as file:
    markdown_text = file.read()

# Find lines with a 12-digit number in the text
lines_with_12_digit_number = find_lines_with_12_digit_number(markdown_text)

# Print the found lines
for line in lines_with_12_digit_number:
    print(line)
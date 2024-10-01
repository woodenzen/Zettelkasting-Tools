import os

def remove_blank_lines(text):
    lines = text.split('\n')
    non_blank_lines = [line for line in lines if line.strip() != '']
    return '\n'.join(non_blank_lines)

if __name__ == "__main__":
    # Retrieve the 'schedule' Keyboard Maestro variable
    input_text = os.environ.get('KMVAR_schedule')
    print(remove_blank_lines(input_text))

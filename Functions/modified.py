import os
import datetime

def count_modified_md_files(directory):
    ten_days_ago = datetime.datetime.now() - datetime.timedelta(days=10)
    counter = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                mod_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
                if mod_time > ten_days_ago:
                    counter += 1

    return counter

if __name__ == '__main__':
    directory = '/Users/will/Dropbox/zettelkasten/'
    print(count_modified_md_files(directory))
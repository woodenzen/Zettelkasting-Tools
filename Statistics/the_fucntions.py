

'''
`User Setting Section
``'''
path = "/Users/will/Dropbox/zettelkasten/"
table_output = "table.txt"

'''
look for every file with a date in the name
'''

def get_files(year):
    files = []
    count = 0
    for file in os.listdir(path):
        pattern = str(year) + r'\d{8}'
        if re.search(pattern, file):
            files.append(file)
            count += 1
    return files, count

'''
look in every file for the links
'''

def get_links(year, link):
    count = 0
    results = get_files(year)
    for file in results[0]:
        with open(path + file, 'r') as f:
            for line in f:
                if link in line:
                    count += 1
    return count

'''
count words in every file by year
'''

def get_words(year):
    count = 0
    results = get_files(year)
    for file in results[0]:
        with open(path + file, 'r') as f:
            for line in f:
                count += len(line.split())
    return count

'''
Get the last year needed to make a complete chart
'''

def next_year():
    today = datetime.date.today()
    year = today.year + 1
    return year


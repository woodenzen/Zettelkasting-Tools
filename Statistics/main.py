#!/usr/bin/env python3

import os
import re
import datetime
from tabulate import tabulate


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



if __name__ == "__main__":  
    
    # This is where all the logic happens. First, we get the earliest year and set annual to an empty list.
    earliest_input = input("Earliest year: ")
    earliest = int(earliest_input)
    annual = []
    
    # We iterate through the years, starting with the earliest year and ending with the current year. We return all the values we need for each year and append them to the annual list.
    for year in range(earliest,next_year()):
        results = get_files(year)
        annual.append([year, results[1], get_links(year, '[[20'), get_words(year)])      
         
# save the table to a file using tabulate
table = tabulate([*annual], 
                 headers=["Year", "Notes", "Links", "Words"], 
                 tablefmt='fancy_grid', 
                 missingval='N/A')

# use context manager to create table.txt file and write table to it
with open(table_output, 'w') as f:
  f.write(table)
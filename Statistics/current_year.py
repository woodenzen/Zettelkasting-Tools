#!/usr/bin/env python3

import os
import re
import datetime
from tabulate import tabulate


# User Setting Section

path = "/Users/will/Dropbox/zettelkasten/"
table_output = "table.txt"

# Get the current year
current_year = datetime.datetime.now().year

# Create a dictionary to store the count of files for each month
file_count_by_month = {}

# Iterate over the files in the directory
for filename in os.listdir(path):
    if filename.endswith(".md"):
        # Get the creation time of the file
        # Extract the last 12 digits before the '.md' from the filename
        timestamp_str = filename[:-3][-12:]

        # Parse the year and month from the extracted digits
        year = int(timestamp_str[:4])
        month = int(timestamp_str[4:6])

        # Create a datetime object from the parsed year and month
        creation_date = datetime.datetime(year, month, 1)

        # Check if the file was created in the current year
        current_year = datetime.datetime.now().year
        if creation_date.year == current_year:
            # Set the month to the parsed month
            month = creation_date.strftime("%B")
            
            # Increment the count for the month in the dictionary
            file_count_by_month[month] = file_count_by_month.get(month, 0) + 1

# Sort the dictionary by month
sorted_file_count_by_month = sorted(file_count_by_month.items(), key=lambda x: datetime.datetime.strptime(x[0], "%B"))

# Print the table
table = tabulate(sorted_file_count_by_month, headers=["Month", "Number Created"], tablefmt="grid")
print(table)

# Print the total for the current year
total = sum(file_count_by_month.values())
print(f"Total for {current_year} so far: {total}")
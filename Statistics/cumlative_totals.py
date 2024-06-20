import os
import datetime
from tabulate import tabulate
import csv

# Initialize the dictionary to store the file count by month and word count
file_count_by_month = {}
word_count_by_month = {}
cumulative_totals = {}
cumulative_word_totals = {}
zettelkasten = "/Users/will/Dropbox/zettelkasten/"

# Get the current year
current_year = datetime.datetime.now().year

# Iterate over all files in the zettelkasten directory
for filename in os.listdir(zettelkasten):
    if filename.endswith('.md'):
        # Extract the last 12 digits before the '.md' from the filename
        timestamp_str = filename[:-3][-12:]

        # Parse the year and month from the extracted digits
        year = int(timestamp_str[:4])
        month = int(timestamp_str[4:6])

        # Check if the file was created since January 2018
        if year >= 2018 and (year > 2018 or month >= 1):
            # Increment the count for the month in the dictionary
            file_count_by_month[(year, month)] = file_count_by_month.get((year, month), 0) + 1

            # Count the words in the file
            with open(os.path.join(zettelkasten, filename), 'r') as f:
                words = f.read().split()
                word_count_by_month[(year, month)] = word_count_by_month.get((year, month), 0) + len(words)

# Calculate the cumulative totals
sorted_months = sorted(file_count_by_month.keys())
for i, (year, month) in enumerate(sorted_months):
    cumulative_totals[(year, month)] = file_count_by_month[(year, month)] + (cumulative_totals[sorted_months[i-1]] if i > 0 else 0)
    cumulative_word_totals[(year, month)] = word_count_by_month[(year, month)] + (cumulative_word_totals[sorted_months[i-1]] if i > 0 else 0)

# Prepare the data for the table
table_data = [(f"{datetime.date(year, month, 1):%B %Y}", cumulative_totals[(year, month)], cumulative_word_totals[(year, month)]) for year, month in sorted_months if year == current_year]

# Print the table
print(tabulate(table_data, headers=["Month", "Cumulative Total", "Cumulative Word Count"], tablefmt="grid"))
# Specify the output file path
output_file = "/Users/will/Dropbox/Projects/zettel_stats/annual_stats/cumulative_totals.csv"

# Prepare the data for the CSV
csv_data = [("Month", "Cumulative Total", "Cumulative Word Count")]
csv_data.extend(table_data)

# Write the data to the CSV file
with open(output_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(csv_data)

# Print a success message
print(f"Table successfully exported to {output_file}")
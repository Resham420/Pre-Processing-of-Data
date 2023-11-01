import csv
import gspread
import re

# Open the CSV file
with open('Originally.csv', 'r') as csv_file:
    # Create a CSV reader object
    csv_reader = csv.reader(csv_file)

    # Specify the column index you want to pick
    column_index = 8  # Replace with the desired column index (starting from 0)

    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Access the value at the specified column index
        if len(row) > column_index:
            value = row[column_index]
            # Use regular expression partial match and replace
            regex_replacements = [
                (r'SBKWU|Sardar Bahadur khan women university Quetta Balochistan|Sardar Bahadur khan womens university Quetta', 'SBK'),
                (r'IUB|University of balochistan|UOB, Quetta.|UOB Quetta|Business administration|University|Student', 'UOB'),
                (r'Buitems', 'BUITEMS')
            ]
            for pattern, replacement in regex_replacements:
                value = re.sub(pattern, replacement, value)

            print(value)

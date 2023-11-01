import csv
import re

# Open the CSV file
input_filename = 'processed_data.csv'
output_filename = 'Updated.csv'

# Create a CSV reader object
with open(input_filename, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    data = list(csv_reader)

# Specify the column index you want to pick
column_index = 10  # Replace with the desired column index (starting from 0)

# Define the regular expression replacements
regex_replacements = [
    (r'Computer science|Computer Science|computer science|Cs|I.T|IT|CS|BSCS|BS IT', 'CS&IT'),
    (r'Pharma d|Phamra D|pharma d|pharmacy', 'Pharmacy'),
    (r'bio chemistry|biochemistry', 'Biochemistry')
]

# Create a new column name for the updated data
new_column_name = 'Updated_Column'

# Iterate over each row and update the specified column
for row in data:
    if len(row) > column_index:
        value = row[column_index]

        # Apply regular expression replacements
        for pattern, replacement in regex_replacements:
            value = re.sub(pattern, replacement, value)

        # Add the updated value to a new column
        row.append(value)

# Save the updated data to the same CSV file with a new column
with open(output_filename, 'w', newline='') as output_file:
    csv_writer = csv.writer(output_file)
    csv_writer.writerows(data)

# Print the result
for row in data:
    print(','.join(row))  # Assuming a CSV format with comma-separated values

print(f"Updated data saved to '{output_filename}'.")

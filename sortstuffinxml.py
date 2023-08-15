import pandas as pd

# Load the Excel file
df = pd.read_excel('totalsize.xlsx')

# Sort the data by roll numbers
sorted_df = df.sort_values(by='Enrollment-No')

# Save the sorted data to a new Excel file
sorted_df.to_excel('sorted_data.xlsx', index=False)

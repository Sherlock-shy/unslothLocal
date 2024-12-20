import pandas as pd
import json

# Load Excel file
file_path = 'xlsx'  # Replace with your file path
df = pd.read_excel(file_path)

# Assuming the Excel has two columns named 'instruction' and 'response'
# Adjust the column names and structure if they are different
data_list = [{"instruction": row['instruction'], "response": row['response']} for _, row in df.iterrows()]

# Convert to JSON format without using \u-encoded sequences
json_data = json.dumps(data_list, indent=2, ensure_ascii=False)

# Write JSON data to a file
with open('output.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_data)

print("Conversion complete. JSON data saved to 'output.json'.")

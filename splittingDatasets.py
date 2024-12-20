#spliting of datasets, modifiy with your datasets structure
import json
from sklearn.model_selection import train_test_split

# Load the multi-turn dataset
input_file = "path_to_datasets.json"
with open(input_file, "r", encoding="utf-8") as file:
    data = json.load(file)

# Count total conversations and display
total_conversations = len(data)
print(f"Total number of conversations: {total_conversations}")

# Split the data into train (70%), validation (15%), and test (15%) sets
train_data, temp_data = train_test_split(data, test_size=0.3, random_state=42)
val_data, test_data = train_test_split(temp_data, test_size=0.5, random_state=42)

# Define output paths
train_file = "your output paths for training datasets"
val_file = "your output path for validation datasets"
test_file = "your output path for testing datasets"

# Save each split without encoding special characters
with open(train_file, "w", encoding="utf-8") as file:
    json.dump(train_data, file, ensure_ascii=False, indent=2)
with open(val_file, "w", encoding="utf-8") as file:
    json.dump(val_data, file, ensure_ascii=False, indent=2)
with open(test_file, "w", encoding="utf-8") as file:
    json.dump(test_data, file, ensure_ascii=False, indent=2)

# Output the sizes of each split
print(f"Training set: {len(train_data)} conversations")
print(f"Validation set: {len(val_data)} conversations")
print(f"Test set: {len(test_data)} conversations")

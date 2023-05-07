import json

# Open the JSON file
with open("config.json", "r") as input_file:
    input_data = json.load(input_file)

# Function to convert decimal values to hexadecimal values
def convert_dec_to_hex(data):
    if isinstance(data, dict):
        # If the value is a dictionary, recursively convert its values
        return {key: convert_dec_to_hex(value) for key, value in data.items()}
    elif isinstance(data, list):
        # If the value is a list, recursively convert its values
        return [convert_dec_to_hex(value) for value in data]
    elif isinstance(data, int):
        # If the value is a decimal integer, convert it to hexadecimal
        return hex(data)[2:].upper()
    else:
        # If the value is not a dictionary, list, or decimal integer, return it unchanged
        return data

# Convert decimal values to hexadecimal values
output_data = convert_dec_to_hex(input_data)

# Write to a new file
with open("config.txt", "w") as output_file:
    json.dump(output_data, output_file, indent=4)
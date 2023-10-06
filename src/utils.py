import re
import json
import os

def append_or_create_json_file(file_path, data_dict):
    if os.path.exists(file_path):
        # If the file exists, load its contents
        with open(file_path, 'r') as file:
            existing_data = json.load(file)

        # Append the new data to the existing dictionary
        existing_data.update(data_dict)

        # Write the updated data back to the file
        with open(file_path, 'w') as file:
            json.dump(existing_data, file)
    else:
        # If the file doesn't exist, create it with the provided dictionary
        with open(file_path, 'w') as file:
            json.dump(data_dict, file)


def extract_list_of_lists(input_string):
    # Define a regular expression pattern to match the list of lists
    outer_pattern = r'\[\[.*?\]\]'
    inner_pattern = r'\[.*?\]'

    # Find all matches of the pattern in the input string
    matches = re.findall(outer_pattern, input_string)

    # Initialize an empty list to store the extracted lists
    extracted_lists = []

    # Loop through the matches and convert them to actual lists
    for match in matches:
        # Remove the square brackets and split by commas to get individual strings
        inner_strings = re.findall(inner_pattern, match[1:-1])
        # Strip leading and trailing spaces from each inner string
        inner_strings = [s.strip() for s in inner_strings]

        # Append the inner strings as a list to the result
        for string in inner_strings:
            extracted_lists.append(string)

    return extracted_lists


def save_text(text, path):
    try:
        with open(path, 'w') as file:
            file.write(text)
        return True  # Success
    except Exception as e:
        return str(e)  # Return the error message if an exception occurs
    
    
def read_text_file(file_path):
    """
    Opens and returns the content of a text file.
    
    Args:
    file_path (str): The path to the text file.

    Returns:
    str: The content of the text file as a string.
    """
    with open(file_path, 'r') as file:
        text_content = file.read()
    return text_content
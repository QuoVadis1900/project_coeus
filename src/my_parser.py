import re

def extract_list_of_lists(input_string):
    # Define a regular expression pattern to match the list of lists
    pattern = r'\[\[.*?\]\]'
    
    # Find all matches of the pattern in the input string
    matches = re.findall(pattern, input_string)
    
    # Initialize an empty list to store the extracted lists
    extracted_lists = []
    
    # Loop through the matches and convert them to actual lists
    for match in matches:
        # Remove the square brackets and split by commas to get individual strings
        inner_strings = match[2:-2].split(',')
        
        # Strip leading and trailing spaces from each inner string
        inner_strings = [s.strip() for s in inner_strings]
        
        # Append the inner strings as a list to the result
        extracted_lists.append(inner_strings)
    
    return extracted_lists

if __name__ == "__main__":
    # Example usage:
    input_string = "Some text before [[string1, string2], [string3, string4]] and some text after."
    result = extract_list_of_lists(input_string)
    print(result)

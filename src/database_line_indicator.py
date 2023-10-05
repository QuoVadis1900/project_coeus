import os

# Function to add line numbers to each line in a file
def add_line_numbers(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line_number, line in enumerate(infile, start=1):
            outfile.write(f"(ln: {line_number}) {line}")

# Specify the input and output folder paths
input_folder = './Database'
output_folder = './Line_Number_Database'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# List all .txt files in the input folder
txt_files = [f for f in os.listdir(input_folder) if f.endswith('.txt')]

# Process each .txt file
for txt_file in txt_files:
    input_file_path = os.path.join(input_folder, txt_file)
    output_file_path = os.path.join(output_folder, txt_file)
    add_line_numbers(input_file_path, output_file_path)

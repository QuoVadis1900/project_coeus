from my_parser import extract_list_of_lists

def make_question_prompt(text, question):
    prompt = f"""
Given the following text with line specifications:
"
{text}
".
Return all important information about the question 
"
{question}
", including line specifications. Only answer with the relevant information, be as concise and short as possible, without loosing relevant information. You don't have to answer the question, only find relevant information.
"""
    return prompt

def make_question_parsing_prompt(summary):
    parser_command = f"""
Text file:
"{summary}"
"
Reformat the text file in the following list format:
[[line specification, information1], [line specification, information2]...]. Do not comment in any way. Strictly response with the list.
"""
    return parser_command

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

    
if __name__ == "__main__":
    #TODO Automatically read all files from the input Database, iterate over them.
    """
    Setup paths and input text file name
    """
    prompt_path = "./prompts/summary_prompt"
    parser_path = "./prompts/parser_prompt"
    response_path = "./response/first_response"
    parsed_response_path = "./response/parsed_response"
    final_result_path = "./response/final_result"
    database_path = "./Line_Number_Database/"
    text_name = "text1.txt"
    text = read_text_file(database_path + text_name)


    question = "How old is Peter?"

    """
    Make prompt, save it to the prompt path. 
    Copy the text from the prompt path file and copy the response from the LLM into the response_path file.
    """
    prompt = make_question_prompt(text=text, question=question)
    save_text(text=prompt, path=prompt_path)
    input("Press Enter after you pasted the response into ./response/first_response...")
    
    response = read_text_file(file_path=response_path)
    parser_command = make_question_parsing_prompt(response)
    save_text(text=parser_command, path=parser_path)
    input("Press Enter after you pasted the parsed response into ./response/parsed_response...")

    #TODO Combine all parsed responses into one file
    parsed_summary = read_text_file(parsed_response_path)
    #TODO Input file with all parsed responses into the LLM and ask it to produce the actual final answer
    string_list = extract_list_of_lists(parsed_summary)
    print(string_list)
    results = {text_name:string_list}
    save_text(text=str(results), path=final_result_path)
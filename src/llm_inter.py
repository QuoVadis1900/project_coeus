def make_question_prompt(text, question):
    prompt = f"""
Given the following text with line specifications:
"{text}". Return all important information about the question 
"{question}", including line specifications.
"""
    return prompt

def make_question_parsing_prompt(summary):
    parser_command = f"""
Summary of document with respective line specification:
"{summary}".
Reformat the summary in the following list format:
[[line specification, information1], [line specification, information2]...]. If the document states, that there are no important information, return  [[]]."""
    return parser_command

def make_summary_prompt(text, question):
    prompt = f"""
Following are findings from different documents with respect to a specific question "How old is Peter?". The format is [text name: [[line specification, information1], [line specification, information2], ...\, text name 2:[...], ...].
Summarize the findings and try to answer the question. Include the name of the text and the respective line specifications that included the used information for the summary.
Summary: {text}
Question: {question}
"""
    return prompt

def make_summary_parsing_prompt(summary, question):
    prompt = f"""
Summarize the following text with respect to the question {question}. Include the used document names and line specifications: 
{summary}"""
    return prompt
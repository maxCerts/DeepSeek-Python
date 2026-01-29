import ollama
import ast

def parse_python_code(file_path):
    with open(file_path, "r") as file:
        code = file.read()
        parsed_code = ast.parse(code)
        return parsed_code

def generate_documentation(parsed_code):
    code_str = ast.dump(parsed_code, annotate_fields=False)
    response = ollama.chat(
    model = "deepseek-r1:8b",
    messages = [{
        "role": "user",
        "content": f"Generate documentation for the following Python code:{code_str}",
    }]
    )
    documentation = response["message"]["content"]
    return documentation

def save_documentation(file_path,documentation):
    with open(file_path, "w") as file:
        file.write(documentation)

python_code = """
def add_numbers(a, b):
\"""This function adds two numbers and returns the result.
Parameters:
a (int): The first number.
b (int): The second number.
Returns:
int: The sum of a and b
\"""
return a + b
"""

file_path = 'generated_documentation.py'
with open(file_path, "w") as file:
    file.write(python_code)

parsed_code = parse_python_code(file_path)
documentation = generate_documentation(parsed_code)
print("Generated documentation:\n",documentation)
save_documentation(file_path,documentation)
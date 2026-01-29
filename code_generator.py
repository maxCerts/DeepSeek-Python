import ollama

def generate_python_code(task_description):
    """
    Uses deepseek coder to generate python code for a given task.
    Example: generate_python_code("Calculate factorial of a number")
    """

    prompt = f""" Write a python function to {task_description}
    Include docstring and example usage. """

    response = ollama.generate(
        model= "deepseek-r1:8b",
        prompt = prompt,
        options = {"temperature":0.3}
    )
    return response["response"]

print(generate_python_code("Calculate factorial of a number"))
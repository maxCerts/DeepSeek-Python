import ollama

def auto_debugger(code:str) -> str:
    """
    Sends broken Python code to DeepSeeks and gets a fixed version with explanation
    """

    response = ollama.generate(
        model= "deepseek-r1:1b",
        prompt = f"Fix this pythond code and explan it:\n\n{code}",
        options = {"temperature":0.3}
    )
    return response["response"]

broken_code = '''
def calculate_average(numbers):
     total = sum(numbers)
     return total / len(number)
'''

print(auto_debugger(broken_code))
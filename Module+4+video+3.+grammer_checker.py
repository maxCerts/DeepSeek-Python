import ollama

def correct_grammar(text):
    prompt = f"Fix the grammar in the following sentence and explain the correction:\n\n{text}"

    response = ollama.generate(
        model = "deepseek-r1:8b",
        prompt = prompt,
        options = {"temperature": 0.3}


    )
    return response['response']

broken_sentence = "He go to school each day."
correction = correct_grammar(broken_sentence)
print("Correction:\n",correction)


import ollama


def get_grammar_correction(text):
    """
    Get grammar correction for the given text using Ollama API.
    
    This function sends the input text to the Ollama API with a specific prompt
    requesting grammar correction and explanation. It uses the deepseek-r1:1.5b
    model with a low temperature setting for consistent results.
    
    Args:
        text (str): The text to be grammar-checked and corrected
        
    Returns:
        str: The API response containing the corrected text and explanation
        
    Example:
        >>> result = get_grammar_correction("He go to school each day.")
        >>> print(result)
    """
    prompt = f"Fix the grammar in the following sentence and explain the correction:\n\n{text}"
    
    api_response = ollama.generate(
        model="deepseek-r1:1.5b",
        prompt=prompt,
        options={"temperature": 0.3}
    )
    
    return api_response['response']


def main():
    """
    Demonstrate the grammar correction functionality with an example.
    
    This function provides a simple example of how to use the
    get_grammar_correction function and displays the result.
    """
    example_sentence = "He go to school each day."
    correction_result = get_grammar_correction(example_sentence)
    
    print("Grammar Correction Result:")
    print("-" * 30)
    print(correction_result)


if __name__ == "__main__":
    main()

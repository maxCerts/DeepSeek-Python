import ollama
from typing import List

def generate_content_plaintext(themes: List[str], days: int = 7) -> str:
    """
    Generate social media posts in plain text format
    Args:
        themes: list of content themes (e.g. ["AI", "Startups"]
        days: Number of posts to generate

    Returns:
        Raw text output from LLM
    """

    prompt = f"""Generate {days} LinkedIn post ideas about {", ".join(themes)}.
    For each post include:
    1. Title
    2. Hook (first sentence)
    3. Content (under 100 words)
    4. 5 hashtags
    5. Best posting time
    
    Separate posts with "___" and keep all text plain. """

    response = ollama.generate(
        model="deepseek-r1:8b",
        prompt=prompt,
        options={"temperature": 0.7}
    )
    return response["response"]

if __name__ == "__main__":
    posts = generate_content_plaintext(["AI Automation", "SaaS"], 3)
    print("Generated posts: ", posts)
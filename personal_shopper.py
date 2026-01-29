import ollama
from typing import List

def get_shopping_recommendations(query: str, num_items: int = 3) -> str:
    """
    Get shopping recommendations as clean formatted text.
    Args:
         query: User's shopping request
         num_items: Number of recommendations to retun
    Returns:
        Formatted text with product recommendations.
    """
    prompt = f"""
    Recommend {num_items} products for: "{query}"
    
    Present as a clean text list with:
    1. Product Name (Price)
    2. Key Specs: CPU/GPU/RAM/Storage
    3. Pros: [list]
    4. Cons: [list]
    5. Where to Buy
    
    Separate products with "___"
    
    Include exact model numbers and current prices
"""

    response = ollama.generate(
        model="deepseek-r1:8b",
        prompt=prompt,
        options={"temperature": 0.4}
    )
    return response["response"]

def print_recommendations(response: str):
    print("\nRecommended Products")
    print("=" * 50)
    print(response)
    print("=" * 50)

if __name__ == "__main__":
    print("AI Personal Shopper (Press Ctrl+C to quit)")
    while True:
        try:
            query = input("\nWhat product are you looking for?\n ").strip()
            if not query:
                continue

            print("Finding the best options....")
            recommendations = get_shopping_recommendations(query)
            print_recommendations(recommendations)

        except KeyboardInterrupt:
            print("Happy Shopping!")
            break


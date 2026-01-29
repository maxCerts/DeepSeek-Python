import ollama
import json

social_post = """ This new app update is so terrible. It is now more slower and hard to use.
"""

response = ollama.chat(
    model = "deepseek-r1:8b",
    messages = [{
        "role": "user",
        "content": f"Analyze the sentiment of this social media post and respond with a JSON containing sentiment (positive, neutral, negative) and a brief reason:\n\n{social_post}"
    }]
)

sentiment_info = response.message.content

try:
    sentiment_data = json.loads(sentiment_info)
    print("Sentiment:", sentiment_data.get("sentiment"))
    print("Reason:", sentiment_data.get("reason"))

except:
    print("Raw response from DeepSeek:")
    print(sentiment_info)
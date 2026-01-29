import pandas as pd
import ollama

df = pd.read_csv("Students_Scores.csv")
print(df.head())

description = f"""
I have a dataset with the following columns:{', '.join(df.columns)}.
Please generate python code to train a machine learning model that predicts {df.columns[-1]}
based on {df.columns[1]}.
"""

response = ollama.chat(
    model = "deepseek-r1:8b",
    messages = [{
        "role": "user",
        "content": description,
    }]
)

model_code = response["message"]["content"]
print("Generated Model Code: \n")
print(model_code)

with open ("student_model.py", "w") as f:
    f.write(model_code)
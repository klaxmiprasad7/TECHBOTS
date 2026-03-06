
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_code(code):

    prompt = f'''
You are a senior software engineer.

Analyze the following code and return:
1. Errors
2. Performance issues
3. Security risks
4. Optimized version of the code

Code:
{code}
'''

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role":"user","content":prompt}]
        )

        return response["choices"][0]["message"]["content"]

    except Exception as e:
        return f"Error during analysis: {str(e)}"




import os
from openai import OpenAI

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.environ["HF_TOKEN"],
)

completion = client.chat.completions.create(
    model="openai/gpt-oss-120b:groq",
    messages=[
        {
            "role": "user",
            "content": "What is the capital of France?"
        }
    ],
)

print(completion.choices[0].message)
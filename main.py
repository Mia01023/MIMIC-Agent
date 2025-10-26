import os
from openai import OpenAI

try:
    client = OpenAI(
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )

    completion = client.chat.completions.create(
        model="qwen-plus",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What is your name?"},
        ],
    )
    print(completion.choices[0].message.content)
    print(completion.model_dump_json())
except Exception as e:
    print(f"wrong message:{e}")

OPENAI_KEY = "sk-........"
MODEL = "gpt-4-1106-preview"
try:
    import requests
except ImportError:
    import subprocess

    subprocess.check_call(["python3", "-m", "pip", "install", "requests"])
    import requests
try:
    import openai
except ImportError:
    import subprocess

    subprocess.check_call(["python3", "-m", "pip", "install", "openai"])
    import openai
import sys

input_string = sys.argv[1]  # user

system = "You are a professional expert, renowned as an exceptionally skilled and efficient English copywriter, a meticulous text editor, and an esteemed New York Times editor."
instruction = "Fix spelling and grammar errors, improve clarity, and make sure your writing is polished and professional, keep the original voice and tone of the writing, only respond with the correct answer, no explanation is needed."
user_message = input_string


client = openai.OpenAI(
    api_key=OPENAI_KEY,
)
try:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": instruction},
            {"role": "user", "content": user_message},
        ],
    )
    generated_text = response.choices[0].message.content

    print(f"{input_string}\n\n{generated_text.strip()}")
except Exception as e:
    print("error", e)

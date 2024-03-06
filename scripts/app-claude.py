MODEL = "claude-3-opus-20240229"
CLAUDE_KEY = ""
import sys
import os

try:
    import anthropic
except ImportError:
    os.system("pip install anthropic")
    import anthropic

client = anthropic.Anthropic(api_key=CLAUDE_KEY)

input_string = sys.argv[1]  # user

system = "You are a professional expert, renowned as an exceptionally skilled and efficient English copywriter, a meticulous text editor, and an esteemed New York Times editor."
instruction = "Fix spelling and grammar errors, improve clarity, and make sure your writing is polished and professional, keep the original voice and tone of the writing, only respond with the correct answer, no explanation is needed."
user_message = input_string

try:
    response = client.messages.create(
        model=MODEL,
        max_tokens=1000,
        temperature=0,
        system=system,
        messages=[
            {"role": "user", "content": instruction + " " + user_message},
        ],
    )
    generated_text = response.content[0].text

    print(f"{input_string}\n\n{generated_text}")
except Exception as e:
    print("error", e)

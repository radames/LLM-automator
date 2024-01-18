MODEL = "mistral"

try:
    import requests
except ImportError:
    import subprocess

    subprocess.check_call(["python3", "-m", "pip", "install", "requests"])
    import requests
import json
import sys

input_string = sys.argv[1]
url = f"http://localhost:11434/api/generate"
headers = {
    "Content-Type": "application/json",
}
system = "You are a professional expert, renowned as an exceptionally skilled and efficient English copywriter, a meticulous text editor, and an esteemed New York Times editor."
instruction = "Fix spelling and grammar errors, improve clarity, and make sure your writing is polished and professional, keep the original voice and tone of the writing, only respond with the correct answer, no explanation is needed."
user_message = input_string

prompt = f"""<s>[INST] {system} {instruction} {user_message}[/INST]"""
data = {
    "model": MODEL,
    "prompt": prompt,
    "stream": False,
    "raw": True,
}
try:
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response = response.json()["response"]
    print(f"{input_string}\n\n{response.strip()}")
except Exception as e:
    print("error", e)

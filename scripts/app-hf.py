HF_TOKEN = "hf_xxxxxx"
MODEL = "mistralai/Mixtral-8x7B-Instruct-v0.1"
try:
    import requests
except ImportError:
    import subprocess

    subprocess.check_call(["python3", "-m", "pip", "install", "requests"])
    import requests
import sys

input_string = sys.argv[1]  # user
url = f"https://api-inference.huggingface.co/models/{MODEL}"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {HF_TOKEN}",
}
system = "You are a professional expert, renowned as an exceptionally skilled and efficient English copywriter, a meticulous text editor, and an esteemed New York Times editor."
instruction = "Fix spelling and grammar errors, improve clarity, and make sure your writing is polished and professional, keep the original voice and tone of the writing, only respond with the correct answer, no explanation is needed."
user_message = input_string

prompt = f"""<s>[INST] {system} {instruction} {user_message}[/INST]"""
data = {
    "inputs": prompt,
    "parameters": {"max_new_tokens": 1000, "return_full_text": False},
}
try:
    response = requests.post(url, headers=headers, json=data)
    generated_text = response.json()[0]["generated_text"]
    print(f"{input_string}\n\n{generated_text.strip()}")
except Exception as e:
    print("error", e)

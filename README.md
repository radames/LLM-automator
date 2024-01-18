# LLM-automator

# Huggingface Backend

## Installation

Get `HF_TOKEN` from <https://huggingface.co/settings/tokens>

Edit `llm-automator.workflow` with the Automator app, replace `HF_TOKEN` with your token.

You may also edit `MODEL="mistralai/Mixtral-8x7B-Instruct-v0.1"` to use a different LLM from [huggingface.co/models](https://huggingface.co/models?pipeline_tag=text-generation&other=endpoints_compatible&sort=trending)

<img src="assets/step-1.jpg" style="max-width: 600px;" />

<img src="assets/step-2.jpg" style="max-width: 600px;" />

Install the workflow. This essentially copies the workflow to `~/Library/Services/llm-automator.workflow`.

<img src="assets/step-3.jpg" style="max-width: 600px;" />

<img src="assets/step-4.jpg" style="max-width: 600px;" />

Go to System Preferences -> Keyboard -> Shortcuts -> Services -> General -> llm-automator, and set the shortcut to whatever you want, in my case I set it to `⌃⌥⌘M`.

<img src="assets/step-5.jpg" style="max-width: 600px;" />

<img src="assets/step-6.jpg" style="max-width: 600px;" />

## Usage

In any OSX application, select some text, and press the shortcut you set in step 3. The selected text will be replaced with the generated text from the model.

# Ollama Backend

Install [ollama](https://ollama.ai/)

Run in the background:

```bash
ollama run mistral
```

Install `llm-automator-ollama.workflow` the same way as above, no need to edit and add token, however you may edit `MODEL="mistral"`, in case you want to use a different model

<img src="assets/step-7.jpg" style="max-width: 600px;" />

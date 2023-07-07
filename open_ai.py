import openai
import os

# Get the API key and resource endpoint from environment variables
API_KEY = os.getenv("AZURE_OPENAI_API_KEY") 
RESOURCE_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT") 

# Set the API type and key in the openai library
openai.api_type = "azure"
openai.api_key = API_KEY
openai.api_base = RESOURCE_ENDPOINT
openai.api_version = "2022-12-01"

COMPLETIONS_MODEL = "text-davinci-003"

strs = ["" for x in range(3)]

# Set the parameter for the completions API call
COMPLETIONS_API_PARAMS = {
    # We use temperature of 0.7 to generate more interesting and varied completions.
    "temperature": 0.7,
    "max_tokens": 500,
    "engine": COMPLETIONS_MODEL,
}

def chat_history(text):
    # Shift the chat history by moving the strings in the list
    strs[0] = strs[1]
    strs[1] = strs[2]
    strs[2] = text

def prompt_open_ai(prompt, tokens):
    # Combine the prompt with the chat history
    prompt_history = strs[0] + "\n" + strs[1] + "\n" + strs[2] + "\n" + prompt

    # Make the completions API call to generate a response
    response = openai.Completion.create(
        prompt=prompt_history,
        **COMPLETIONS_API_PARAMS
    )
    
    # Extract the generated text from the response
    generated_text = response["choices"][0]["text"]
    
    # Update the chat history with the new text
    chat_history(prompt + "\n" + generated_text)

    return generated_text

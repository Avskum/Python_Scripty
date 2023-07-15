#bot was made for Linux CZ/SK community
#autor: Robert Mašír aka Delirium aka Avskum

import requests
import json

client = discord.Client(intents=discord.Intents.all())

def call_openai_api(prompt_text):
    url = "https://api.openai.com/v1/engines/text-davinci-003/completions"
    headers = {
        "Authorization": "Bearer api_key",
        "Content-Type": "application/json",
    }
    data = json.dumps({
        "prompt": prompt_text,
        "max_tokens": 100
    })
    response = requests.request("POST", url, headers=headers, data=data)
    response_json = response.json()
    if 'choices' in response_json:
        return response_json["choices"][0]["text"].strip()
    else:
        print(f"Error: {response_json}")
        return None

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!chatgpt'):
        prompt = message.content[8:]
        response_text = call_openai_api(prompt)
        if response_text is not None:
            await message.channel.send(response_text)

client.run('api_discord_key')

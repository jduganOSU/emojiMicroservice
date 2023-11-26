import requests
from dotenv import load_dotenv
import os

load_dotenv()

def fetch_emoji(name):
    key = os.getenv('API_NINJA_KEY')
    api_url = 'https://api.api-ninjas.com/v1/emoji?name={}'.format(name)
    response = requests.get(api_url, headers={'X-Api-Key': key})
    json = response.json()
    print(json)
    if not json:
        return 'Emoji name not found'

    return json[0]['character']
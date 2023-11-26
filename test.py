import requests

if __name__ == '__main__':
    emoji = requests.get('http://127.0.0.1:5000/fetch_emoji?name=guitar').json()
    print(emoji['emoji'])
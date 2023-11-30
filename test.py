import requests

if __name__ == '__main__':
    emoji = requests.get('https://emoji-microservice-c2d2e08d1329.herokuapp.com/fetch_emoji?name=guitar').json()
    print(emoji['emoji'])
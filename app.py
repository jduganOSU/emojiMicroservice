from flask import Flask, jsonify, request
from fetch_emoji import fetch_emoji
import flask_cors

app = Flask(__name__)
flask_cors.CORS(app)


@app.route('/fetch-emoji')
def emoji_return():
    name = request.args.get('name', default='', type=str)
    emoji = fetch_emoji(name)
    if emoji == 'Emoji name not found':
        return {'emoji': 'Error: Emoji name not found'}
    return jsonify(emoji=emoji)

if __name__ == '__main__':
    app.run(port=5000)

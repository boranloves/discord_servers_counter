from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)
bot_name = "시이"

@app.route("/", methods=["GET", "POST"])
def bot_info():
    bot_name = request.form.get('name')
        
    if bot_name:
        url = f"https://koreanbots.dev/api/v2/search/bots?query={bot_name}"
    else:
        url = f"https://koreanbots.dev/api/v2/search/bots?query=시이" 

    headers = {
                "Content-Type": "application/json"
            }

    response = requests.get(url, headers=headers)
    data1 = response.json() 

    servers = data1["data"]["data"][0]["servers"]
    id = data1["data"]["data"][0]["id"]
    avatar_id = data1["data"]["data"][0]["avatar"]
    name = data1["data"]["data"][0]["name"]
    intro = data1["data"]["data"][0]["intro"]

    avatar_url = f"https://cdn.discordapp.com/avatars/{id}/{avatar_id}.png"

    datas = {"name": name, "avatar": avatar_url, "servers": servers, "intro": intro}

    return render_template('bot_info.html', data=datas)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

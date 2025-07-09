from flask import Flask, render_template, request
import asyncio
from spammer import TelegramSpammer

app = Flask(__name__)
spammer = None

@app.route("/", methods=["GET", "POST"])
def index():
    global spammer
    if request.method == "POST":
        api_id = int(request.form["api_id"])
        api_hash = request.form["api_hash"]
        phone_number = request.form["phone_number"]
        chat = request.form["chat"]
        delay = int(request.form["delay"])
        messages = request.form["messages"].splitlines()

        spammer = TelegramSpammer(api_id, api_hash, phone_number, chat, delay, messages)
        asyncio.run(spammer.start())

    return render_template("index.html")

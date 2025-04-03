from flask import Flask
import threading
import time

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is alive!"

def keep_alive():
    app.run(host="0.0.0.0", port=8080)

# Flask server ko background me run karne ke liye thread use karo
threading.Thread(target=keep_alive, daemon=True).start()

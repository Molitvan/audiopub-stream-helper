import chat_client

name = "ping"

def run(data, chat: chat_client.chat_client):
    username = data["user"]["name"]
    chat.send_message(f"Pong! Sent by {username}")

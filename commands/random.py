import chat_client
import random

name = "random"

def run(data, chat: chat_client.chat_client):
    chat.send_message(f"Your random number is: {random.randint(0, 100)}")

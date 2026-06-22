import chat_client

name = "random"
import random

def run(data, chat: chat_client.chat_client):
    chat.send_message(f"Your random number is: {random.randint(0, 100)}")

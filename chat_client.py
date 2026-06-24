import requests
import json
import sys
from main import play, error_sound

class chat_client():
    base_url: str
    stream_url: str
    session: requests.Session

    def __init__(self, stream_url: str, config):
        self.stream_url = stream_url

        self.session = requests.session()
        self.base_url = config["url"]

        login_response = self.session.post(f"{self.base_url}/login", data={ "email": config["credentials"]["email"], "password": config["credentials"]["password"] }, allow_redirects=False)

        if "failure" in login_response.text:
            print("Login failed. Check your email and password.")
            print("If you want to use Audiopub Stream Helper without loggin in, you must disable chat commands in config.json.")
            if config["enabled_sounds"]["error"]: play(error_sound)
            sys.exit(1)

        print("Logged in.")

    def send_message(self, message: str):
        chat_response = self.session.post(self.stream_url, json={ "content": message })

        if not chat_response.ok:
            print("Chat send failed")
            print("Status:", chat_response.status_code)
            print(chat_response.text)
            raise Exception()
        
        return True

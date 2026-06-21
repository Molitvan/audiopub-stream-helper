import requests
import json

class chat_client():
    base_url: str
    stream_url: str
    session: requests.Session

    def __init__(self, stream_url: str):
        self.stream_url = stream_url

        with open("config.json", "r") as file:
            config = json.loads(file.read())
            file.close()

        self.session = requests.session()
        self.base_url = config["url"]

        login_response = self.session.post(f"{self.base_url}/login", data={ "email": config["credentials"]["email"], "password": config["credentials"]["password"] }, allow_redirects=False)

        if login_response.status_code not in (200, 303, 302):
            print("Login failed")
            print("Status:", login_response.status_code)
            print(login_response.text)
            raise SystemExit(1)

        print("Logged in.")

    def send_message(self, message: str):
        chat_response = self.session.post(self.stream_url, json={ "content": message })

        if not chat_response.ok:
            print("Chat send failed")
            print("Status:", chat_response.status_code)
            print(chat_response.text)
            raise SystemExit(1)
        
        return True

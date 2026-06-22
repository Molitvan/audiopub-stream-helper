import requests
import prism
import json
import sseclient
import time
import playsound3
import sys
import chat_client
import pkgutil
import importlib
import commands as commands_package

connect_sound = "sounds/connect.wav"
disconnect_sound = "sounds/disconnect.wav"
listener_join_sound = "sounds/listener_join.wav"
listener_leave_sound = "sounds/listener_leave.wav"
error_sound = "sounds/error.wav"

def play(sound: str):
    try:
        playsound3.playsound(sound)
    except:
        pass

def main(url: str, use_sapi: str):
    with open("config.json", "r") as file:
        config = json.loads(file.read())
        file.close()

    commands = []
    if config["enable_chat_commands"]:
        for module_info in pkgutil.walk_packages(commands_package.__path__, commands_package.__name__ + "."):
            commands.append(importlib.import_module(module_info.name))

    if use_sapi != "":
        speech = prism.Context().create(prism.BackendId.SAPI)
        print("Useing SAPI")
    else:
        speech = prism.Context().create_best()
        print("Using best backend")

    if config["enable_chat_commands"]:
        chat = chat_client.chat_client(url)

    listeners: int = 0

    while True:
        try:
            print("Connecting...")
            play(connect_sound)

            response = requests.get(f"{url}/events", stream=True, timeout=None)
            response.raise_for_status()

            client = sseclient.SSEClient(response)

            for event in client.events():
                data = json.loads(event.data) if event.data else {}

                if event.event == "chat":
                    name = data["user"]["name"]
                    content = data["content"]
                    print(f"{name}: {content}")
                    if config["enable_chat_narration"]: speech.output(f"{name} said {content}")

                    if config["enable_chat_commands"] and content.startswith(config["command_prefix"]):
                        for command in commands:
                            if command.name == "".lstrip(config["command_prefix"]):
                                command.run(data)
                elif event.event == "listeners":
                    active = data["activeListeners"]

                    if active > listeners:
                        play(listener_join_sound)
                        print(f"Listener joined: {active} listeners")
                    elif active < listeners:
                        play(listener_leave_sound)
                        print(f"Listener left: {active} listeners")

                    listeners = active
                elif event.event == "finish":
                    message = "Stream finished. Exiting..."
                    speech.output(message)
                    print(message)
                    play(disconnect_sound)
                    return
        except KeyboardInterrupt:
            print("Exiting...")
            play(disconnect_sound)
            sys.exit(0)
        except Exception as error:
            print(f"Disconnected: {error}")
            print("Trying to reconnect in 5 seconds...")
            play(error_sound)
            time.sleep(5)

if __name__ == "__main__":
    print("Welcome to Audiopub Stream Helper")
    url = input("Enter the stream URL: ").rstrip("/")
    use_sapi = input("Would you like to force use SAPI for output? Press enter for no, type anything for yes: ")
    main(url, use_sapi)
    input("Press ENTER to exit")

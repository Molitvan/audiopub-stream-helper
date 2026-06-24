# Audiopub Stream Helper

A small utility to enhance the experience of streaming on [Audiopub](https://audiopub.site).

## Features

- Chat narration
- Sound effects for when listeners leave and join, when the stream ends and when errors happen
- Custom chat commands

Yeah... when I said it's small, I meant it lol.

## Setup

1. [Install UV](https://github.com/astral-sh/uv)
2. Install Git (if not already installed)
3. Clone this repository by opening your terminal and running "git clone https://github.com/Molitvan/audiopub-stream-helper"
4. Open your terminal in the cloned repository folder and run "uv sync"

## Updates

To install updates, run "git pull" from your terminal in the cloned repository folder periodically.

## Usage

Simply open the terminal in the folder where you set everything up and run "uv run main.py"

### Custom Chat Commands

All commands are just simply Python files with a specific structure. A variable called name (the name of the command) and a function called run (what the command does) that accepts 2 arguments: data (a dictionary containing the data we get from Audiopub) and chat (a chat_client object, used to send messages back). Those Python files must be placed in the commands folder.

There are some demo commands included. Feel free to look through those to understand how they work better.

Note: in order to use custom commands, you must fill out config.json (generated on first run) with your Audiopub email and password. Also, commands are disabled by default, so if you want to use them you have to set enable_chat_commands to true in config.json.

[Listen to the custom commands tutorial](https://audiopub.site/listen/e15601c5-7a30-4e49-9c75-f84afd2b6424)

#### Commands Data

When you make a command, you get a dictionary called data containing data from Audiopub. This is its structure:
- id: str (the ID of the message)
- content: str (the content of the message)
- createdAt: int (when was the message sent)
- user: dict (a dictionary containing information about the user who sent the message)
    - id: str (the message author's ID)
    - name: str (the message author's username)
    - displayName: str (the message author's display name)
    - bio: str (the message author's bio)
- stream: dict (a dictionary containing information about the stream)
    - id: str (the ID of the stream)
    - title: str (the title of the stream)
    - description: str (the description of the stream)
    - state: enum (the state of the stream, can be: pending, active, disconnected, finished)
    - peakListeners: int (the most amount of listeners the stream had)
    - activeListeners: int (how many listeners the stream currently has)
    - createdAt: int (when was the stream started)
    - user: dict (information about the stream's creator)
        - id: str (the stream creator's ID)
        - name: str (the stream creator's username)
        - displayName: str (the stream creator's display name)
        - bio: str (the stream creator's bio)
    - chats: list of dicts or None (a list of all the previous chat messages. The messages all have the same structure as the data dictionary described here)

## Customizing the sounds

You can customize the default sounds by replacing files in the sounds folder. To disable a sound, see config.json (generated automatically on first run).

## Maintenance

I made this tool just for fun and I plan on maintaining it only while it's fun for me to do so. I made it for myself first, but I'm posting it here in case someone else finds it interesting. That said, feel free to open pull requests or fork this if you want something added.

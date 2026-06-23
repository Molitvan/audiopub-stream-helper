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

## Customizing the sounds

You can customize the default sounds by replacing files in the sounds folder. To disable a sound, delete it from the folder or rename it.

Note: in order to use custom commands, you must fill out config.json (generated on first run) with your Audiopub email and password

## Maintenance

I made this tool in about an hour (including the sounds) and I plan on maintaining it only for how much my needs require. I made it for myself first, but I'm posting it here in case someone else finds it interesting. That said, feel free to open pull requests or fork this if you want something added.

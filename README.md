# Keystones
A Discord bot to track mythic keystones in World of Warcraft using [discord.py](https://github.com/Rapptz/discord.py).

## Features

- Keep track of keystones for your characters

    ![Example of !add command](https://imgur.com/tIEpNym.png)
    
- Show the latest keystones for anyone in your server

    ![Example of !keys command](https://imgur.com/LZ1ZDry.png)
    
- Check this week's affixes

    ![Example of !affixes command](https://imgur.com/8aReCE4.png)
    
- Get information about a specific affix

    ![Example of !affix command](https://imgur.com/9bFGic0.png)
    
- See the timers for a specific dungeon

    ![Example of !timer command](https://imgur.com/fxcOkxC.png)
    
- List all of the dungeons with some of their alternative names

    ![Example of !dungeons command](https://imgur.com/RJsoAsb.png)
    
- And more - use the `!help` command for more details about each command

## Add the bot to your server

Use [this link](https://discord.com/api/oauth2/authorize?client_id=544014565348737026&permissions=2048&scope=bot) to add the bot to your server. You must be a server admin to add the bot.

## Run the bot on your own

Requires [python 3.6.3](https://www.python.org/downloads/release/python-363/) to run.

- Clone this repo by running `git clone https://github.com/Hovspian/keystones.git` from the terminal or fork it and follow the instructions there
- Get the project's dependencies by running `pip install -r requirements.txt`
- Follow `secrets_example.py` to set up your own `secrets.py`
- Run the bot with `python -m keystones.__main__` while in the root directory of this repo

## Bug reports, feature requests, and other issues

If you find an issue with the bot or think of a feature that would be useful, [open an issue](https://github.com/Hovspian/keystones/issues/new/choose).

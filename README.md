# youtube-playlist-telegram-bot
A benign telegram bot using Youtube Data API v3.

## Usage

```bash
# venv
pip3 install -r requirements.txt
./playlits-bot.py
```

Prerequisite: 

* [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) 
* [google-api-python-client](https://github.com/googleapis/google-api-python-client) 

### Try My Bot

Telegram @ElisaArchive

(Now not available)

![demo](./assets/demo.gif)

## Todo

- [ ] Determine the playlist list - Syntactic sugar
- [ ] Determine the logic of configs, logging info and other assets
- [ ] Run as cron 
- [x] why my Elisa In Ecuador account would raise exception?? -  not all users have username, use `chat.id` instead
- [ ] Do I want to wrap it up as an API?
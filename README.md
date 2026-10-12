# message-sender

Small Python scripts that post a message to Twitter, Telegram, Discord, Mastodon and the Steem blockchain, one script per platform plus `main.py`, which combines them. A starting point for a bot that cross-posts the same message to several networks.

> **Status:** archived. Built in 2019. Kept for reference, not maintained. Several of these platforms have changed their APIs and client libraries since then, so expect the scripts to need updates before they work.

## What it does

- `twitter.py`: posts a tweet with Tweepy, authenticating with OAuth consumer and access tokens.
- `telegram.py`: sends a message to a chat with the `telebot` module.
- `dc.py`: logs in as a Discord bot and sends the message to every server the bot has joined, then disconnects (see the note below).
- `mastodon-tooth.py`: posts a toot to mastodon.social with Mastodon.py.
- `steemit.py`: publishes a post with a title and the tags `tr` and `busy` to the Steem blockchain with steem-python.
- `main.py`: all five senders in one file; running it sends "Hello World" to each platform.

Every script sends a "Hello World" test message when run. Credentials are empty placeholders in the code (there is no config file or environment variable support), so fill them in first.

### Discord note

`dc.py` shows how to push a message to every server a bot is in without waiting for a user command. It posts only in text channels named `general` or `text`; to target another channel, change the name check in `sendm()`.

## Background

The scripts came out of Free Games On Steam, a bot that shared free game offers from Steam, Origin, Humble Bundle, Epic Games and others on these platforms. The bot itself is not in this repo. Its accounts were [@freegamesonsteam@mastodon.social](https://mastodon.social/@freegamesonsteam) and [@freegameonsteam](https://twitter.com/freegameonsteam) on Twitter.

## Tech stack

- Python 3
- Tweepy (Twitter)
- `telebot` (Telegram)
- discord.py (Discord)
- Mastodon.py (Mastodon)
- steem-python (Steem)

## Notes

- `requirements.txt` pins only `steem==1.0.1`; the other libraries are not listed.
- `steemit.py` also contains a copy of the Discord sender at the bottom, so running it posts to Discord as well.

## License

GPL-3.0, see [LICENSE](LICENSE).

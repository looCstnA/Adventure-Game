# A Game for the Planet - Chatbots in Python

A few simple scene bots text-based adventure game that will search for keys/commands (now multiple words or sentences) in order to advance.

Three classes:

- Scene: a scene is now a bot to have a "conversation" with.
- Player: that represents our user.
- Giveway: represents when the user receives something.

One Function:

- extract_command: extracts commands from text using partial matching

You can try it with:

```
git clone <this_repo>
cd <this_repo>
virtualenv -p python3 env
pip install -r requirements.txt
python3 game.py
```

## Chatterbot

- [Chatterbot](https://chatterbot.readthedocs.io/en/stable/)
- [Chatterbot-corpus](https://github.com/gunthercox/chatterbot-corpus)

Before jumping into the (now almosrt intelligent) game. Have a look at what we are doing in the `test_bot.py`

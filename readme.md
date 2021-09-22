# A Game for the Planet - Chatbots in Python

A simple text-based adventure game that will for keys/commands (now multiple words or sentences) in order to advance.

Three classes:

- Scene: to create, well, differnet scenes.
- Player: that represents our user.
- Giveway: represents when the user receives something.

One Function:

- extract commands

You can try it with:

```
git clone <this_repo>
cd <this_repo>
virtualenv -p python3 env
pip install -r requirements.txt
python3 game.py
```


## Fuzzy Matching

- [Python FuzzyWuzzy](https://pypi.org/project/fuzzywuzzy/)

Before jumping into the (now almosrt intelligent) game. Have a look at what we are doing in the `test_algos.py`


Afterwards, you can move to the `Chatterbot` branch of this repo.

```
git checkout -b Chatterbot
```

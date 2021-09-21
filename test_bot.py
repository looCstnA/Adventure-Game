from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

## Simple List Trainer

chatbot = ChatBot(
    'Test',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///test1.sqlite3'
)

trainer = ListTrainer(chatbot)
trainer.train([
    'Bonjour',
    'Bonjour',
    'Comment allez vous?',
    'Très bien.',
    'Savez-vous ou nous sommes?',
    'Non, ou sommes nous?',
    'Nous sommes à AntsWood, un petit village paisible'
])

print('\n\n*** Simple List Trainer Conversation ***\n\n')

while True:
    try:
        bot_input = chatbot.get_response(input())
        print(bot_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break


## Corpus Training

chatbot = ChatBot('Export Example Bot'
	storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///test2.sqlite3')

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.french')

'''
This is an example showing how to create an export file from
an existing chat bot that can then be used to train other bots.
'''
# trainer.export_for_training('./french_export.json')

print('\n\n*** Corpus Trainer Conversation ***\n\n')

while True:
    try:
        bot_input = chatbot.get_response(input())
        print(bot_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break
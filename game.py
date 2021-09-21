from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from fuzzywuzzy import fuzz, process
from yaml import load

# class Scene(ChatBot):
#     """An augmented ChatBot"""
#     def __init__(self, name):
#         super().__init__(
#             name, 
#             read_only=True,
#             storage_adapter='chatterbot.storage.SQLStorageAdapter',
#             database_uri='sqlite:///'+name+'.sqlite3'
#         )

        
def extract_command(text, keys_dict):
    pack = []
    for k, v in keys_dict.items():
        cmd = process.extract(text, v, scorer=fuzz.partial_ratio, limit=1)
        if cmd[0][1] == 100:
            return k
        elif cmd[0][1] > 70:
            pack.append([k,cmd[0][1]])
    if pack:
        return sorted(pack, key=lambda x: x[1], reverse=True)[0][0]
    return None


class Player():
    """docstring for Player"""
    def __init__(self):
        super(Player, self).__init__()
        self.inventory = []


class Scene(ChatBot):
    """docstring for Scene"""
    def __init__(self, name, keywords, keys_dict, player=None, condition=None, success=None, fail=None):
        super(Scene, self).__init__(
            name, 
            read_only=True,
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            database_uri='sqlite:///'+name+'.sqlite3'
        )
        trainer = ListTrainer(self, show_training_progress=False)
        
        data = load(open("conversations/"+name+".yaml", 'r'))
        for conv in data['conversations']:
            trainer.train(conv)
        
        self.intro = data['intro']
        self.keywords = keywords
        self.keys_dict = {k: keys_dict[k] for k in keywords} # only keys given
        self.player = player
        self.condition = condition
        self.success = success
        self.fail = fail

    def run(self):
        print("\n\n\n\n")
        print(self.intro)
        print("\n")
        if self.player and self.condition:
            if self.condition in self.player.inventory:
                return self.success
            else:
                return self.fail
        while True:
            reponse = input(">").lower()
            cmd = extract_command(reponse, self.keys_dict)
            if cmd:
                return cmd
            else:
                # chatbot.get_response
                print(self.get_response(reponse))


class Giveaway():
    """docstring for ClassName"""
    def __init__(self, item, player, callback):
        super(Giveaway, self).__init__()
        self.item = item
        self.player = player
        self.callback = callback

    def run(self):
        self.player.inventory.append(self.item)
        return self.callback
                


SCENES_KEYS = {
    'départ':['retourne au début','redémarrer','recommencer au départ','retourner à Antsbourg'],
    'fourmi':['parler à la fourmi','saluer la fourmi'],
    'abeille':["parler à l abeille", 'saluer l abaille'],
    'graines':['demander les graines à l abeille','puis je avoir les graines','donne moi les graines'],
    'forêt':['à la forêt','vers la foret','prendre le chemin','prendre le chemin vers la forêt'],
    'planter':['planter les graines','utiliser les graines']
}

player = Player()
scenes = {
    'départ': Scene(
        name='antswood',
        # intro="Bonjour visiteurs, bienvenue à Antswood.\n\nUne forêt où cohabitent différentes espèces (comme ici une fourmi et une abeille) qui, ensemble, forment un écosystème complexe rempli de personnages, d’actions (et réactions), d’intrigues et de challenges à accomplir.",
        keywords=['fourmi','abeille','forêt'],
        keys_dict=SCENES_KEYS
    ),
    'fourmi':Scene(
        'fourmi',
        # intro="Bonjour, je suis fourmi #27903. \n\nNous les fourmis entretenons les arbres et la forêt. Notre objectif: maintenir un certain équilibre dans l’écosystème.",
        keywords=['départ','abeille','forêt'],
        keys_dict=SCENES_KEYS
    ),
    'abeille': Scene(
        'abeille',
        # intro="Bonjour, je suis une abeille. Nous nous chargeons de polliniser les fleurs. Notre objectif: trouver des fleurs. Parfois nous y trouvons des graines :)",
        keywords=['départ','fourmi','forêt','graines'],
        keys_dict=SCENES_KEYS
    ),
    'graines': Giveaway('graines',player,'abeille2'),
    'abeille2': Scene(
        name='abeille2',
        # intro="Voici, prenez ces graines. Elles vous surront sûrement plus utiles.",
        keywords=['départ','fourmi','forêt'],
        keys_dict=SCENES_KEYS
    ),
    'forêt': Scene(
        name="foret",
        # intro="Vous vous balladez en forêt...",
        keywords=['départ','planter'],
        keys_dict=SCENES_KEYS,
    ),
    'planter': Scene(
        name='planter',
        # intro="...",
        keywords=['départ'],
        keys_dict=SCENES_KEYS,
        player=player,
        condition='graines',
        success='3ND',
        fail='forêt'
    ),
    '3ND': Scene(
        name='fin',
        # intro="Bien joué!",
        keywords=['départ'],
        keys_dict=SCENES_KEYS
    )
}

def main():
    scene = "départ"
    while True:
        scene = scenes[scene].run()

main()



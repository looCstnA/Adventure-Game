class Player():
    """docstring for Player"""
    def __init__(self):
        super(Player, self).__init__()
        self.inventory = []


class Scene():
    """docstring for Scene"""
    def __init__(self, intro, keywords, player=None, condition=None, success=None):
        super(Scene, self).__init__()
        self.intro = intro
        self.keywords = keywords
        self.player = player
        self.condition = condition
        self.success = success

    def run(self):
        print("\n\n\n\n")
        print(self.intro)
        print("\n")
        if self.player and self.condition:
            if self.condition in self.player.inventory:
                return self.success
        while True:
            reponse = input(">").lower()
            if reponse in self.keywords:
                return reponse


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
                

player = Player()
scenes = {
    'départ': Scene(
        intro="Bonjour visiteurs, bienvenue à Antswood.\n\nUne forêt où cohabitent différentes espèces (comme ici une fourmi et une abeille) qui, ensemble, forment un écosystème complexe rempli de personnages, d’actions (et réactions), d’intrigues et de challenges à accomplir.",
        keywords=['fourmi','abeille','forêt'],
    ),
    'fourmi':Scene(
        intro="Bonjour, je suis fourmi #27903. \n\nNous les fourmis entretenons les arbres et la forêt. Notre objectif: maintenir un certain équilibre dans l’écosystème.",
        keywords=['start','abeille','forêt'],
    ),
    'abeille': Scene(
        intro="Bonjour, je suis une abeille. Nous nous chargeons de polliniser les fleurs. Notre objectif: trouver des fleurs. Parfois nous y trouvons des graines :)",
        keywords=['départ','fourmi','forêt','graines'],
    ),
    'graines': Giveaway('graines',player,'abeille2'),
    'abeille2': Scene(
        intro="Voici, prenez ces graines. Elles vous surront sûrement plus utiles.",
        keywords=['départ','fourmi','forêt'],
    ),
    'forêt': Scene(
        intro="Vous vous balladez en forêt...",
        keywords=['départ'],
        player=player,
        condition='graines',
        success='3ND'
    ),
    '3ND': Scene(
        intro="Vous avez planté les graines. Bien joué!",
        keywords=['départ']
    )
}

def main():
    scene = "départ"
    while True:
        scene = scenes[scene].run()

main()
from fuzzywuzzy import fuzz, process

SCENES_KEYS = {
    'départ':['retourne au début','redémarrer','recommencer au départ'],
    'fourmi':['parler à la fourmi','saluer la fourmi'],
    'abeille':["parler à l abeille", 'saluer l abaille']
}

userinputs = [
    "Bonjour",
    "Comment allez vous?",
    "puis je recommencer",
    "recommence!",
    "fourmi",
    "j aimerai parler à la fourmi",
    "pourrais je parler à la fourmi?"
]

def extract_command(text, keys_dict):
    pack = []
    for k, v in keys_dict.items():
        cmd = process.extract(text, v, scorer=fuzz.partial_ratio, limit=1)
        print(cmd)
        if cmd[0][1] == 100:
            return k
        elif cmd[0][1] > 50:
            pack.append([k,cmd[0][1]])
    if pack:
        print(pack)
        return sorted(pack, key=lambda x: x[1], reverse=True)[0][0]
    return None

for i in userinputs:
    print('---')
    print('Searching for o from i:', i)
    
    print('Fuzzy Ratio')
    for key, li in SCENES_KEYS.items():
        print(process.extract(i, li, scorer=fuzz.ratio))
    print('Partial Ratio')
    for key, li in SCENES_KEYS.items():
        print(process.extract(i, li, scorer=fuzz.partial_ratio, limit=1))
    print('Token Sort Ratio')
    for key, li in SCENES_KEYS.items():
        print(process.extract(i, li, scorer=fuzz.token_sort_ratio))

    print('found: ',extract_command(i, SCENES_KEYS))
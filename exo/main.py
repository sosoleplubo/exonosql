import json
from unicodedata import normalize

import tqdm

def code_insee_paris(arrondissement):
    if not arrondissement:
        return None
    arr = arrondissement.upper().split()
    if "BOIS DE BOULOGNE" in arr:
        return "75116"
    if "BOIS DE VINCENNES" in arr:
        return "75120"
    match =

def normalize_paris(tree):
    return {
        "source":"paris",
        "commune":tree.get("arrondissement"),
        "code_insee": code_insee_paris(tree.get("arrondissement")),
        "nom":tree.get("libellefrancais"),
        "latin":f"{tree.get('genre','')} {tree.get('espece','')}".strip() or None,
        "hauteur":tree.get("hauteurenm"),
        "circon"
    }

with open("data/data1.json", "r") as f1:
    with open("data/data2.json", "r") as f2:
            data1 = json.load(f1)
            data2 = json.load(f2)

            unifier = []

            for tree in tqdm(data2):
                if tree.get("remarquable") == "OUI":
                    unifier.append(normalize_paris(tree))

            for tree in tqdm(data):
                unifier.append(normalize_hds(tree))

            with open("data/data3.json", "w") as f3:


            dataFilter = [k for k in data2 if k["remarquable"] == "OUI"]

            for item in data1:
                item[]

            common_keys = set(data1[0].keys()) & set(dataFilter[0].keys())
            print(common_keys)
            normalize_data = [[{k: item[k] for k in common_keys} for item in dataFilter],
                              [{k: item[k] for k in common_keys} for item in data1]]
            json.dump(normalize_data, f3, indent=2)

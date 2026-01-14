import json
from unicodedata import normalize

with open("data/data1.json", "r") as f1:
    with open("data/data2.json", "r") as f2:
        with open("data/data3.json", "w") as f3:
            data1 = json.load(f1)
            data2 = json.load(f2)
            dataFilter = [k for k in data2 if k["remarquable"] == "OUI"]
            common_keys = data1.keys() & data2.keys()

            merged_data = [dataFilter, data1]

            normalize
            json.dump(merged_data, f3, indent=2)

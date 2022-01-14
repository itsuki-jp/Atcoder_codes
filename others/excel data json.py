import json
from collections import OrderedDict
import pprint

with open("lang.json") as f:
    df = json.load(f)

dict = {}

for i in df:
    language = i["language"]
    count = i["count"]
    if language not in dict.keys():
        dict[language] = count
    else:
        dict[language] += count

print(dict)
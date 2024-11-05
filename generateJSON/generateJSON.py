import json

from PPT_Generation.createPPT import CreatePPT
from generateJSON.getDatas import GetDatas

# This function will generate a JSON file with the information entered for the creation of the powerpoint
def GenerateJSON(root, pages):
    # We create the json file and fill it with the dict store in data
    with open("data.json", "w") as f:
        json.dump(GetDatas(pages), f, indent=4)

    # We start the creation of the powerpoint
    CreatePPT("data.json")

    # We stop the application
    root.destroy()
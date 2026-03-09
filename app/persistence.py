
import json, os
DATA_FILE = "data/shapes.json"

def load_shapes():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE,"r") as f:
        return json.load(f)

def save_shapes(shapes):
    with open(DATA_FILE,"w") as f:
        json.dump(shapes,f,indent=2)

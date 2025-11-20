import json

SAVE_FILE = "savegame.json"

def save_data(player):
    data = {
        "health": player.health,
        "x": player.pos.x,
        "y": player.pos.y
    }
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f)

def load_data():
    try:
        with open(SAVE_FILE, "r") as f:
            return json.load(f)
    except:
        return None

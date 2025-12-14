import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "periodic_table.json")

with open(DATA_PATH, "r") as f:
    PERIODIC_TABLE = json.load(f)





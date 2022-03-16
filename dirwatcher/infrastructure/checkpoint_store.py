import json
from pathlib import Path

STORE_LOCATION = "store.json"

def mapEntry(k, v):
    return Path(k), v

def load_checkpoints() -> dict[Path, str]:
    result = {}

    f = None
    try: 
        f = open(STORE_LOCATION)
        # Do something with the file
        jsonContent = json.load(f)
            
        for k in jsonContent:
            result[Path(k)]=jsonContent[k]
    finally:
        if f:
            f.close()
    return result



def save_checkpoints(hashes: dict[Path, str]):
    ...

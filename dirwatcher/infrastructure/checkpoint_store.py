import json
from pathlib import Path

STORE_LOCATION = "store.json"

def mapEntry(k, v):
    return Path(k), v

def load_checkpoints() -> dict[Path, str]:
    result = {}

    with open(STORE_LOCATION, 'r') as f: 
        # Do something with the file
        jsonContent = json.load(f)

        for k in jsonContent:
            result[Path(k)]=jsonContent[k]
        return result



def save_checkpoints(hashes: dict[Path, str]):
    with open(STORE_LOCATION, 'w+') as f: 

        # Do something with the file
        temp_hashes = {}
        for k in hashes:
            temp_hashes[str(k)] = hashes[k]
        content = json.dumps(temp_hashes)
        f.write(content)

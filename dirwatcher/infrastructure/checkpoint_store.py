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
    f = None
    try: 
        f = open(STORE_LOCATION, 'w+')
        # Do something with the file
        temp_hashes = {}
        for k in hashes:
            temp_hashes[str(k)] = hashes[k]
        content = json.dumps(temp_hashes)
        f.write(content)

    finally:
        if f:
            f.close()

import pytest

import dirwatcher.infrastructure.checkpoint_store as store
from pathlib import Path


def test_load_checkpoints_should_load_path_to_hash_mapping_from_json_file():
    store.STORE_LOCATION = "dirwatcher/infrastructure/test_data/example_checkpoint_store.json"
    checkpoints = store.load_checkpoints()
    assert isinstance(checkpoints, dict)
    assert [(Path("dirwatcher/checkpoint_store.py"),
             "b45be769a6206b136bb60d5437349e318a51ac6ed9ce690bb3184b9e8c01ac00")] == list(checkpoints.items())


def test_load_checkpoints_should_raise_FileNotFoundError_when_store_file_not_found():
    with pytest.raises(FileNotFoundError):
        store.STORE_LOCATION = "some/non-existent-path.json"
        store.load_checkpoints()

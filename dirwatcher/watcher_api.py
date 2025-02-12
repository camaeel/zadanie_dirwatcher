from pathlib import Path
import logging
from flask import Flask

from dirwatcher.infrastructure.checkpoint_store import CheckpointStoreAdapter
from dirwatcher.infrastructure.hasher import Hasher
from dirwatcher.infrastructure.traverser import make_traverser
from dirwatcher.watcher_service import WatcherService, NoPriorCheckpointSavedError, InvalidDirectoryRequested

app = Flask("dirwatcher")
logger = logging.getLogger(__name__)
STORE_LOCATION = "store.json"


@app.route("/<path:directory>/save", methods=["POST"])
def save_current_state(directory):
    service = WatcherService(make_traverser(Path(directory)), CheckpointStoreAdapter(), Hasher())
    try:
        service.checkpoint_current_state()
    except InvalidDirectoryRequested as e:
        logger.error(e)
        return {"error": "the directory you requested does not exist"}, 400
    return "OK", 200


@app.route("/<path:directory>/ischanged")
def has_anything_changed(directory):
    service = WatcherService(make_traverser(Path(directory)), CheckpointStoreAdapter(Path(STORE_LOCATION)), Hasher())
    try:
        return {"changed": service.has_anything_changed()}, 200
    except NoPriorCheckpointSavedError as e:
        logger.error(e)
        return {"error": "you tried to use this endpoint without previously saving state"}, 400
    except InvalidDirectoryRequested as e:
        logger.error(e)
        return {"error": "you tried to check the directory that does not exist"}, 400

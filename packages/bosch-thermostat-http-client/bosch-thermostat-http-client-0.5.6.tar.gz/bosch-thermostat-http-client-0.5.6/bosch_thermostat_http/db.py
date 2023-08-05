"""Retrieve standard data."""
import json
import os

from .const import RC300

MAINPATH = os.path.join(os.path.dirname(__file__), "db")
FILENAME = os.path.join(MAINPATH, "db.json")


def open_json(file):
    """Open json file."""
    with open(file, "r") as db_file:
        datastore = json.load(db_file)
        return datastore
    return None


def get_initial_db():
    """Get initial db. Same for all devices."""
    return open_json(FILENAME)


def get_db_of_firmware(device_type, firmware_version):
    """Get db of specific device."""
    filename = "rc300.json" if device_type == RC300 else "default.json"
    filepath = os.path.join(MAINPATH, filename)
    _db = open_json(filepath)
    if _db:
        if firmware_version in _db:
            return _db[firmware_version]
    return None


def get_custom_db(firmware_version, _db):
    """Get db of device if yours doesn't exists."""
    if _db:
        if firmware_version in _db:
            return _db[firmware_version]
    return None

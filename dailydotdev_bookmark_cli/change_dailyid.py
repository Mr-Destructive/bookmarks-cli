from .bookmarks import trim_id, get_id
from pathlib import Path
import os
import re


def change_id():

    id_file = ".dailydevid.txt"

    new_id = input("Enter the new daily.dev RSS Feed URL: ")
    new_id = trim_id(new_id)
    old_id = Path(id_file).read_text()

    if old_id != new_id:
        with open(id_file, "r+") as f:
            old_id = f.read()
            f.write(f.read().replace(old_id, new_id))
        print("daily.dev id successfully edited")

    elif old_id == new_id:
        print("daily.id was not changed as it was the identical")

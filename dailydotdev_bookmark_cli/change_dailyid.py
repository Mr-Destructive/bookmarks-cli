from .bookmarks import trim_id, get_id
import os
import re

def change_id():

    id_file = '.dailydevid.txt'
    
    with open(id_file, "r+") as f1:
        new_id = input("Enter the new daily.dev RSS Feed URL: ")
        new_id = trim_id(new_id)
        contents = f1.read()
        flags=0
        pattern = re.compile(re.escape(contents), flags)
        contents = pattern.sub(new_id, contents)
        f1.seek(0)
        f1.truncate()
        f1.write(contents)
    print("daily.dev id successfully edited")

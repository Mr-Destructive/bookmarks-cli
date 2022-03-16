from .bookmarks import get_bookmarks
from .delete_dailyid import delete_id
from .change_dailyid import change_id
from rich import print
import argparse 

def main():
    print("[white]Daily Dot Dev Bookmark CLI[/white]")
    parser = argparse.ArgumentParser()
    parser.add_argument('--rm', action='store_true') 
    parser.add_argument('--del', action='store_true') 
    parser.add_argument('--ch', action='store_true') 
    parser.add_argument('--ed', action='store_true') 
    args = parser.parse_args() 

    if args.rm or args.del:
        delete_id()
    elif args.ch or args.ed:
        change_id()
    else:
        get_bookmarks()

from .bookmarks import get_bookmarks
from .delete_dailyid import delete_id
from .change_dailyid import change_id
from .tui import tui_app
from rich import print
import argparse 

def main():
    print("[white]Daily Dot Dev Bookmark CLI[/white]")
    parser = argparse.ArgumentParser()
    parser.add_argument('--rm', action='store_true') 
    parser.add_argument('--ch', action='store_true') 
    parser.add_argument('--tui', action='store_true') 
    args = parser.parse_args() 

    if args.rm:
        delete_id()
    elif args.ch:
        change_id()
    elif args.tui:
        tui_app()
    else:
        get_bookmarks()

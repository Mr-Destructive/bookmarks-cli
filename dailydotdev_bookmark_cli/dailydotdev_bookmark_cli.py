from .bookmarks import get_bookmarks
import feedparser
from rich import print
import os.path

def main():
    print("[white]Daily Dot Dev Bookmark CLI[/white]")
    get_bookmarks()

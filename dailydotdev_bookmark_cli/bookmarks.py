import feedparser
from pathlib import Path
from rich import print
import os.path


id_file = ".dailydevid.txt"


def trim_id(bookmark_id):
    return bookmark_id.split("/")[-1]


def get_feed(url):
    return feedparser.parse(url)


def get_id():

    bookmark_id = ""
    if os.path.isfile(id_file):
        bookmark_id = Path(id_file).read_text()

    if not bookmark_id:
        print("[green]Enter your-daily-dev bookmark feed url: ", end="")
        bookmark_id = input()
        bookmark_id = trim_id(bookmark_id)

        url = f"https://api.daily.dev/rss/b/{bookmark_id}"
        feed = get_feed(url)

        if "feed" in feed:
            with open(id_file, "w") as file:
                file.write(bookmark_id)

    return bookmark_id


def get_bookmarks_list():

    daily_id = get_id()

    if daily_id:
        url = f"https://api.daily.dev/rss/b/{daily_id}"
        feed = get_feed(url)

        bookmarks = feed.entries
        return bookmarks

    else:
        print("[red]Please input a valid User ID!")
    input("Press enter to exit")


def get_bookmarks():

    bookmarks = get_bookmarks_list()
    daily_id = Path(id_file).read_text()
    url = f"https://api.daily.dev/rss/b/{daily_id}"
    name = get_feed(url).feed.title

    print(f"[green]{name}")

    for bookmark in bookmarks:
        link = bookmark.link.split("?utm_source")[0].strip()

        blog_base_link = link.split("/posts/")[0].strip().replace("app", "api")

        blog_id = link.split("/posts/")[1].strip()

        blog_link = blog_base_link + "/r/" + blog_id

        print(
            f""" - [yellow][link={blog_link}]{bookmark.title}[/link][/yellow]\n
[blue][link={blog_link}]{blog_link}[/link]\n"""
        )

        if len(bookmarks) == 0:
            print(
                "[yellow]Sorry, you do not have any bookmarks created in your daily.dev account feed!"
            )

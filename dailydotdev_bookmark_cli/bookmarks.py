import feedparser
from rich import print
import os.path


def get_id():

    id_file = '.dailydevid.txt'
    bookmark_id = ""
    if os.path.isfile(id_file):
        with open(id_file, 'r') as file:
            bookmark_id = file.readlines()
        bookmark_id = bookmark_id[0]

    if not bookmark_id:
        print("[green]Enter your-daily-dev bookmark feed url: ", end="")
        bookmark_id = input()
        bookmark_id = bookmark_id.split('/')[-1]

    return bookmark_id

def get_bookmarks():

    daily_id = get_id()
    id_file = '.dailydevid.txt'

    if daily_id:
        url = f"https://api.daily.dev/rss/b/{daily_id}"
        feed = feedparser.parse(url)

        if feed.feed:
            with open(id_file, 'w') as file:
                file.write(daily_id)
        name = feed.feed.title

        print(f"[red]{name}")

        bookmarks = feed.entries

        for bookmark in bookmarks:
            link = bookmark.link.split("?utm_source")[0].strip()
            
            blog_base_link = link.split("/posts/")[0].strip().replace("app", "api") 
            
            blog_id = link.split("/posts/")[1].strip()
            
            blog_link = blog_base_link+"/r/"+blog_id

            print(f""" - [yellow][link={blog_link}]{bookmark.title}[/link][/yellow]\n
    [blue][link={blog_link}]{blog_link}[/link]\n""")

    else:
        print("[red]Please input a valid User ID!")
    input()


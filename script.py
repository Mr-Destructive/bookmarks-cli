import feedparser
from rich import print
import requests
import string
import random

with open('.dailydevid.txt', 'r') as file:
    daily_id = file.readlines()[0]

if not daily_id:
    print("[green]Enter your-daily-dev id: ", end="")
    daily_id = input()

if daily_id:
    url = f"https://api.daily.dev/rss/b/{daily_id}"
    feed = feedparser.parse(url)
    name = feed.feed.title
    print(f"[red]{name}")

    bookmarks = feed.entries

    for bookmark in bookmarks:
        link = bookmark.link.split("?utm_source")[0].strip()
        
        blog_base_link = link.split("/posts/")[0].strip().replace("app", "api") 
        
        blog_id = link.split("/posts/")[1].strip()
        
        blog_link = blog_base_link+"/r/"+blog_id
        print(f""" - [yellow][link={blog_link}]{bookmark.title}[/yellow] -> 
[cyan]{blog_link}[/link][/cyan]\n""")

else:
    print("[red]Please input a valid User ID!")
input()


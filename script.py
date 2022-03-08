import feedparser
from rich import print
import requests

print("[green]Enter your-daily-dev id: ", end="")
daily_id = input()

url = f"https://api.daily.dev/rss/b/{daily_id}"

feed = feedparser.parse(url)
name = feed.feed.title
print(f"[red]{name}")

bookmarks = feed.entries

for bookmark in bookmarks:
    blog_link = bookmark.link.split("?utm_source")[0].strip()
    print(f" - [yellow][link={blog_link}]{bookmark.title} -> {blog_link}[/link]")

input()

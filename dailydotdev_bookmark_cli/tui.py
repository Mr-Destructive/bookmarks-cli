from .bookmarks import get_bookmarks_list
from rich.panel import Panel
from textual.app import App
from textual.reactive import Reactive
from textual.widget import Widget
import random


class Hover(Widget):

    mouse_over = Reactive(False)

    def render(self) -> Panel:
        bookmarks = get_bookmarks_list()
        bookmark_list = len(bookmarks)
        bookmark = bookmarks[random.randint(0, bookmark_list - 1)]
        link = bookmark.link.split("?utm_source")[0].strip()
        blog_base_link = link.split("/posts/")[0].strip().replace("app", "api")
        blog_id = link.split("/posts/")[1].strip()
        blog_link = blog_base_link + "/r/" + blog_id
        return Panel(
            f"[green]{bookmark.title}[/]\n[link={blog_link}]{blog_link}[/link]",
            style=("on green" if self.mouse_over else ""),
        )


class HoverApp(App):
    async def on_mount(self) -> None:
        bookmarks_list = len(get_bookmarks_list())
        hovers = (Hover() for _ in range(5))
        await self.view.dock(*hovers, edge="top")


def tui_app():

    HoverApp.run(log="textual.log")

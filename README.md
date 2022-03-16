# Daily Dot Dev Bookmark's CLI

- View your daily.dev bookmarks from the CLI with Python

## Installation

To install the python package, install with pip or any other python package management tool of your choice.

```
pip install dailydotdev-bookmarks-cli
```

After installing the python package simply enter the command `bookmarks`,

```
bookmarks
```

This will prompt you to enter your daily.dev's bookmark RSS Feed URL, simply copy and paste as it is and finally the list of all your bookmarks will be displayed. 

![Daily Dev CLI](https://res.cloudinary.com/techstructive-blog/image/upload/v1647365911/blog-media/rf8nqohqu2k3orf4atso.gif)

### Edit a Existing RSS Feed URL link(id)

To change/edit an existing RSS Feed URL, you can enter the following command, and it will ask for the new URL, simply input that and you should be good to go.
```
bookmakrs --ch
```

### Delete the RSS Feed URL link(id)

To delete an existing RSS Feed URL, you can enter the following command, this will delete the file that holds your ID(URL for Bookmarks)

```
bookmakrs --rm
```

## Dependencies 

- [Feedparser](https://pypi.org/project/feedparser/)
- [Rich](https://pypi.org/project/rich/)

## TODO

- Add a TUI to view articles


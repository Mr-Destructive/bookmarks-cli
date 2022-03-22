# Daily Dot Dev Bookmark's CLI

[![PyPI version](https://badge.fury.io/py/dailydotdev-bookmark-cli.svg)](https://badge.fury.io/py/dailydotdev-bookmark-cli)

- View your daily.dev bookmarks from the CLI with Python
- A simple [Python Package](https://pypi.org/project/dailydotdev-bookmark-cli/)

## Installation

### In a Python Environment

To install the python package, install with pip or any other python package management tool of your choice.

```
pip install dailydotdev-bookmark-cli
```

After installing the python package simply enter the command `bookmarks`,

```
bookmarks
```

This will prompt you to enter your daily.dev's bookmark RSS Feed URL, simply copy and paste as it is and finally the list of all your bookmarks will be displayed. 

**NOTE: You do not have to enter the bookmark URL link again and again, it will be stored in a file. If you want to change it, you can modify or delete the file containing the id as explained later.**

https://user-images.githubusercontent.com/40317114/158827491-974249eb-1e04-469b-b907-87a8b3a75b0f.mp4

![Daily Dev CLI](https://res.cloudinary.com/techstructive-blog/image/upload/v1647365911/blog-media/rf8nqohqu2k3orf4atso.gif)

### With Docker

Using the [Dockerfile](https://github.com/Mr-Destructive/bookmarks-cli/blob/main/Dockerfile), you can simply execute the following commands:

```Dockerfile

FROM python:3

RUN pip install dailydotdev-bookmark-cli

```

Copy the Dockerfile in the your current working directory, build the image and run the image with interactive mode in bash.

```
docker build . -t bookmarkcli
```

```
docker run -it bookmarkcli bash
```

https://user-images.githubusercontent.com/40317114/158831643-01a10a27-6e78-4a0a-a791-62f2ccee50e1.mp4


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

### Terminal User Interface (using Textual and Rich)

If you want a TUI for your bookmarks, you have a option to display it using the `--tui` option in the package. 

**NOTE: It will only support the terminal systems with support the functionality of displaying rich content.**

```
bookmarks --tui
```

## Dependencies 

- [Feedparser](https://pypi.org/project/feedparser/)
- [Rich](https://pypi.org/project/rich/)
- [Textual](https://pypi.org/project/textual/)


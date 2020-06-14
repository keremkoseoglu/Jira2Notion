# Jira to Notion

This little program will capture a Jira issue and create a corresponding Notion subpage. Mac users can fetch the current issue from the foremost Chrome or Safari window. Others will get a popup asking for the issue number.

![Screenshot](/screenshot.png?raw=true "Screenshot")

## Installation

### OS independent

* Install Python First. The program won't work unless you install Python.  [Click here](https://www.python.org/downloads/mac-osx/) to install Python. [The official Python docs](https://docs.python.org/3/using/mac.html) are good enough to help you through the installation.

* Create a folder (presumably called j2n), and download all of the files in this repository there

* Open a terminal window, go to the j2n folder and type the following commands:

```
python3 -m venv venv
```

### Windows

If you are using Windows, continue with the following commands:

```
venv\Scripts\activate.bat
pip install notion
pip install jira
```

### Mac / Linux

If you are using Mac or Linux, continue with the following commands:

```
. venv/bin/activate
pip install notion
pip install jira
```

## Setup

### OS independent

* Ensure that you have [Notion](www.notion.so) and Jira accounts (doh)

* Create a new config file which looks like sample_config.txt. You are going to fill this file with your credentials. This file is pretty intuitive except the "notion" part:
  * token_v2: The value you should enter here is stored in a cookie called token_v2, which will be found in the browser you are logged in to Notion.
  * page: This is the URL of the page you are going to transfer your Jira issues to. Simply copy & paste the page URL from your browser.

* Ensure that config.py points to your own configuration file, which you have prepared above

* Modify notion_manager.py to change the content of your cards (optional)

### Mac OS (optional)

If you wish to fetch the Jira issue in your current browser window automatically; open "Chrome - Jira to Notion.applescript" or "Safari - Jira to Notion.applescript" using Apple Script Editor and export as j2n.app (or whatever name you like)

## Usage

### Windows

Simply run main.py. This will open a popup and ask for your Jira issue number. The issue you enter here will be read from Jira and transferred to Notion. You can run main.py from the command line by typing:

```
cd j2n
venv\Scripts\activate.bat
python3 main.py
```

Obviously, you should change the folder name j2n with your own installation path. Feel free to create a .bat file including this command for easy startup.

### Linux

Simply run main.py. This will open a popup and ask for your Jira issue number. The issue you enter here will be read from Jira and transferred to Notion. You can run main.py from the command line by typing:

```
cd j2n
. venv/bin/activate
python3 main.py
```

Obviously, you should change the folder name j2n with your own installation path. Feel free to create a .sh file including this command for easy startup.

### Mac OS

Follow the Linux steps for the popup.

If you have completed the optional Mac setup steps; you can also transfer the Jira issue in your current browser to Notion.
* Open a new issue in Chrome or Safari
* Run j2n.app

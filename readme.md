# Jira to Notion

This little Mac program will capture the current issue in the foremost Chrome or Safari window, and create a corresponding Notion subpage.

### Prerequisites:

* Install Python First. The program won't work unless you install Python!

* [Click here](https://www.python.org/downloads/mac-osx/) to install Python. [The official Python docs](https://docs.python.org/3/using/mac.html) are good enough to help you through the installation.

### Usage:


* Create a new config file which looks like sample_config.txt
* Ensure that config.py points to your own configuration file
* Modify notion_manager.py to change the content of your cards (optional)
* Open "Chrome - Jira to Notion.applescript" or "Safari - Jira to Notion.applescript" using Apple Script Editor and export as j2n.app (or whatever name you like)

To test it:

* Open a new issue in Chrome or Safari
* Run j2n.app

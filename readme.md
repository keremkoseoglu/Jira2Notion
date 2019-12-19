# Jira to Notion

This little Mac program will capture the current issue in the foremost Chrome window, and create a corresponding Notion subpage.

To use this program;
- Create a new config file which looks like sample_config.txt
- Ensure that config.py points to your own configuration file
- Modify notion_manager.py to change the content of your cards (optional)
- Open Chrome - Jira to Notion.applescript using Apple Script Editor and export as j2n.app (or whatever name you like)

To test it;
- Open a new issue in Chrome
- Run j2n.app
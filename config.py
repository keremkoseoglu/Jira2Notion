""" Configuration module """
import json
import os


class Config:
    """ Configuration class """
    _CONFIG_FILE = "/Users/kerem/Documents/etc/config/jira2notion.txt" # Check sample_config.txt

    def __init__(self):
        # Read text file
        script_dir = os.path.dirname(__file__)
        config_path = os.path.join(script_dir, self._CONFIG_FILE)
        txt_file = open(config_path, "r")
        txt_content = txt_file.read()
        txt_file.close()
        json_data = json.loads(txt_content)

        # Parse contents
        self.notion_token_v2 = json_data["config"]["notion"]["token_v2"]
        self.notion_page = json_data["config"]["notion"]["page"]
        self.notion_comment_count = int(json_data["config"]["note"]["comment_count"])

        self.jira_base_url = json_data["config"]["jira"]["base_url"]
        self.jira_username = json_data["config"]["jira"]["username"]
        self.jira_password = json_data["config"]["jira"]["password"]

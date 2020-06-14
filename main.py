""" Program entry point """
import sys
from config import Config
from notion_manager import NotionManager
from jira_manager import JiraManager
from gui import get_value_by_popup

def sync_issue(issue_code: str):
    """ Reads the given issue from Jira and transfers to Notion """
    my_config = Config()
    my_jira_manager = JiraManager(my_config)
    my_notion_manager = NotionManager(my_config)

    issue = my_jira_manager.get_issue(issue_code)
    my_notion_manager.create_page(issue, my_jira_manager)
    sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        desired_issue = sys.argv[1]
        sync_issue(desired_issue)
    else:
        get_value_by_popup(sync_issue)

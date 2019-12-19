from config import Config
from notion_manager import NotionManager
from jira_manager import JiraManager
import sys

desired_issue = sys.argv[1]
#desired_issue="VOL-6370"

my_config = Config()
my_jira_manager = JiraManager(my_config)
my_notion_manager = NotionManager(my_config)

issue = my_jira_manager.get_issue(desired_issue)
my_notion_manager.create_page(issue, my_jira_manager)
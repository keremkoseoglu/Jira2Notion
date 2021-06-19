""" Notion Data Access Object module """
from abc import ABC, abstractmethod
from jira.resources import Issue
from jira_manager import JiraManager
from config import Config

class NotionDAO(ABC):
    """ Notion Data Access Object class
    This abstract class follows the logic of the well known
    Data Access Object design pattern. Google it for details.
    """
    def __init__(self, c: Config):
        self._config = c

    @abstractmethod
    def create_page(self, issue: Issue, jira_man: JiraManager, with_comments: bool = False):
        """ Creation of a new Notion page """
        pass

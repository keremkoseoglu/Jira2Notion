""" Jira manager module """
from jira import JIRA


class JiraManager:
    """ Jira manager class """
    _ISSUE_URL_DECORATOR = "/browse/"

    def __init__(self, Config):
        self._config = Config

        options = {
            "server": self._config.jira_base_url
        }
        self._jira = JIRA(
            options,
            basic_auth=(self._config.jira_username, self._config.jira_password))

    def get_issue(self, issue_key: str):
        """ Returns the issue having the key issue_key """
        issue = self._jira.issue(issue_key)
        return issue

    def get_url(self, issue_key: str) -> str:
        """ Returns the issue URL of the given issue key """
        return self._config.jira_base_url + self._ISSUE_URL_DECORATOR + issue_key

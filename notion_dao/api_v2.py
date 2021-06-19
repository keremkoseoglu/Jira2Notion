""" Notion official API module """
import json
import requests
from requests.structures import CaseInsensitiveDict
from jira.resources import Issue
from config import Config
from jira_manager import JiraManager
from notion_dao.dao import NotionDAO

_PAGE_URL = "https://api.notion.com/v1/pages"

class APIv2(NotionDAO):
    """ Official Notion API implementation """
    def __init__(self, c: Config):
        super().__init__(c)

    def create_page(self, issue: Issue, jira_man: JiraManager, with_comments: bool = False):
        """ Creation of a new Notion page """
        global _PAGE_URL

        # Get details from JIRA
        try:
            title_key = issue.fields.parent.key
        except Exception:
            title_key = issue.key

        title = title_key + " - " + issue.fields.summary
        link = jira_man.get_url(issue.key)

        description = issue.fields.description
        if description is None:
            description = "(No description)"

        # Post to Notion
        headers = {"Content-Type": "application/json",
                   "Notion-Version": self._config.notion_official_version,
                   "Authorization": "Bearer " + self._config.notion_official_token}

        body = {
            "parent": { "database_id": "9530bb3c443d47fcadc6ecc566a6b364" },
            "properties": {
            "title": { "title": [{ "text": { "content": title } }] }
            },
            "children": [
                {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": { "text": [{ "type": "rich_text", "text": { "content": link, "link": { "url": link } } }] }
                },
                {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": { "text": [{ "type": "text", "text": { "content": description } } ] }
                },
                {
                    "object": "block",
                    "type": "heading_1",
                    "heading_1": { "text": [{ "type": "text", "text": { "content": "İşler" } } ] }
                },
                {
                    "object": "block",
                    "type": "to_do",
                    "to_do": { "text": [{ "type": "text", "text": { "content": "..." } } ] }
                },
                {
                    "object": "block",
                    "type": "heading_1",
                    "heading_1": { "text": [{ "type": "text", "text": { "content": "Request notu" } } ] }
                },
                {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": { "text": [{ "type": "text", "text": { "content": "..." } } ] }
                },
                {
                    "object": "block",
                    "type": "heading_1",
                    "heading_1": { "text": [{ "type": "text", "text": { "content": "Soft Config" } } ] }
                },
                {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": { "text": [{ "type": "text", "text": { "content": "..." } } ] }
                },
                {
                    "object": "block",
                    "type": "heading_1",
                    "heading_1": { "text": [{ "type": "text", "text": { "content": "Yorum" } } ] }
                },
                {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": { "text": [{ "type": "text", "text": { "content": "..." } } ] }
                }
            ]
        }

        response = requests.post(_PAGE_URL, data=json.dumps(body), headers=headers)

        if response.status_code != 200:
            raise Exception("Notion API error: " + response.reason)

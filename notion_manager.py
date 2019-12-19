from config import Config
from jira.resources import Issue
from jira_manager import JiraManager
from notion.client import NotionClient
from notion.block import PageBlock
from notion.block import TextBlock
from notion.block import HeaderBlock
from notion.block import TodoBlock
from notion.block import BookmarkBlock
from notion.block import CodeBlock
from notion.block import SubheaderBlock
from notion.block import DividerBlock
from notion.block import QuoteBlock


class NotionManager:

    def __init__(self, c: Config):
        self._config = c
        self._client = NotionClient(token_v2=self._config.notion_token_v2)
        self._page = self._client.get_block(self._config.notion_page)

    def create_page(self, issue: Issue, jira_man: JiraManager):

        try:
            title_key = issue.fields.parent.key
        except:
            title_key = issue.key

        title = title_key + " - " + issue.fields.summary

        subpage = self._page.children.add_new(PageBlock, title=title)

        subpage.children.add_new(BookmarkBlock, link=jira_man.get_url(issue.key), title=issue.key, description=issue.fields.summary)
        subpage.children.add_new(TextBlock, title=issue.fields.description)
        subpage.children.add_new(DividerBlock)
        subpage.children.add_new(HeaderBlock, title="İşler")
        subpage.children.add_new(TodoBlock, title="İlerlet")
        subpage.children.add_new(TodoBlock, title="İncele")
        subpage.children.add_new(TodoBlock, title="Todo")
        subpage.children.add_new(TodoBlock, title="Activate")
        subpage.children.add_new(TodoBlock, title="EPC & Release")
        subpage.children.add_new(TodoBlock, title="İlerlet & not yaz")
        subpage.children.add_new(DividerBlock)
        subpage.children.add_new(HeaderBlock, title="Bittiğinde Jira'ya yazılacak")
        subpage.children.add_new(SubheaderBlock, title="Request notu")
        subpage.children.add_new(TextBlock, title="...")
        subpage.children.add_new(SubheaderBlock, title="Yorum")
        subpage.children.add_new(TextBlock, title="...")
        subpage.children.add_new(DividerBlock)
        subpage.children.add_new(HeaderBlock, title="Mevcut yorumlar")

        for i in range(self._config.notion_comment_count):
            comment_idx = issue.fields.comment.total - 1 - i
            if comment_idx < 0:
                break
            current_comment = issue.fields.comment.comments[comment_idx]
            subpage.children.add_new(QuoteBlock, title=current_comment.body)
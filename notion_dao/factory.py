""" Notion object factory module """
from config import Config
from notion_dao.dao import NotionDAO
from notion_dao.api_v1 import APIv1
from notion_dao.api_v2 import APIv2

def get_instance(c: Config) -> NotionDAO:
    """ Returns a new notion object """
    if c.notion_official_configured:
        result = APIv2(c)
    else:
        result = APIv1(c)
    return result

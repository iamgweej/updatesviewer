import requests
import xml.etree.ElementTree as ET

from typing import Iterable
from datetime import datetime
from email.utils import parsedate_to_datetime

import fetcher

class RSSUpdate(fetcher.Update):
    
    def __init__(self, title: str, link: str, description: str, pub_date: datetime):
        
        self._title = title
        self._link = link
        self._description = description
        self._pub_date = pub_date

    @property
    def title(self):
        return self._title
    
    @property
    def link(self):
        return self._link
    
    @property
    def description(self):
        return self._description
    
    @property
    def pub_date(self) -> datetime:
        return self._pub_date


class RSSFetcher(fetcher.Fetcher):
    """
    Fetches updates from RSS channels.
    """

    def __init__(self, url: str):    
        self._url = url

    def _build_item(self, item: ET.Element) -> RSSUpdate:
        
        title = item.find('title')
        assert title is not None # TODO: change to raise exception
        
        link = item.find('link')
        assert link is not None # TODO: change to raise exception
        
        description = item.find('description')
        assert description is not None # TODO: change to raise exception
        
        pub_date = item.find('pubDate')
        assert pub_date is not None # TODO: change to raise exception
        dt_pubdate = parsedate_to_datetime(pub_date.text) # TODO add try-catch

        return RSSUpdate(title.text, link.text, description.text, dt_pubdate)

    def fetch(self) -> Iterable[RSSUpdate]:
        
        resp = requests.get(self._url)
        if resp.status_code != 200: # Check that the request went through
            pass # TODO: raise appropriate exception

        root = ET.fromstring(resp.text) # TODO: check if this raises, im too tired right now

        # TODO: change these assertions to ifs and throws
        assert root.tag == 'rss' # TODO: maybe add root.attrib.get('version') == '2.0' 

        channel = root.find('channel')
        assert channel is not None # TODO: check this to a throw of an actual exception
        
        yield from (self._build_item(item) for item in channel.findall('item'))

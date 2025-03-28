# -*- coding: utf-8 -*-

import logging

from bs4 import BeautifulSoup, Tag

from lncrawl.models import Chapter
from lncrawl.templates.browser.chapter_only import ChapterOnlyBrowserTemplate

logger = logging.getLogger(__name__)


class SnowyCodexCrawler(ChapterOnlyBrowserTemplate):
    base_url = "https://snowycodex.com/"

    def initialize(self) -> None:
        self.cleaner.bad_css.update(
            {
                ".wpulike",
                ".sharedaddy",
                ".wpulike-default",
                '[style="text-align:center;"]',
            }
        )
        self.cleaner.bad_tag_text_pairs.update(
            {
                "p": r"[\u4E00-\u9FFF]+",
            }
        )

    def parse_title(self, soup: BeautifulSoup) -> str:
        tag = soup.select_one(".entry-content h2")
        assert isinstance(tag, Tag)
        return tag.text.strip()

    def parse_cover(self, soup: BeautifulSoup) -> str:
        tag = soup.select_one(".entry-content img")
        assert isinstance(tag, Tag)
        if tag.has_attr("data-src"):
            return self.absolute_url(tag["data-src"])
        elif tag.has_attr("src"):
            return self.absolute_url(tag["src"])

    def parse_authors(self, soup: BeautifulSoup):
        tag = soup.find("strong", string="Author:")
        assert isinstance(tag, Tag)
        yield tag.next_sibling.text.strip()

    def select_chapter_tags(self, soup: BeautifulSoup):
        yield from soup.select(".entry-content a[href*='/chapter']")

    def parse_chapter_item(self, tag: Tag, id: int) -> Chapter:
        return Chapter(
            id=id,
            title=tag.text.strip(),
            url=self.absolute_url(tag["href"]),
        )

    def select_chapter_body(self, soup: BeautifulSoup) -> Tag:
        return soup.select_one(".entry-content")

import unittest
from extract_markdown_links import extract_markdown_links

class TestExtractMarkdownLinks(unittest.TestCase):
    def test_extract_markdown_link(self):
        matches = extract_markdown_links(
            "This is text with a link [this is a link](https://i.imgur.com)"
        )
        self.assertListEqual([("this is a link", "https://i.imgur.com")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        
        self.assertListEqual([("to boot dev", "https://www.boot.dev"),
                              ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)


    def test_extract_markdown_link_Failure(self):
        matches = extract_markdown_links(
            "This is text with a link [this is a link(https://i.imgur.com)"
        )
        
        self.assertListEqual([], matches)

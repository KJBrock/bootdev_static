import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_represent_value(self):
        node = HTMLNode("a", "foobar")
        self.assertEqual(f"{node}", "<a>foobar</a>")
        
    def test_represent_children(self):
        node = HTMLNode("block", None, [HTMLNode("a", "foobar"), HTMLNode("p", "baz")])
        self.assertEqual(f"{node}", "<block>2 children</block>")

    def test_represent_value_with_props(self):
        node = HTMLNode("a", "foobar", None, { "href" : "http://someplace.test", "target" : "something"})
        self.assertEqual(f"{node}", "<a href=\"http://someplace.test\" target=\"something\">foobar</a>")
        



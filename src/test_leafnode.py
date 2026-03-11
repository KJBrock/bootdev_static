import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "Hello, world!")
        self.assertEqual(node.to_html(), "<h1>Hello, world!</h1>")

    def test_leaf_to_html_li(self):
        node = LeafNode("li", "Hello, world!")
        self.assertEqual(node.to_html(), "<li>Hello, world!</li>")

    def test_leaf_value_error(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError) as ve:
            node.to_html()
        
        self.assertEqual(f"{ve.exception}","all leaf nodes must have a value")
         
    def test_leaf_node_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

        html = node.to_html()
        self.assertEqual(html, '<a href="https://www.google.com">Click me!</a>')
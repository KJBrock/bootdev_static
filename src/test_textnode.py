import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node.", TextType.BOLD)
        node2 = TextNode("This is a text node.", TextType.BOLD)
        self.assertEqual(node1, node2)
        
    def test_different_text_noteq(self):
        node1 = TextNode("This is a text node.", TextType.BOLD)
        node2 = TextNode("This is another text node.", TextType.BOLD)
        self.assertNotEqual(node1, node2)
        
    def test_different_types_noteq(self):
        node1 = TextNode("This is a text node.", TextType.BOLD)
        node2 = TextNode("This is a text node.", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_emptyurl_noteq_defaulturl(self):
        node1 = TextNode("This is a text node.", TextType.BOLD, "")
        node2 = TextNode("This is a text node.", TextType.BOLD)
        self.assertNotEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()
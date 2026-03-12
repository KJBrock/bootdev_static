import unittest

from textnode import TextNode, TextType
from leafnode import LeafNode
from htmlnode import HTMLNode

def text_node_to_html_node(node):
    tag = None
    props = None
    match node.text_type:
        case TextType.TEXT:
                return LeafNode(None, node.text)

        case TextType.BOLD:
            return LeafNode("b", node.text)
            
        case TextType.ITALIC:
            return LeafNode("i", node.text)
            
        case TextType.CODE:
            return LeafNode("code", node.text)
            
        case TextType.LINK:
            return LeafNode("a", node.text, { "href" : node.url })
    
        case TextType.IMAGE:
            return LeafNode("img", "", {"src" : node.url,
                                        "alt" : node.text})
    
    
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
        
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is image alt text", TextType.IMAGE, "https://somecom.com/foo.jpeg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertTrue(html_node.props is not None)
        self.assertEqual(html_node.props["src"], "https://somecom.com/foo.jpeg")
        self.assertEqual(html_node.props["alt"], "This is image alt text")
        
    def test_url(self):
        node = TextNode("This is anchor text", TextType.LINK, "https://somecom.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is anchor text")        
        self.assertTrue(html_node.props is not None)
        self.assertEqual(html_node.props["href"], "https://somecom.com")
        


if __name__ == "__main__":
    unittest.main()
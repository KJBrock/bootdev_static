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

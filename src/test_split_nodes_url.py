import unittest
from textnode import TextNode, TextType
from split_nodes_url import split_nodes_image, split_nodes_link

class TestSplitNodes(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
        
    def test_split_links(self):
        test_node_list = [TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
                                   TextType.TEXT)]
        
        new_nodes = split_nodes_link(test_node_list)
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
            ], 
            new_nodes)

    def test_split_links_not_images(self):
        test_node_list = [TextNode("This is text with a link ![image](https://i.imgur.com/zjjcJKZ.png) and [to youtube](https://www.youtube.com/@bootdotdev)",
                                   TextType.TEXT)]
        
        new_nodes = split_nodes_link(test_node_list)
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("![image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT),
                TextNode(" and ", TextType.TEXT),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
            ], 
            new_nodes)




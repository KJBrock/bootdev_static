import unittest

from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
        def test_no_delimiter(self):
            node = TextNode("This is a text node.", TextType.TEXT)
            new_nodes = split_nodes_delimiter([node], "*", TextType.BOLD)
            self.assertEqual(len(new_nodes), 1)
            self.assertEqual(new_nodes[0], node)

        def test_unbalanced_delimiter(self):
            node = TextNode("This is a *text* node, but with a *bad delimiter balance!", TextType.TEXT)
            new_nodes = []
            with self.assertRaises(Exception) as ve:
                new_nodes = split_nodes_delimiter([node], "*", TextType.BOLD)
                
            self.assertEqual(f"{ve.exception}",f"unmatched delimiter '*'")

        def test_one_delimited_block(self):
            node = TextNode("This is a *text* node.", TextType.TEXT)
            new_nodes = split_nodes_delimiter([node], "*", TextType.BOLD)
            self.assertEqual(len(new_nodes), 3)
            self.assertEqual(new_nodes, [TextNode("This is a ", TextType.TEXT),
                                         TextNode("text", TextType.BOLD),
                                         TextNode(" node.", TextType.TEXT)])
            
        def test_delimiter_at_start(self):
            node = TextNode("*This* is a text node.", TextType.TEXT)
            new_nodes = split_nodes_delimiter([node], "*", TextType.BOLD)
            self.assertEqual(len(new_nodes), 2)
            self.assertEqual(new_nodes, [TextNode("This", TextType.BOLD),
                                         TextNode(" is a text node.", TextType.TEXT)])
            
        def test_adjacent_delimited_blocks(self):
            node = TextNode("This is a *text**node*.", TextType.TEXT)
            new_nodes = split_nodes_delimiter([node], "*", TextType.BOLD)
            self.assertEqual(len(new_nodes), 4)
            self.assertEqual(new_nodes, [TextNode("This is a ", TextType.TEXT),
                                         TextNode("text", TextType.BOLD),
                                         TextNode("node", TextType.BOLD),
                                         TextNode(".", TextType.TEXT)])

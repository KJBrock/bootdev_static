import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
        
    def test_to_html_with_two_branches(self):
        grandchild_node1 = LeafNode("h1", "grandchild")
        grandchild_node2 = LeafNode("p", "grandchild")
        grandchild_node3 = LeafNode("h2", "grandchild")
        child_node1 = ParentNode("span", [grandchild_node1, grandchild_node2])
        child_node2 = ParentNode("span", [grandchild_node3])
        parent_node = ParentNode("div", [child_node1, child_node2])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><h1>grandchild</h1><p>grandchild</p></span><span><h2>grandchild</h2></span></div>",
        )
        
    def test_to_html_with_children_and_props(self):
        props = {"href" : "https://foo.org",
                 "cookie" : "f049jfri94"}
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], props)
        self.assertEqual(parent_node.to_html(), "<div href=\"https://foo.org\" cookie=\"f049jfri94\"><span>child</span></div>")

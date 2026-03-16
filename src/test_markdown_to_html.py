import unittest
from parentnode import ParentNode
from leafnode import LeafNode
from markdown_to_html import markdown_to_html_node

class TestMarkDownToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )


    def test_unordered_list(self):
        md = """- This is list item #1
- And this is list item #2
- This list item has some **bold** text in it
- And this has **bold** and _italic_
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        
        self.assertEqual(
            html,
            "<div><ul><li>This is list item #1</li><li>And this is list item #2</li><li>This list item has some <b>bold</b> text in it</li><li>And this has <b>bold</b> and <i>italic</i></li></ul></div>",
        )



    def test_ordered_list(self):
        md = """
1. This is list item #1
2. And this is list item #2
30. This list item has some **bold** text in it, and looks like we skipped some to check multi-digit entries.
400. And this has **bold** and _italic_
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
    
        self.assertEqual(
            html,
            "<div><ol><li>This is list item #1</li><li>And this is list item #2</li><li>This list item has some <b>bold</b> text in it, and looks like we skipped some to check multi-digit entries.</li><li>And this has <b>bold</b> and <i>italic</i></li></ol></div>",
        )

    def test_h1(self):
        md = """
# This is the title!

1. This is list item #1
2. And this is list item #2
30. This list item has some **bold** text in it, and looks like we skipped some to check multi-digit entries.
400. And this has **bold** and _italic_
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>This is the title!</h1><ol><li>This is list item #1</li><li>And this is list item #2</li><li>This list item has some <b>bold</b> text in it, and looks like we skipped some to check multi-digit entries.</li><li>And this has <b>bold</b> and <i>italic</i></li></ol></div>",
        )

    def test_blockquote(self):
        md = """
> "I am in fact a Hobbit in all but size."
>
> -- J.R.R. Tolkien
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        print("============ HTML ")
        print(f"{html}")
        print("============ Expected")
        print("<div><blockquote>\"I am in fact a Hobbit in all but size.\" -- J.R.R. Tolkien</blockquote></div>")
        print("===================")

        self.assertEqual(
            html,
            "<div><blockquote>\"I am in fact a Hobbit in all but size.\" -- J.R.R. Tolkien</blockquote></div>",
        )


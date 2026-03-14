import unittest

from blocktype import block_to_block_type, BlockType

paragraph_block = "This is a paragraph.\nWith two lines"
heading1_block = "# This is a top layer heading"
heading6_block = "###### This is an h6"
too_long_heading_block = "####### This is an h6"
code_block = "```\ndef square(n):\n\treturn n * n\n```"
quote_block = ">This is a quote.\n> There are multiple lines in the quote.\n>   They look a little different"
ordered_list_block = "1. This is an ordered list.\n2. With two items."
unordered_list_block = "- This is an unordered list.\n- Another item in the list."

class TestBlockType(unittest.TestCase):
    def test_paragraph(self):
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(paragraph_block))
         
    def test_heading1(self):
        self.assertEqual(BlockType.HEADING, block_to_block_type(heading1_block))

    def test_heading6(self):
        self.assertEqual(BlockType.HEADING, block_to_block_type(heading6_block))

    def test_too_long_heading7(self):
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(too_long_heading_block))

    def test_code(self):
        self.assertEqual(BlockType.CODE, block_to_block_type(code_block))

    def test_quote(self):
        self.assertEqual(BlockType.QUOTE, block_to_block_type(quote_block))

    def test_ordered_list(self):
        self.assertEqual(BlockType.ORDERED_LIST, block_to_block_type(ordered_list_block))

    def test_unordered_list(self):
        self.assertEqual(BlockType.UNORDERED_LIST, block_to_block_type(unordered_list_block))

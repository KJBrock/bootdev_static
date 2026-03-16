import re
from markdown_to_blocks import markdown_to_blocks
from text_to_textnodes import text_to_textnodes
from text_node_to_html_node import text_node_to_html_node
from textnode import TextNode, TextType
from parentnode import ParentNode
from leafnode import LeafNode

from blocktype import *
from my_regexes import *
    
def md_block_to_html(md_block, block_type):
    html_nodes = []

    match block_type:
        case BlockType.PARAGRAPH:
            paragraph = md_block.replace("\n", " ")
            html_children = [text_node_to_html_node(node) for node in text_to_textnodes(paragraph)]
            html_node = ParentNode("p", html_children)
            html_nodes.append(html_node)                                
    
        case BlockType.HEADING:
            match = re.match(HEADING_COUNT_REGEX, md_block)
            if not match:
                raise Exception("error parsing header block")
                    
            header_count = len(match.group(1))
            header_block = md_block[header_count:] # Strip off the '#' characters and the space
                    
            html_children = [text_node_to_html_node(node) for node in text_to_textnodes(header_block)]
            html_node = ParentNode(f"h{header_count-1}", html_children)
            html_nodes.append(html_node)                
            
        case BlockType.CODE:
            code_block = md_block[4:-3] # skip leading ```\n and trailing ```
            html_children = [text_node_to_html_node(node) for node in text_to_textnodes(code_block , False)]
            code_node = ParentNode(f"code", html_children)
            html_node = ParentNode(f"pre", [code_node])
            html_nodes.append(html_node)                
            
        case BlockType.QUOTE:
            lines = md_block.split("\n")
            quote_text = " ".join([l[1:].strip() for l in lines if len(l) > 1])
            html_children = [text_node_to_html_node(node) for node in text_to_textnodes(quote_text)]
            html_node = ParentNode(f"blockquote", html_children)
            html_nodes.append(html_node)                
            
        case BlockType.UNORDERED_LIST:
            list_items = md_block.split("\n")
            html_children = []
            for item in list_items:
                stripped = item[2:] # leading "- "
                if len(stripped) > 0:
                    item_children = [text_node_to_html_node(node) for node in text_to_textnodes(stripped)]
                    list_item = ParentNode("li", item_children)
                    html_children.append(list_item)
            html_node = ParentNode(f"ul", html_children)
            html_nodes.append(html_node)                
            
        case BlockType.ORDERED_LIST:
            list_items = md_block.split("\n")
            html_children = []
            for item in list_items:
                prefix_match = re.match(OLIST_PREFIX_LEN_REGEX, item)
                prefix_length = len(prefix_match.group(1))
                stripped = item[prefix_length:] # leading "\d+. " Variable number of digits possible for large lists.
                if len(stripped) > 0:
                    item_children = [text_node_to_html_node(node) for node in text_to_textnodes(stripped)]
                    list_item = ParentNode("li", item_children)
                    html_children.append(list_item)
            html_node = ParentNode(f"ol", html_children)
            html_nodes.append(html_node)                
            
        case _: 
            raise ValueError(f"unknown block type {block_type}")

    return html_nodes
    
       
def markdown_to_html_node(markdown_text):
    md_blocks = markdown_to_blocks(markdown_text)
    
    html_nodes = []
    for md_block in md_blocks:
        
        block_type = block_to_block_type(md_block)
        new_nodes = md_block_to_html(md_block, block_type)
        html_nodes.extend(new_nodes)
        
    root_node = ParentNode("div", html_nodes)
    return root_node
        
            
            
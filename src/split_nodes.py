import re
from textnode import TextNode, TextType
from my_regexes import *

def split_node(node, regex, match_type):
    new_nodes = []
    components = re.split(SPLIT_RE, node.text)
    if len(components) == 1: # No match found
        new_nodes.append(node)
        return new_nodes
                
    for component in components:
        if len(component) == 0:
            continue
        urlinfo = re.findall(regex, component)
        if not urlinfo:# or len(urlinfo) == 0:
            new_nodes.append(TextNode(component, TextType.TEXT))
        else:
            new_nodes.append(TextNode(urlinfo[0][0], match_type, urlinfo[0][1]))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        new_nodes.extend(split_node(node, LINK_RE, TextType.LINK))
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        new_nodes.extend(split_node(node, IMAGE_RE, TextType.IMAGE))
    return new_nodes


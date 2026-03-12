from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter
from split_nodes_url import split_nodes_image, split_nodes_link

DELIMITERS = {"**" : TextType.BOLD,
              "_" : TextType.ITALIC, 
              "`" : TextType.CODE}

def get_splitter(delimiter, text_type):
    def splitter(node):
        return split_nodes_delimiter(node, delimiter, text_type)
    return splitter

def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    
    operations = []
    for (d, t) in DELIMITERS.items():
        operations.append(get_splitter(d,t))
    operations.append(split_nodes_image)
    operations.append(split_nodes_link)
    
    new_nodes = [node]
    for op in operations:
        new_nodes = op(new_nodes)
        
    return new_nodes  
    
                
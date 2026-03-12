from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        fragments = old_node.text.split(delimiter)
        if len(fragments) == 1: # No delimiters found
            new_nodes.append(old_node)
            continue
        
        if len(fragments) % 2 == 0: # unbalanced delimiter
            raise Exception(f"unmatched delimiter \'{delimiter}\'")

        for index in range (len(fragments)):
            if len(fragments[index]) == 0: # Empty.  Either a delimiter starting a block of text or an empty delimiter pair.
                continue
            
            if index % 2 == 0: # it's a text fragment
                new_nodes.append(TextNode(fragments[index], TextType.TEXT))
            else: # it's a delimited fragment
                new_nodes.append(TextNode(fragments[index], text_type))
        
    return new_nodes
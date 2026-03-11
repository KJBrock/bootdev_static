from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)
        
    def to_html(self):
        if self.children is None:
            raise ValueError("all parent nodes must have children")
        
        if self.tag is None:
            raise ValueError("all parent nodes must have a tag")

        html_prefix = f"<{self.tag}{self.props_to_html()}>"
        html_suffix = f"</{self.tag}>"
        
        children = [f"{child.to_html()}" for child in self.children]
        return html_prefix + "".join(children) + html_suffix
    
    

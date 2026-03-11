from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)
        
    def to_html(self):
        if self.value is None:
            raise ValueError("all leaf nodes must have a value")
        
        if self.tag is None:
            return self.value
        
        return f"{self}"

    def __repr__(self):
        value_str = ""
        if self.value is not None:
            value_str = self.value

        return f"<{self.tag}{self.props_to_html()}>{value_str}</{self.tag}>"


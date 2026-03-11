class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children # []
        self.props = props # {}
        
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None or len(self.props) == 0:
            return ""
        
        return " " + " ".join([f"{k}=\"{v}\"" for k,v in self.props.items()])
    
    def __repr__(self):
        value_str = ""
        if self.value is not None:
            value_str = self.value
        
        if self.value is not None:
            return f"<{self.tag}{self.props_to_html()}>{value_str}</{self.tag}>"
        else:
            return f"<{self.tag}{self.props_to_html()}>{len(self.children)} children</{self.tag}>"
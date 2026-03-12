import re

LINK_RE=r"\[(.*?)\]\((http(s?):\/\/(\w+)((\.\w+)*)(\/[@?\w]+)*)\)"

def extract_markdown_links(text):
    links = re.findall(LINK_RE, text)
    print(f"extract links: ---> {links}")

    return [(link[0], link[1]) for link in links]
    
    
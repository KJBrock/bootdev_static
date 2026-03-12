import re
from my_regexes import *

def extract_markdown_links(text):
    links = re.findall(LINK_RE, text)
    return [(link[0], link[1]) for link in links]


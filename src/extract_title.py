import re
from my_regexes import *

def extract_title(markdown):
    title_match = re.findall(TITLE_MATCH_REGEX, markdown)
    if not title_match:
        raise Exception("no title in markdown")

    title = title_match[0]
     
    return title.strip()
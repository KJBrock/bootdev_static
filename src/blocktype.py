from enum import Enum
import re
from my_regexes import *

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

REGEX_TO_BLOCK_TYPE = {
    HEADING_BLOCK_RE : BlockType.HEADING,
    CODE_BLOCK_RE  : BlockType.CODE,
    QUOTE_BLOCK_RE  : BlockType.QUOTE,
    ULIST_BLOCK_RE  : BlockType.UNORDERED_LIST,
    OLIST_BLOCK_RE  : BlockType.ORDERED_LIST, 
}
    
def block_to_block_type(text):
    block_type = BlockType.PARAGRAPH
    for k in REGEX_TO_BLOCK_TYPE.keys():
        match = re.fullmatch(k, text)
        if match is not None:
            block_type = REGEX_TO_BLOCK_TYPE[k]
            break

    return block_type
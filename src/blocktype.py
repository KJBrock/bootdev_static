from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

REGEX_TO_BLOCK_TYPE = {
    r"#{1,6} .*" : BlockType.HEADING,
    r"```\n.*(\n.*)*```" : BlockType.CODE,
    r"(^>[^\n]*)(\n>[^\n]*)*" : BlockType.QUOTE,
    r"(^- [^\n]*)(\n- [^\n]*)" : BlockType.UNORDERED_LIST,
    r"(^\d\. [^\n]*)(\n\d\. .*)*" : BlockType.ORDERED_LIST,    
}
    
def block_to_block_type(text):
    block_type = BlockType.PARAGRAPH
    for k in REGEX_TO_BLOCK_TYPE.keys():
        match = re.fullmatch(k, text)
        if match is not None:
            block_type = REGEX_TO_BLOCK_TYPE[k]
            break
    return block_type
SPLIT_RE = r"(!?\[.*?\]\(.*?\))"
IMAGE_RE = r"!\[(.*?)\]\((.*?)\)"

# Link needs to explicitly exclude the !, otherwise is would also match the image link
LINK_RE  = r"(?<![!])\[(.*?)\]\((.*?)\)" 

HEADING_COUNT_REGEX = r"(#{1,6})"
OLIST_PREFIX_LEN_REGEX = r"(\d+\. )"

HEADING_BLOCK_RE = r"#{1,6} .*"
CODE_BLOCK_RE = r"```\n.*(\n.*)*```"
QUOTE_BLOCK_RE = r"(>[^\n]*)(\n>[^\n]*)*"
ULIST_BLOCK_RE = r"(- [^\n]*)(\n- [^\n]*)*"
OLIST_BLOCK_RE = r"(\d+\. [^\n]*)(\n\d+\. [^\n]*)*"

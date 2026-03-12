SPLIT_RE = r"(!?\[.*?\]\(.*?\))"
IMAGE_RE = r"!\[(.*?)\]\((.*?)\)"

# Link needs to explicitly exclude the !, otherwise is would also match the image link
LINK_RE  = r"(?<![!])\[(.*?)\]\((.*?)\)" 


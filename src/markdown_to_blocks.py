

def markdown_to_blocks(markdown):
    candidate_blocks = markdown.split("\n\n")

    blocks = []
    for block in candidate_blocks:
        if len(block) == 0:
            continue
        stripped = block.strip()
        if len(stripped) == 0:
            continue
        
        blocks.append(stripped)

    return blocks
    
    
    
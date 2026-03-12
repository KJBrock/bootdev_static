import re
from my_regexes import *

def extract_markdown_images(text):
    images = re.findall(IMAGE_RE, text)
    match = re.match(IMAGE_RE, text)
    return [(image[0], image[1]) for image in images]
    

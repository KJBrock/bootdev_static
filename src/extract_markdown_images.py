import re

IMAGE_RE=r"!\[(.*?)\]\((http(s?):\/\/(\w+)((\.\w+)*)(\/[@?\w]+)*(\.\w+)?)\)"

def extract_markdown_images(text):
    images = re.findall(IMAGE_RE, text)
    print(f"extract images: ---> {images}")
    return [(image[0], image[1]) for image in images]
    

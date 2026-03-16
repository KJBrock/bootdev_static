import os
from htmlnode import HTMLNode
from markdown_to_html import markdown_to_html_node
from extract_title import extract_title
from copy_recurse import create_dir_if_needed
        
def generate_page(from_path, template_path, dest_path, base_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Read the markdown file at from_path and store the contents in a variable.
    md = ""
    with open(from_path, "r") as f:
        md = f.read()    

    # Read the template file at template_path and store the contents in a variable.
    template = ""
    with open(template_path, "r") as f:
        template = f.read()    
    
    # Use your markdown_to_html_node function and .to_html() method to convert the markdown file to an HTML string.
    html_node = markdown_to_html_node(md)
    if not html_node:
        raise Exception(f"markdown_to_html_node failed for {from_path}")
    
    html_string = html_node.to_html()
    
    # Use the extract_title function to grab the title of the page.
    html_title = extract_title(md)

    # Replace the {{ Title }} and {{ Content }} placeholders in the template with the HTML and title you generated.
    title_placeholder = "{{ Title }}"
    content_placeholer = "{{ Content }}"
    
    html_page = template.replace(title_placeholder, html_title)
    html_page = html_page.replace(content_placeholer, html_string)
    html_page = html_page.replace('href="/', f"href=\"{base_path}")
    html_page = html_page.replace('src="/', f"src=\"{base_path}")

    # Write the new full HTML page to a file at dest_path. Be sure to create any necessary directories if they don't exist.
    destdir = os.path.dirname(dest_path)
    create_dir_if_needed(destdir)
    
    with open(dest_path, "w") as f:
        f.write(html_page)    

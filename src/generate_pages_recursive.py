import os
from generate_page import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, base_path):
    print(f"--> generate_pages_recursive({dir_path_content}, {template_path}, {dest_dir_path}, {base_path})")
    
    if not os.path.exists(dir_path_content):
        raise Exception("source dir missing in generate_pages_recursive")

    files = os.listdir(dir_path_content)
    print(f"----> {files}")

    # Crawl every entry in the content directory
    for f in files:
        print(f"------> Checking file {f}")
        fullpath = os.path.join(dir_path_content, f)
    
        # For each markdown file found, generate a new .html file using the same template.html. The generated pages should be 
        # written to the public directory in the same directory structure.
        basefile = os.path.splitext(f)
        if  os.path.isfile(fullpath):
            if  len(basefile) > 1 and basefile[1] == ".md":
                target_file = os.path.join(dest_dir_path, "".join([basefile[0], ".html"]))
                print(f"------> generating page {fullpath}, {template_path}, {target_file}")
                generate_page(fullpath, template_path, target_file, base_path)
            else: 
                print(f"------> skipping {f}")
                    
        if os.path.isdir(fullpath):
            newsrc = os.path.join(dir_path_content, f)
            newdst = os.path.join(dest_dir_path, f)
            print(f"------> recursing {newsrc}, {template_path}, {newdst}")            
            generate_pages_recursive(newsrc, template_path, newdst, base_path)
    
    
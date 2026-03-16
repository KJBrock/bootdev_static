import sys
from copy_recurse import copy_recurse
from generate_pages_recursive import generate_pages_recursive

def main():
    args = sys.argv
    print(f"--> main(args = {args})")
    
    basedir = "/"
    if len(args) > 1:
        basedir = args[1]
        
    print("----> copying static files")
    copy_recurse("static", "docs")

    print("----> generating web pages")
    generate_pages_recursive("content", "template.html", "docs", basedir)

if __name__ == "__main__":
    main()

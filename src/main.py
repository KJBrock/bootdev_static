from copy_recurse import copy_recurse
from generate_pages_recursive import generate_pages_recursive

def main():
    print("--> main()")
    
    print("----> copying static files")
    copy_recurse("static", "public")

    print("----> generating web pages")
    generate_pages_recursive("content", "template.html", "public")

if __name__ == "__main__":
    main()

import os
import shutil

def create_dir_if_needed(dir):
    if os.path.exists(dir):
        if os.path.isfile(dir):
            raise Exception("destination dir is a regular file!")
        return
    
    parent = os.path.dirname(dir)
    if len(parent):
        create_dir_if_needed(parent)
        os.mkdir(dir)
        
def remove_dst(dst):
    print(f"--> remove_dst({dst})")
    if os.path.exists(dst):
        shutil.rmtree(dst)
    else:
        print(f"directory '{dst}' already gone")
        
def copy_files(src, dst):
    print(f"--> copy_files({src}, {dst})")

    if not os.path.exists(dst):
        print(f"----> creating directory {dst}")
        os.mkdir(dst)

    files = os.listdir(src)
    print(f"----> {files}")

    for f in files:
        fullpath = os.path.join(src, f)
        if os.path.isfile(fullpath):            
            print(f"will copy {f} from {fullpath} -> {dst}") 
            shutil.copy(fullpath, dst)   
            
        elif os.path.isdir(fullpath):
            newdst = os.path.join(dst, f)
            if os.path.exists(newdst):
                raise Exception("destination should have been cleared!")
            
            print(f"recursing to {f}")
            copy_files(os.path.join(src, f), newdst)
                        
        else:
            raise Exception(f"unknown file type for {fullpath}")

def copy_recurse(src, dst):
    print(f"--> copy_recurse({src}, {dst})")
    print("----> check src dir")
    # os.path.exists
    if not os.path.exists(src):
        raise Exception(f"source directort '{src}' does not exist")

    print("----> calling remove_dst")
    remove_dst(dst)
        
    print("----> calling copy_files")
    copy_files(src, dst)

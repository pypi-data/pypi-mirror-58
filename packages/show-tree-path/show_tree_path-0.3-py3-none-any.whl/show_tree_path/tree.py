from pathlib import Path
import os
# prefix components:
space =  '    '
branch = '│   '
# pointers:
tee =    '├── '
last =   '└── '


def show_tree(dir_path: Path, prefix: str=''):
    contents = list(dir_path.iterdir())
    pointers = [tee] * (len(contents) - 1) + [last]
    for pointer, path in zip(pointers, contents):
        try:
            yield prefix + pointer + path.name + "(" +str(len(os.listdir(path))) + ")"
        except:
            yield prefix + pointer + path.name
        if path.is_dir():
            extension = branch if pointer == tee else space 
            yield from show_tree(path, prefix=prefix+extension)
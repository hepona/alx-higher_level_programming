#!/usr/bin/python3
"""script that adds all arguments to a list"""
if __name__ == "__main__":
    """script that adds all arguments to a Python list"""
    from sys import argv
    from load_from_json_file import load_from_json_file
    from save_to_json_file import save_to_json_file
    
    filename = "add_item.json"
    for i in range(1, len(argv)):
        save_to_json_file(str(argv[i]), filename)
    print(load_from_json(filename))

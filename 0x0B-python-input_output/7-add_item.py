#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

    filename = "add_item.json"
    for i in range(1, len(argv)):
        save_to_json_file(str(argv[i]), filename)
    print(load_from_json_file(filename))

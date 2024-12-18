import json
import os

json_file_loc = os.path.expanduser(os.environ["KMVAR_local_BookmarksFile"])

def print_bookmarks():
    with open(json_file_loc, "r") as j:
        json_file = json.load(j)
        bookmarks_info = json_file["roots"]["bookmark_bar"]["children"]
        
        def find_bookmarks(dict): # recursively find bookmarks in json file
            for item in dict:
                if "children" in item:
                    find_bookmarks(item["children"])
                else:
                    if len(item["name"]) > 0:
                        print(item["name"],': ',end = '')
                    print(item["url"])
        find_bookmarks(bookmarks_info)

print_bookmarks()

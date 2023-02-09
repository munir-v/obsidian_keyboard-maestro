import json
import os

json_file_loc = os.path.expanduser('~/Library/Application Support/BraveSoftware/Brave-Browser/Default/Bookmarks')

# with open(json_file_loc, 'r') as fp:
#     data = json.load(fp)
# del data['names'][1]

# with open(filepath, 'w') as fp:
#     json.dump(data, fp)

def delete_bookmark(url):
    with open(json_file_loc, "r") as j:
        json_file = json.load(j)
        bookmarks_info = json_file["roots"]["bookmark_bar"]["children"]

        def find_bookmarks(dict): # recursively find bookmarks in json file
            for item in dict:
                if "children" in item:
                    find_bookmarks(item["children"])
                else:
                    if item["url"] == url:
                        print("found it")
                        print(item["url"])
                        print(item)
                        del item
        find_bookmarks(bookmarks_info)
    
    with open(json_file_loc, 'w') as j:
        json.dump(json_file, j)

url = "https://stackoverflow.com/questions/71764921/how-to-delete-an-element-in-a-json-file-python"

delete_bookmark(url)

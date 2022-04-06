import os

# path = "./data"

# path_list = os.walk(path)
path_list = os.walk("./data/")
# print(path_list)
print(list(path_list))
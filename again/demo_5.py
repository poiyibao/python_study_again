"""
with open('D:\\study\\again\\test.txt') as file_object:
    contents = file_object.read()
print(contents)
"""
txt_list =[ ]
filename = "D:\\study\\again\\test.txt"
with open(filename) as file_object:
    for line in file_object:
       txt_list = txt_list.append(line)
print(txt_list)


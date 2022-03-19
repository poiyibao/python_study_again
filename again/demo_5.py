"""
with open('D:\\study\\again\\test.txt') as file_object:
    contents = file_object.read()
print(contents)
"""
txt_list =[]
filename = "D:\\study\\again\\test.txt"
with open(filename, 'w') as file_object:
    file_object.write("test10")
# 如果要写入的文件不存在，函数open()将自动创建它
# 以写入模式（'w'）打开文件时如果指定的文件已经存在，会在写入前清空内容
# 保留文件原本的内容使用附加模式（'a'）
# Python只能将字符串写入文本文件。数值数据存储到文本文件中，必须先使用函数str()将其转换为字符串格式。



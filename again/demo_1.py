"""
# sort() & sorted()
list_1 = [ "bmw" ,"audi" ,"toyota", "subaru"]
list_2 = list_1.sorted()
#list_3 = list_1.sorted()
print(list_2)
#切片的复制可以做到独立完整的复制，而赋值知识改变指针


list_demo_1 = ["bmw" ,"audi" ,"toyota", "subaru"]
list_demo_2 = list_demo_1
list_demo_3 = list_demo_1[:]
#list_demo_2只是改变了指针指向list_demo_1，并非复制新列表，
# 当list_demo_1变化，list_demo_2跟着变化，而list_demo_3不会
list_demo_1.append("BYD")
print(list_demo_1,list_demo_2,list_demo_3)
"""

 
 # 字典
from queue import PriorityQueue
from xml.etree.ElementInclude import DEFAULT_MAX_INCLUSION_DEPTH


alien_1 = {
    "jen" : "python",
    'sarch' : 'c',
    'edward' : 'ruby',
    'phol' : 'pyhon',
 }
print(f"test is {alien_1['jen']}")

class Dog:
    # moni
    def __init__(self, name, age ):
        self.name = name
        self.age = age
    def sit(self):
        print(f"{self.name} de yi ge fucntion ")
    def roll_over(self):
        print(f"{self.name} rolled over !")


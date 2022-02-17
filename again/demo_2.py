# f字符串
first_name = "poi"
last_name = "yibao"
name = f'{first_name.title()}{last_name.title()}'
print(name)
# rstrip()
string_1 = " empty "
string_1 = string_1.rstrip()
print(string_1)

#insert(num,index)在任意位置添加新元素；append(index)在列表尾添加

dic ={
  'color': 'blue',
  'num': 13,
  'max': 'maxkey',
  'min': 'minkey'
	}
for k, v in dic.items():
    print(f"{k}={v}")
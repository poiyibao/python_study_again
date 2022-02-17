import requests
head = {
    'user-Agnet' : 'Mozilla/5.0 (Linux; Android 10; MI 9 Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 XWEB/1171 MMWEBSDK/200201 Mobile Safari/537.36 MMWEBID/2568 MicroMessenger/7.0.12.1620(0x27000C37) Process/tools NetType/4G Language/zh_CN ABI/arm64'
}
params = {
   'workerId':'076572'
}
req = requests.get(url=http://58.56.100.190:18666/building/a/api/checkReport/data,params=params, headers=head)
print(req)


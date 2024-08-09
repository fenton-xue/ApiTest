import requests

# 建一个会话
req = requests.Session()

url = "http://sellshop.5istudy.online/sell/user/login"

data = {
    "username": "test01",
    "password": "123456"
}
# 登录，req里保存了cookie或session
res = req.post(url=url, data=data)

# print(res.text)

url2 = "http://sellshop.5istudy.online/sell/seller/order/list"

res2 = req.get(url=url2)
print(res2.text)


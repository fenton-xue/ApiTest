import requests

def test_mobile():
    r = requests.get("https://api.github.com/events")
    # 接口状态返回码
    print(r.status_code)

    # 接口返回的json数据
    print(r.json())

    # 接口返回的文本
    print(r.text)

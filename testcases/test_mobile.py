import requests


def test_mobile():
    print("\n测试手机号归属地get请求")
    params = {
        "shouji": "15618919442",
        "appkey": "0c818521d38759e1"
    }

    r = requests.get(url="http://sellshop.5istudy.online/sell/shouji/query", params=params)
    assert r.status_code == 200
    result = r.json()
    assert result['status'] == 0
    assert result['msg'] == 'ok'
    assert result['result']['shouji'] == "15618919442"
    assert result['result']['province'] == "上海"
    assert result['result']['city'] == "上海"
    assert result['result']['company'] == "中国联通"
    assert result['result']['areacode'] == "0571"


def test_mobile_post():
    print("\n测试手机号归属地post请求")
    params = {
        "shouji": "15618919442",
        "appkey": "0c818521d38759e1"
    }

    r = requests.post(url="http://sellshop.5istudy.online/sell/shouji/query", params=params)

    assert r.status_code == 200
    result = r.json()
    assert result['status'] == 0
    assert result['msg'] == 'ok'
    assert result['result']['shouji'] == "15618919442"
    assert result['result']['province'] == "上海"
    assert result['result']['city'] == "上海"
    assert result['result']['company'] == "中国联通"
    assert result['result']['areacode'] == "0571"


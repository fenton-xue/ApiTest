import pytest
import requests


class TestMobile:

    def setup_class(self):
        print("测试开始")

    def teardown_class(self):
        print("测试结束")

    def test_mobile(self):
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

    def test_mobile_post(self):
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


if __name__ == '__main__':
    pytest.main()

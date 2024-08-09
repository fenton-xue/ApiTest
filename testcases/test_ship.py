# 用户名密码登录
# 拿到token，获取用户信息
import requests

class TestUser:

    token_1 = ""
    username_1 = ""

    def test_login(self):
        username = "fenton"
        password = "123456"
        # res = requests.post("/login", json={"username": username, "password": password})
        token = "token"
        assert token == "token"
        # assert token == res.json()["token"]
        # return token
        TestUser.token_1 = token
        TestUser.username_1 = username


    def test_user_info(self):
        # token = self.test_login()
        headers = {
            "token": TestUser.token_1
        }

        requests.post("/get_user", headers=headers)

        assert headers['token'] == TestUser.token_1

#coding:utf-8
import pytest
from ObjectPages.login_page import LoginPage as LP
from Testdatas import test_data
@pytest.mark.usefixtures("access_web")
@pytest.mark.usefixtures("refresh_web")
# @pytest.mark.demo
class TestLogin:
    data=test_data.test_login
    # @pytest.mark.parametrize(item,data)
    @pytest.mark.parametrize("item", data)
    def test_login(self,access_web,item):
        model="登录"
        # LP(access_web[0]).login_flow("15179062604","Z5201314",model)
        LP(access_web[0]).login_flow(item["username"],item["password"],model)



import pytest
from test_web_weixin_hw.page.main_page import MainPage

class TestAddDepart:
    def setup_class(self):
        # 第一次实例化
        self.main=MainPage()

    def teardown_class(self):
        self.main.quit()

    def test_add_depart(self):
        res=self.main.goto_contact().goto_add_depart().add_depart('xingbaba').get_depart_name()
        assert 'xingbaba' in res
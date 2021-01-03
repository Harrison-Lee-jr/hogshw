import pytest
from test_web_weixin_hw.page.main_page import MainPage

#建议driver和case分离
class TestAddMember:
    def setup_class(self):
        # 第一次实例化
        self.main=MainPage()
    def test_add_member(self):
        '''添加成员测试用例'''
        # 1、跳转添加成员页面 2、添加成员 3、自动跳转通讯录页面
        res=self.main.goto_add_member().add_member().get_member()
        assert 'rong' in res

    # 第一次参数化，传入重复的acctid，正确的手机号，断言信息
    # 第二次参数化，传入正确的acctid，重复的手机号，断言信息
    @pytest.mark.parametrize("acctid,phone,expect_res",
                             [('137','13119191615','该帐号已被“rong”占有'),('138','13119191614','该手机号已被“rong”占有')])
    def test_add_member_fail(self,acctid,phone,expect_res):
        res=self.main.goto_add_member().add_member_fail(acctid,phone)
        assert expect_res in res

    def test_add_member_by_contact(self):
        '''通过通讯录页面添加成员'''
        res=self.main.goto_contact().goto_add_member_bycontact().add_member().get_member()
        assert 'rong' in res

    # 回复到首页还原一开始的状态
    def teardown(self):
        self.main.back_main()

    def teardown_class(self):
        self.main.quit()

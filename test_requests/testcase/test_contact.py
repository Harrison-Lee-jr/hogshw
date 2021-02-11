from time import sleep
import pytest
from test_requests.reg_page.contact import Contact

class TestContact:
    def setup_class(self):
        self.contact=Contact()
        self.userid='zhangsan00123'
        self.name='zhangsan'

    @pytest.mark.parametrize("corpid,corpsecret,result",
                             [(None,None,0),('',None,41002),(None,'',41004)])
    def test_token(self,corpid,corpsecret,result):
        r=self.contact.get_token(corpid,corpsecret)
        assert r.get('errcode')==result

    def test_create(self):
        self.contact.create_member(userid=self.userid,name=self.name,mobile='13812400000',department=[1],alias='jackz')
        try:
            find_result=self.contact.find_member(self.userid)
        finally:
            self.contact.delete_member(self.userid)
        assert find_result["name"] == self.name

    def test_update(self):
        self.contact.create_member(userid=self.userid, name=self.name, mobile='13812400000', department=[1],
                                   alias='jackz')
        change_mobile='13812400001'
        self.contact.update_member(self.userid,self.name,change_mobile)
        try:
            find_result=self.contact.find_member(self.userid)
        finally:
            self.contact.delete_member(self.userid)
        assert find_result['mobile']==change_mobile

    def test_delete(self):
        self.contact.create_member(userid=self.userid,name=self.name,mobile='13812400000',department=[1],alias='jackz')
        sleep(2)
        r=self.contact.delete_member(self.userid)
        # print(r)
        assert r['errmsg']=='deleted'

    @pytest.mark.parametrize("userid,expected",
                             [("LiJinRong","LiJinRong"),("137","137"),("LiJinRong","LiJinRong"),("137","137")])
    def test_find(self,userid,expected):
        # self.contact.create_member()
        r=self.contact.find_member(userid)
        # print(r)
        assert r['userid']==expected
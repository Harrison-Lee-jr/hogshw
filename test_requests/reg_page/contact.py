from typing import List
from test_requests.reg_page.base import Base

class Contact(Base):

    def create_member(self,userid:str,name:str,mobile:str,department:List[int],**kwargs):
        '''
            "userid": "zhangsan00123",
            "name": "张三",
            "alias": "jackzhang",
            "mobile": "+86 13812400000",
            "department": [1]
        '''
        create_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create'
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department":department
        }
        data.update(kwargs)
        r = self.s.post(url=create_member_url,json=data)
        return r.json()

    def delete_member(self,userid):
        params={"userid":userid}
        delete_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete'
        # proxies={"https":"127.0.0.1:8888"}
        # r = requests.get(delete_url,proxies=proxies,verify=False)
        r=self.s.get(delete_url,params=params)
        return r.json()

    def find_member(self,userid):
        # userid="LiJinRong"
        params={"userid":userid}
        get_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get'
        r = self.s.get(get_member_url,params=params)
        return r.json()

    def update_member(self,userid:str,name:str,mobile:str,**kwargs):
        '''
            "userid": "LiJinRong",
            "name": "李四",
        '''
        update_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update'
        data = {
            "userid": userid,
            "name": name,
            "mobile":mobile
        }
        data.update(kwargs)
        r = self.s.post(url=update_url, json=data)
        return r.json()
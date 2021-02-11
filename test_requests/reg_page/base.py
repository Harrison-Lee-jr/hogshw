import requests
from requests import Session

class Base:
    def __init__(self):
        self.s=Session()
        self.corpid='ww7d34ae62889fcb2f'
        self.corpsecret='PRYaTl52cqneCtGqzC4D27cYflIJihqyVpx0DSELD-Q'
        self.s.params["access_token"]=self.get_token().get("access_token")

    def get_token(self,corpid=None,corpsecret=None):
        if corpid is None:
            corpid=self.corpid
        if corpsecret is None:
            corpsecret=self.corpsecret
        params={"corpid":corpid,"corpsecret":corpsecret}
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        r = requests.get(url,params=params)
        return r.json()
import requests

url='https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww7d34ae62889f&corpsecret=PRYaTl52cqneCtGqzC4D27cYflIJihqyVpx0'
def get_token():
    r=requests.get(url)
    token=r.json()['access_token']
    return token
def test_defect_member():
    get_member_url=f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={get_token()}&userid=LiJinRong'
    r=requests.get(get_member_url)
    print(r.json())
    assert '荣' == r.json()['name']
def test_update_member():
    update_url=f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={get_token()}'
    data={
        "userid": "LiJinRong",
        "name": "李四",
    }
    r=requests.post(url=update_url,json=data)
    print(r.json())
def test_create_member():
    create_member_url=f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={get_token()}'
    data={
    "userid": "zhangsan00123",
    "name": "张三",
    "alias": "jackzhang",
    "mobile": "+86 13812400000",
    "department": [1]
    }
    r=requests.post(url=create_member_url,json=data)
    print(r.json())
def test_delete_member():
    delete_url=f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={get_token()}&userid=zhangsan00123'
    r=requests.get(delete_url)
    print(r.json())
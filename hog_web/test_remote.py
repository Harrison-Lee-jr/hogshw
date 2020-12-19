from selenium import webdriver
from time import sleep
import yaml
class TestWework:
    def test_demo(self):
        opt=webdriver.ChromeOptions()
        #设置debug地址
        opt.debugger_address='127.0.0.1:9222'
        driver=webdriver.Chrome(options=opt)
        driver.implicitly_wait(5)
        driver.get('https://work.weixin.qq.com/wework_admin/frame')
        driver.find_element_by_id('menu_contacts').click()
        print(driver.get_cookies())
#使用cookie登陆
def test_cookie():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx') #先打开扫码登陆的页面
    cookies=[{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688853829878070'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325111206839'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688853829878070'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'zv5GWTLMElosRxfVsHJ07xTT1AWbt-bRUwZXrwyEhk9f6UA0vbpGgNap45ayQ61V'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a8635123'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'Ksuhro7R2qmqC1j396HT-8cabYZ28CDMflCcPi1JCsIwgO1XYcZxToP5wofIGikX5qg6cAW2xtcT8rb-qrXSy6EDOcWvJ2VP0iSnMugWOV-Z_sEQoGbaSgd0aw1rMsh_v-6gekQBIx1baFhK7k4rtNh-BqupL6fr25HAmKyMUoeQ7bFSYaQiEr_IT_OUFIW_QnVZzrkk84lmh_-3UAAuoAub7g4IU33Q1hmNHZ1LjJVs1CgQ56dtcYZ2WXkt2RoXoj3O_JvjugOoOO1wF3i5Tg'}, {'domain': '.work.weixin.qq.com', 'expiry': 1639922838.326038, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 2147483648.007697, 'httpOnly': False, 'name': 'pt2gguin', 'path': '/', 'secure': False, 'value': 'o2498186879'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '9633533873'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 2147483648.540691, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'aeA0CWmQcj'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '1112897550428294'}, {'domain': 'work.weixin.qq.com', 'expiry': 1608418374.325595, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '8vcqhpu'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '8730015744'}, {'domain': '.qq.com', 'expiry': 2147483647.908339, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': '624be8090355ac565c82fa2021415e3a17eefeb7709290ead265a1e1e3d132d1'}, {'domain': '.qq.com', 'expiry': 1837217653.045073, 'httpOnly': False, 'name': 'pac_uid', 'path': '/', 'secure': False, 'value': '0_5ab5b47600047'}, {'domain': '.work.weixin.qq.com', 'expiry': 1610979875.190302, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'cht'}]
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get('https://work.weixin.qq.com/wework_admin/frame')
    driver.find_element_by_id('menu_contacts').click()
    sleep(4)
    driver.quit()

def test_get_cookie():
    opt = webdriver.ChromeOptions()
    opt.debugger_address = '127.0.0.1:9222'
    driver = webdriver.Chrome(options=opt)
    driver.implicitly_wait(5)
    driver.get('https://work.weixin.qq.com/wework_admin/frame#contacts') #进入通讯录的页面
    cookie=driver.get_cookies()
    with open('data_cookie.yaml','w',encoding='UTF-8') as f:
        yaml.dump(cookie,f)

#使用序列化cookie方法进行登陆
def test_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')  # 先打开扫码登陆的页面
    with open('data_cookie.yaml',encoding='UTF-8') as f:
        yaml_data=yaml.safe_load(f)
        for cookie in yaml_data:
            driver.add_cookie(cookie)
    driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
    driver.find_element_by_id('menu_contacts').click()
    driver.find_element_by_link_text('添加成员').click()
    driver.find_element_by_id('username').send_keys('李一')
    driver.find_element_by_id('memberAdd_acctid').send_keys('123')
    driver.find_element_by_id('memberAdd_phone').send_keys('13119191614')
    driver.find_element_by_link_text('保存').click()
    contact_list=driver.find_element_by_xpath('//*[@title="13119191614"]').text
    assert '13119191614' in contact_list
    sleep(4)
    driver.quit()



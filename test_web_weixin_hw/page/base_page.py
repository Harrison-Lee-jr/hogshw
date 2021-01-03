from time import sleep
import yaml
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self,base_driver=None):
        # 注解，不是赋值操作。用作idle的类型提示
        base_driver:WebDriver
        # 因为main_page和add_member里类都继承了basepage初始化打开了页面
        # 这样实际运行会打开多个窗口，所以加入参数控制
        if base_driver is None:
            self.driver=webdriver.Chrome()
            self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx') # 先打开扫码登陆的页面
            self.__cookie_login()
        else:
            self.driver=base_driver
        self.driver.implicitly_wait(4)

    def __cookie_login(self):
        # 使用cookie登陆
        with open('/Users/jinronglee/PycharmProjects/hogs/test_web_weixin_hw/page/data_cookie.yaml', encoding='UTF-8') as f:
            yaml_data = yaml.safe_load(f)
            for cookie in yaml_data:
                self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')

    def find(self,by,value=None):
        # 把解元组操作也封装到这里,那么其它地方就可以去掉*了，不去掉也可以
        if value is None:
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by=by, value=value)
        # return self.driver.find_element(by=by,value=value)

    def finds(self,by,value=None):
        if value is None:
            return self.driver.find_elements(*by)
        else:
            return self.driver.find_elements(by=by, value=value)

    def wait_click(self,locator):
        WebDriverWait(self.driver,9).until(
            expected_conditions.element_to_be_clickable(locator))

    def quit(self):
        sleep(4)
        self.driver.quit()
import logging
import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from test_self_frame210109.black_handle import black_wrapper

class Black:
    def __init__(self):
        pass

class BasePage:
    FIND='find'
    ACTION='action'
    FIND_AND_CLICK='find_and_click'
    SEND='send'
    CONTENT='content'

    def __init__(self,driver:WebDriver=None):
        # :WebDriver是为了注解，在后续调用中能提示查找到
        self.driver=driver
        # 参考：黑名单类
        self.black_list=[(By.XPATH,"//*[@resource-id='com.xueqiu.android:id/iv_close']")]

    # 为解决base里方法越来越臃肿，可用以下方法扩展(装饰器模式和装饰器不相关，两个东西)
    # 设计模式：代理模式、装饰器模式
    # 装饰器
    @black_wrapper
    def find(self,by,locator):
        return self.driver.find_element(by,locator)


    def finds(self,by,locator):
        return self.driver.find_elements(by,locator)

    def find_and_click(self,by,locator):
        '''
        find 出现弹窗，去除弹窗，click
        如果不封装一起，分开find和click可能出现，find出现弹窗还没处理完弹窗就执行click而报错
        '''
        self.find(by,locator).click()

    def scroll_find(self,text):
        return self.driver.find_element(MobileBy.
                                 ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 f'text("{text}").instance(0));')
    def send(self,by,locator,content):
        return self.driver.find_element(by,locator).send_keys(content)

    def swip_find(self,by,locator):
        self.driver.implicitly_wait(1)
        # 找到所有元素
        eles=self.driver.find_elements(by,locator)
        # 不停滑动，直到找到为止
        while len(eles)==0:
            # 滑动
            self.driver.swipe(0,600,0,400)
            eles=self.driver.find_elements(by,locator)
        self.driver.implicitly_wait(5)
        return eles[0]

    def swip_find_click(self,by,locator):
        self.swip_find(by,locator).click()

    def scroll_find_click(self,text):
        self.scroll_find(text).click()

    def find_and_send(self,by,locator,text):
        self.find(by,locator).send_keys(text)

    def wait_for(self,by,locator):
        def wait_ele_for(driver:WebDriver):
            eles=driver.find_elements(by,locator)
            return len(eles)>0
        WebDriverWait(self.driver,10).until(wait_ele_for)

    def get_toast_text(self):
        result=self.find(MobileBy.XPATH,"//*[@class='android.widget.Toast']").text
        logging.info(result)
        return result

    def load(self,yaml_path):
        with open(yaml_path,encoding='utf-8') as f:
            data=yaml.load(f)
        # step: find,action
        for step in data:
            # todo:关键字可变问题——把常量定义成类变量
            xpath_expr=step.get(self.FIND)
            action=step.get(self.ACTION)
            if action==self.FIND_AND_CLICK:
                self.find_and_click(By.XPATH,xpath_expr)
            elif action==self.SEND:
                content=step.get(self.CONTENT)
                self.send(By.XPATH,xpath_expr,content)


    def screenshot(self,pic_path):
        self.driver.save_screenshot(pic_path)

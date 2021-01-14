import yaml
from selenium.webdriver.common.by import By
from test_self_frame210109.base_page import BasePage

class Search(BasePage):
    def search(self):
        # （1）常规方法：
        # self.find(By.XPATH,"//*[@resource-id='com.xueqiu.android:id/search_input_text']").send_keys('Nio')
        # （2）改用数据驱动：
        '''
        with open('../page/search.yaml',encoding='utf-8') as f:
            data=yaml.load(f)
        # step: find,action
        for step in data:
            xpath_expr=step.get('find')
            action=step.get('action')
            if action=='find_and_click':
                self.find_and_click(By.XPATH,xpath_expr)
            elif action=='send':
                content=step.get('content')
                self.send(By.XPATH,xpath_expr,content)
        '''
        # （3）读取yaml封装到basepage中
        self.load('../page/search.yaml')
        return True
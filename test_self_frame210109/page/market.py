from test_self_frame210109.base_page import BasePage
from test_self_frame210109.page.search import Search

#driver 数据
#basepage 对象
class Market(BasePage):

    def goto_search(self):
        #（1）常规方法：
        # self.find_and_click(By.XPATH,"//*[@resource-id='com.xueqiu.android:id/action_search']")
        #（2）改用数据驱动：
        '''
        with open('../page/market.yaml',encoding='utf-8') as f:
            data=yaml.load(f)
        # step: find,action
        for step in data:
            xpath_expr=step.get('find')
            action=step.get('action')
            if action=='find_and_click':
                self.find_and_click(By.XPATH,xpath_expr)
        '''
        #（3）读取yaml封装到basepage中
        self.load('../page/market.yaml')
        return Search(self.driver)
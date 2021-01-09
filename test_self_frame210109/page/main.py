from selenium.webdriver.common.by import By

from test_self_frame210109.base_page import BasePage
from test_self_frame210109.page.market import Market


class Main(BasePage):
    def goto_market(self):
        # 模拟弹窗的出现，点击发言logo
        self.find_and_click(By.XPATH,"//*[@resource-id='com.xueqiu.android:id/post_status']")
        self.find_and_click(By.XPATH,"//*[@resource-id='android:id/tabs']//*[@text='行情']")
        return Market(self.driver)
from time import sleep

from selenium.webdriver.common.by import By

from test_web_weixin_hw.page.base_page import BasePage



class AddDepart(BasePage):
    _location_depart_name=(By.CSS_SELECTOR,"[name=name]")
    _location_belong=(By.CSS_SELECTOR,'.js_parent_party_name')
    _location_choose=(By.XPATH,'//*[@class="inputDlg_item"]//*[@id="1688853807025034_anchor"]')
    _location_confirm=(By.CSS_SELECTOR,".ww_dialog_foot .ww_btn_Blue")
    def add_depart(self,name):
        from test_web_weixin_hw.page.contact_page import ContactPage
        self.find(self._location_depart_name).send_keys(name)
        self.find(self._location_belong).click()
        self.find(self._location_choose).click()
        self.find(self._location_confirm).click()
        return ContactPage(self.driver)
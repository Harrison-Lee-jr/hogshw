from appium import webdriver
from test_self_frame210109.base_page import BasePage
from test_self_frame210109.page.main import Main


class App(BasePage):
    def start(self):
        if self.driver is None:
            caps = {}
            caps["platformName"] = "android"
            # caps["deviceName"] = "wework"
            caps["appPackage"] = "com.xueqiu.android"
            caps["appActivity"] = ".view.WelcomeActivityAlias"
            caps["noReset"] = "true"
            caps["ensureWebviewsHavePages"] = True
            # 设置页面等待空闲状态的时间
            caps['settings[waitForIdleTimeout]'] = 0
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self.driver.launch_app()
        self.driver.implicitly_wait(10)
        return self

    def restart(self):
        # 重启app
        self.driver.close_app()
        self.driver.launch_app()
        pass

    def stop(self):
        # 停止app
        self.driver.quit()

    def goto_main(self):
        # 进入到首页
        return Main(self.driver)

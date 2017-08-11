# coding=utf-8
from src.testcase.case.LaunchApp import *


class GNAppAccountSettings3(LaunchApp):
    @case_run(False)
    def run(self):
        self.case_module = u"账户设置"  # 用例所属模块
        self.case_title = u'退出当前账号后，取消按钮功能检查'  # 用例名称
        self.zentao_id = 1973  # 禅道ID


    # 用例动作
    def case(self):
        try:
            self.widget_click(self.page["device_page"]["title"],
                              self.page["device_page"]["user_image"],
                              self.page["personal_settings_page"]["title"])

            self.widget_click(self.page["personal_settings_page"]["title"],
                              self.page["personal_settings_page"]["account_setting"],
                              self.page["account_setting_page"]["title"])

            self.widget_click(self.page["account_setting_page"]["title"],
                              self.page["account_setting_page"]["logout"],
                              self.page["logout_popup"]["title"])

            self.widget_click(self.page["logout_popup"]["title"],
                              self.page["logout_popup"]["cancel"],
                              self.page["account_setting_page"]["title"])

            self.widget_click(self.page["account_setting_page"]["title"],
                              self.page["account_setting_page"]["logout"],
                              self.page["logout_popup"]["title"])

            x = self.driver.get_window_size()['width']
            y = self.driver.get_window_size()['height']
            x = int(x * 0.1)
            y = int(y * 0.1)
            self.driver.tap([(x, y)])
            self.widget_click(self.page["account_setting_page"]["title"],
                              self.page["account_setting_page"]["title"],
                              self.page["account_setting_page"]["title"])
            try:
                self.wait_widget(self.page["logout_popup"]["title"])
                self.logger.info(u"[CHECK_PAGE]登出弹窗未消失")
                raise ValueError()
            except TimeoutException:
                pass
            except ValueError:
                raise TimeoutException()

            self.case_over(True)
        except TimeoutException:
            self.case_over(False)


# coding=utf-8
from src.testcase.GN_APP.WidgetOperation import *


class GNAPPLogin3(WidgetOperation):
    @case_run(True)
    def run(self):
        self.case_module = u"登录"  # 用例所属模块
        self.case_title = u'登录页面—登录功能检查'  # 用例名称
        self.zentao_id = "1891"  # 禅道ID

    # 用例动作
    def case(self):
        user_name = self.widget_click(self.page["login_page"]["username"],
                                      self.page["login_page"]["title"])

        # 发送数据
        data = self.user["user_name"]
        data = bytearray.fromhex(str(data)).decode('utf-8').replace(" ", "")
        user_name.clear()
        self.ac.send_keys(user_name, data, self.driver)
        self.debug.info(u'[APP_INPUT] ["用户名"] input success')
        time.sleep(0.5)

        self.show_pwd(self.wait_widget(self.page["login_page"]["check_box"]))
        login_pwd = self.widget_click(self.page["login_page"]["password"],
                                      self.page["login_page"]["title"])

        data = self.user["login_pwd"]
        data = bytearray.fromhex(str(data)).decode('utf-8').replace(" ", "")
        login_pwd.clear()
        self.ac.send_keys(login_pwd, data, self.driver)
        self.debug.info(u'[APP_INPUT] ["密码"] input success')
        time.sleep(0.5)

        self.widget_click(self.page["login_page"]["login_button"],
                          self.page["device_page"]["title"])

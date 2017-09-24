# coding=utf-8
from src.testcase.case.LaunchApp_JD import *


class JDAppAppFunction1(LaunchAppJD):
    @case_run_jd(False)
    def run(self):
        self.case_module = u"APP功能测试"  # 用例所属模块
        self.case_title = u'定时记录删除是否成功"'  # 用例名称
        self.zentao_id = 1170  # 禅道ID

    # 用例动作
    def case(self):
        try:
            while True:
                elements = self.wait_widget(self.page["app_home_page"]["device"])
                new_value = copy.copy(self.page["app_home_page"]["device"])
                for index, element in elements.items():
                    if self.ac.get_attribute(element, "name") == conf["MAC"][0]:
                        new_value[0] = new_value[0][index]

                        self.widget_click(new_value, self.page["control_device_page"]["title"])
                        raise ValueError()
                    else:
                        self.ac.swipe(0.6, 0.9, 0.6, 0.6, 0, self.driver)
                        time.sleep(1)
        except ValueError:
            pass

        try:
            self.wait_widget(self.page["control_device_page"]["power_on"])
            power_state = "power_on"
        except TimeoutException:
            self.wait_widget(self.page["control_device_page"]["power_off"])
            power_state = "power_off"

        self.widget_click(self.page["control_device_page"]["normal_timer"],
                          self.page["normal_timer_page"]["title"])

        self.widget_click(self.page["normal_timer_page"]["timer_log"],
                          self.page["timer_log_page"]["title"])

        self.widget_click(self.page["timer_log_page"]["clear"],
                          self.page["timer_log_clear_popup"]["title"])

        self.widget_click(self.page["timer_log_clear_popup"]["confirm"],
                          self.page["timer_log_page"]["no_log"])

        self.widget_click(self.page["timer_log_page"]["to_return"],
                          self.page["normal_timer_page"]["title"])

        self.widget_click(self.page["normal_timer_page"]["add_timer"],
                          self.page["add_normal_timer_page"]["title"])

        delay_time = 1
        start_time, set_time = self.set_timer_roll(self.page["add_normal_timer_page"]["timer_h"],
                                                   self.page["add_normal_timer_page"]["timer_m"],
                                                   self.page["add_normal_timer_page"]["set_timer"], delay_time)

        if power_state == "power_on":
            self.widget_click(self.page["add_normal_timer_page"]["power_off"],
                              self.page["add_normal_timer_page"]["title"])
        elif power_state == "power_off":
            self.widget_click(self.page["add_normal_timer_page"]["power_on"],
                              self.page["add_normal_timer_page"]["title"])

        end_time = time.time() + (delay_time + 1) * 60
        while True:
            if time.strftime("%H:%M") == start_time:
                self.widget_click(self.page["add_normal_timer_page"]["saved"],
                                  self.page["normal_timer_page"]["title"])
            else:
                if time.time() < end_time:
                    time.sleep(1)
                else:
                    break

        self.widget_click(self.page["normal_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        end_time = time.time() + (delay_time + 1) * 60
        if power_state == "power_on":
            power_state = u"设备已关闭"
        elif power_state == "power_off":
            power_state = u"设备已开启"
        while True:
            element = self.wait_widget(self.page["control_device_page"]["power_state"])
            if self.ac.get_attribute(element, "name") == power_state:
                self.logger.info(u"[APP_INFO]%s" % power_state)
                break
            else:
                if time.time() < end_time:
                    time.sleep(1)
                else:
                    raise TimeoutException()

        self.widget_click(self.page["control_device_page"]["normal_timer"],
                          self.page["normal_timer_page"]["title"])
        time.sleep(3)
        self.widget_click(self.page["normal_timer_page"]["timer_log"],
                          self.page["timer_log_page"]["title"])

        month, day = time.strftime("%m-%d").split("-")
        set_time = u"%s%s月%s日" % (set_time, month, day)
        element = self.wait_widget(self.page["timer_log_page"]["has_log"])
        if self.ac.get_attribute(element, "name") == set_time:
            self.logger.info(u"[APP_INFO]存在定时记录%s" % set_time)
        else:
            raise TimeoutException()

        self.widget_click(self.page["timer_log_page"]["clear"],
                          self.page["timer_log_clear_popup"]["title"])

        self.widget_click(self.page["timer_log_clear_popup"]["confirm"],
                          self.page["timer_log_clear_popup"]["no_log"])

        self.case_over(True)

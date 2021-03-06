# coding=utf-8
from src.testcase.GN_F1331.WidgetOperation import *


class GNF1331Timer8(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"定时器(#9)"  # 用例所属模块
        self.case_title = u'设备当前状态和延时定时输出状态相同，延时定时执行状态检查'  # 用例名称
        self.zentao_id = "121"  # 禅道ID

    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"][self.app][self.device_mac])

        self.delete_out_date_timer()
        self.delete_normal_timer_all()

        self.set_power("main_button_off")

        self.input_serial_command("power", "set_delay_timer", "launch_delay_timer")

        self.widget_click(self.page["control_device_page"]["up_timer"],
                          self.page["up_timer_page"]["title"])

        now = time.strftime("%H:%M")

        time_1 = ["delay", "00:05"]
        start_time_1, set_time_1 = self.create_delay_timer("up_timer_page", now, time_1)

        self.widget_click(self.page["up_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        time.sleep(120)

        self.widget_click(self.page["control_device_page"]["up_button"],
                          self.page["control_device_page"]["up_button_off"])

        control_time_1 = time.time()

        while True:
            if time.time() > set_time_1 + 10:
                break
            print(time.time())
            time.sleep(1)

        #####
        #  开关
        btn_dict = self.check_button_state(start_time_1, control_time_1, set_time_1)
        # 定时设置
        set_delay_dict = self.check_set_delay_timer(start_time_1)
        # 定时执行
        launch_delay_dict = self.check_launch_delay_timer(set_delay_dict, set_time_1)

        # 设置
        set_timer = set_delay_dict[start_time_1]
        s_time, s_id = set_timer[0], set_timer[1]
        result = [s_time is not None]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (s_time, result))
        # 执行
        launch_timer = launch_delay_dict[set_time_1]
        l_time, l_id = launch_timer[s_id][0], launch_timer[s_id][1]
        result = [l_time is not None,
                  l_id == s_id]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (launch_timer, result))

        # 开关
        # 上层关→开
        btn = btn_dict[start_time_1]
        btn_up = btn[1][0]
        result = [btn_up == "1"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))
        # 上层手动开→关
        btn = btn_dict[control_time_1]
        btn_up = btn[1][0]
        result = [btn_up == "0"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))
        # 上层关→关
        btn = btn_dict[set_time_1]
        btn_up = btn[1][0]
        result = [btn_up == "0"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

from selenium.common.exceptions import TimeoutException
from AppDetailPage import AppDetailPage
from base_element import event_log
from login_test import login_test
from time import sleep
import random
import yaml

class PodDetailPage(AppDetailPage):
    def DeletePod(self):
        self.click_element('poddetail_more_loc')
        self.click_element('poddetail_more_delete_loc')
        self.click_element('poddetail_more_delete_ensure_loc')
        self.screenshot('poddetail delete pod')

    def poddetail_action_result(self, testcase):
        pass



from selenium.common.exceptions import TimeoutException
from base_element import BasePage
from base_element import event_log
from login_test import login_test
from time import sleep
import yaml


class ModelShop(BasePage):
    def InstallModel(self, imgaddr):
        self.click_element('modelshop_manualinstall_loc')
        self.click_element('modelshop_manualinstall_fromweb_loc')
        self.type('modelshop_manualinstall_fromweb_addr_loc', imgaddr)
        self.click_element('modelshop_manualinstall_fromweb_next_loc')
        sleep(2)
        self.click_element('modelshop_manualinstall_fromweb_check_loc')
        self.click_element('modelshop_manualinstall_fromweb_ensure_loc')

    def modelshop_action_result(self, testcase):
        pass


model = ModelShop()


def installmodel(imgaddr):
    event_log('case','modelshop install model manually')
    model.click_element('modelshop_installed_loc')
    model.InstallModel(imgaddr)
    # model.action_result()


if __name__ == '__main__':
    login_test('admin', 'changeme')
    integratedmodel = ModelShop()
    integratedmodel.click_element('sidebar_model_loc')
    installmodel('daocloud.io/daocloud/dce-2048-plugin')

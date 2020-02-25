from selenium.common.exceptions import TimeoutException
from base_element import event_log
from login_test import login_test
from AppDetailPage import AppDetailPage
from time import sleep
import random
import yaml


class DeploymentDetailPage(AppDetailPage):
    def ManageDeployment(self, mov):  # 启动/停止/重启服务
        key = 'deploymentdetail_more_status_' + mov + '_loc'
        self.click_element(key)
        self.click_element('appdetail_assure_loc')
        # self.action_result('appdetail_' + mov + ' deployment', 'sign')
        return self.screenshot('appdetail_' + mov + 'deployment')

    def ManageLabel(self):
        pass

    def deployment_detail_action_result(self, testcase, appname, expectdata='none'):
        pass


if __name__ == '__main__':
    login_test('admin', 'changeme')
    deploymentdetail = DeploymentDetailPage()
    event_log('case', 'deployment detail manage')
    deploymentdetail.click_element('sidebar_workloadlist_loc')
    deploymentdetail.click_element('sidebar_workload_deploymentlist_loc')
    deploymentdetail.click_element('deploymentlist_firstdeploy_loc')
    deploymentdetail.get_url()
    deploymentdetail.OpenTty()
    sleep(1)
    deploymentdetail.ChangeRc(3)

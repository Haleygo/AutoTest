from selenium.common.exceptions import TimeoutException
from base_element import BasePage
from base_element import event_log
from login_test import login_test
from time import sleep
import random
import yaml


class AppDetailPage(BasePage):
    @property
    def Double_Assure(self):  # 双重确认操作
        self.click_element('appdetail_assure_loc')
        self.click_element('appdetail_save_loc')

    def OpenTty(self):
        # self.click_element('appdetail_opentty_loc')
        self.click_element('appdetail_opentty_ensure_loc')
        sleep(4)
        window = self.get_handle()
        if len(window) == 2:
            event_log('success', 'open tty')
            self.switch_win(window[1])
            self.screenshot('appdetail_opentty')
            self.close()
            self.switch_win(window[0])
        else:
            event_log('fail', 'open tty')
            self.screenshot('appdetail_opentty')
        return self.click_element('appdetail_opentty_cancel_loc')

    def ChangeRc(self, num):  # 改变服务rc值
        self.clearcontent('appdetail_changerc_targetnum_loc')
        self.type('appdetail_changerc_targetnum_loc', num)
        self.Double_Assure
        # self.action_result('appdetail_change rc', 'sign')
        return self.screenshot('appdetail_managedeploy')

    def ChangeImg(self, imgaddr):  # 更改镜像
        sleep(1)
        self.click_element('appdetail_changeimg_addrclear_loc')
        sleep(1)
        self.click_element('appdetail_changeimg_addrinput_loc')
        self.type('appdetail_changeimg_addrinput_loc', imgaddr)
        self.click_element('appdetail_changeimg_addrverify_loc')
        sleep(2)
        self.Double_Assure
        # self.action_result('appdetail_change image', 'sign')
        return self.screenshot('appdetail_managedeploy')

    def ManageDeployment(self, mov):  # 启动/停止/重启服务
        key = 'appdetail_deployment' + mov + '_loc'
        self.click_element(key)
        self.click_element('appdetail_assure_loc')
        # self.action_result('appdetail_' + mov + ' deployment', 'sign')
        return self.screenshot('appdetail_' + mov + 'deployment')

    def ManageLabel(self, mov):  # 编辑标签
        # self.click_element('appdetail_managelabel_loc')
        # sleep(1)
        if mov == 'add':
            print('666')
            self.click_element('appdetail_managelabel_add_deploylabel_loc')
            self.type('appdetail_managelabel_input_deploylabel_key_loc', 'deploytest' + str(random.randint(1, 1000)))
            self.type('appdetail_managelabel_input_deploylabel_value_loc', 'true')
            self.click_element('appdetail_managelabel_podlabel_loc')
            self.click_element('appdetail_managelabel_add_podlabel_loc')
            self.type('appdetail_managelabel_input_podlabel_key_loc', 'podtest' + str(random.randint(1, 1000)))
            self.type('appdetail_managelabel_input_podlabel_value_loc', 'true')
            self.Double_Assure
        if mov == 'edit':
            event_log('case', 'edit label')
        # self.action_result('appdetail managelabel', 'sign')
        return self.screenshot('appdetail_manage_label')

    def ChangeResource(self, cpulimit, cpurequest, memlimit):
        self.clearcontent('appdetail_toolbarconfig_resourceconfig_cpulimit_loc')
        self.type('appdetail_toolbarconfig_resourceconfig_cpulimit_loc', cpulimit)
        self.clearcontent('appdetail_toolbarconfig_resourceconfig_cpurequest_loc')
        self.type('appdetail_toolbarconfig_resourceconfig_cpurequest_loc', cpurequest)
        self.click_element('appdetail_toolbarconfig_resourceconfig_memconfig_loc')
        self.clearcontent('appdetail_toolbarconfig_resourceconfig_memlimit_loc')
        self.type('appdetail_toolbarconfig_resourceconfig_memlimit_loc', memlimit)
        self.click_element('appdetail_assure_loc')
        self.click_element('appdetail_toolbarconfig_resourceconfig_save_loc')
        # self.action_result('appdetail change resource', 'sign')
        return self.screenshot('appdetail_change_resource')

    def ScheduleDeployment(self, schedulelabel):
        self.click_element('appdetail_toolbarconfig_scheduleconfig_policy_uselabel_loc')
        self.click_element('appdetail_toolbarconfig_scheduleconfig_policy_chooselabel_loc')
        self.type('appdetail_toolbarconfig_scheduleconfig_policy_labelsearch_loc', schedulelabel)
        sleep(1)
        # self.move_element('appdetail_toolbarconfig_scheduleconfig_policy_foundlabel_loc')
        self.click_element('appdetail_toolbarconfig_scheduleconfig_policy_foundlabel_loc')
        self.Double_Assure
        # self.action_result('appdetail schedule deployment', 'sign')
        return self.screenshot('appdetail_schedule_deployment')

    def AddDeployment(self, image_addr, deploymentname):
        self.click_element('appdetail_adddeployment_loc')
        self.click_element('applist_createappbyimage_customizeimage_loc')
        self.type('applist_createappbyimage_customizeimage_imagename_loc', image_addr)
        self.click_element('applist_createappbyimage_customizeimage_ensureaddr_loc')
        sleep(2)
        self.click_element('applist_createappbyimage_continue_loc')
        self.clearcontent('applist_createappbyimage_appname_loc')
        self.type('applist_createappbyimage_appname_loc', deploymentname)
        sleep(1)
        self.click_element('applist_createappbyimage_continue_loc')
        self.click_element('applist_createappbyimage_auditapp_loc')
        self.click_element('applist_createappbyimage_deployapp_loc')  # 以上为复用通过镜像部署应用的镜像选择操作
        self.click_element('appdetail_adddeployment_ensure_loc')
        return self.screenshot('appdetail_add_deployment')

    def AddService(self):
        pass

    def appdetail_action_result(self, testcase, appname, expectdata='none'):
        deployment_cfg_list = ['changerc', 'changeimg', 'managedeploylabel', 'managepodlabel', 'changeresource',
                               'scheduledeployment']
        deployment_cfg_dir = {'changerc': ['spec', 'replicas'],
                              'changeimg': ['spec', 'template', 'spec', 'containers', 'image'],
                              'managedeploylabel': ['metadata', 'labels'],
                              'managepodlabel': ['spec', 'template', 'metadata', 'labels'],
                              'changeresource': ['spec', 'template', 'spec', 'containers', 'resources'],
                              'scheduledeployment': ['spec', 'template', 'spec', 'affinity', 'nodeAffinity']
                              }
        if testcase == 'managedeployment':  # 启动/停止/重启服务用例结果判断
            sign = '//*[@class="noty_body"]'
            try:
                element = self.element_present(sign)
                while element:
                    return event_log('success', testcase)
            except TimeoutException:
                return event_log('fail', testcase)
        elif testcase == 'adddeployment':  # 在应用下添加服务用例结果判断
            cmd = 'kubectl describe app ' + appname + " | grep 'Deployment Name' | awk '{print $3}'"
            realdeploymentnames = self.get_hostcmd(cmd)
            if expectdata in realdeploymentnames:
                return event_log('success', testcase)
            else:
                return event_log('fail', testcase)
        elif testcase in deployment_cfg_list:  # 配置服务相关用例结果判断
            deployment_name = self.get_hostcmd(
                "kubectl get deployment | awk '{print $1}' | grep " + appname)  # 得到服务名称，没有考虑多服务应用
            cmd = 'kubectl get deployment ' + deployment_name + ' -o yaml'
            deployment_yaml = self.get_hostcmd(cmd)
            realdata = yaml.load(deployment_yaml, Loader=yaml.FullLoader)
            loc = deployment_cfg_dir(testcase)
            for i in loc:
                realdata = realdata[i]
            if realdata == expectdata:
                return event_log('success', testcase)
            else:
                return event_log('fail', testcase)


if __name__ == '__main__':
    login_test('admin', 'changeme')
    # app_create_byyaml()
    appdetail = AppDetailPage()
    event_log('case', 'manage app')
    appdetail.click_element('sidebar_applist_loc')
    appdetail.click_element('applist_firstapp_loc')
    appdetail.get_url()
    appdetail.AddDeployment('daocloud.io/daocloud/dao-2048:latest', 'autoadddeploy')
    sleep(1)

from base_element import event_log
from AppDetailPage import AppDetailPage
from login_test import login_test
import app_create
from time import sleep
import random

appdetail = AppDetailPage()


def opentty():
    event_log('case', 'appdetail open tty')
    appdetail.click_element('appdetail_opentty_loc')
    sleep(1)
    appdetail.OpenTty()


def changerc(num):
    event_log('case', 'appdetail change rc')
    appdetail.click_element('appdetail_changerc_loc')
    appdetail.ChangeRc(num)


def changeimg(imgaddr):
    event_log('case', 'appdetail change image')
    appdetail.click_element('appdetail_changeimg_loc')
    sleep(1)
    appdetail.ChangeImg(imgaddr)


def managedeployment(mov):
    event_log('case', 'appdetail ' + mov + ' deployment')
    appdetail.ManageDeployment(mov)


def managelabel(mov):
    event_log('case', 'appdetail ' + mov + ' label')
    appdetail.click_element('appdetail_managelabel_loc')
    sleep(1)
    appdetail.ManageLabel(mov)

def changeresource(cpulimit, cpurequest, memlimit):
    event_log('case', 'appdetail change deployment resource')
    appdetail.click_element('appdetail_toolbarconfig_loc')
    appdetail.move_element('appdetail_deploymentlist_gear_loc')
    appdetail.double_click('appdetail_toolbarconfig_resourceconfig_loc')
    appdetail.ChangeResource(cpulimit, cpurequest, memlimit)


def scheduledeployment(schedulelabel):
    event_log('case', 'appdetail change deployment schedule policy')
    appdetail.click_element('appdetail_toolbarconfig_loc')
    appdetail.move_element('appdetail_deploymentlist_gear_loc')
    appdetail.double_click('appdetail_toolbarconfig_scheduleconfig_loc')
    appdetail.ScheduleDeployment(schedulelabel)

def adddeployment(image_addr, deploymentname):
    event_log('case', 'appdetail add deployment')
    appdetail.AddDeployment(image_addr, deploymentname)


if __name__ == '__main__':
    login_test('admin', 'changeme')
    # app_create.app_create_byyaml('autobyyaml' + str(random.randint(1, 1000)))
    # app_create.app_create_byimage('autobyimage' + str(random.randint(1, 1000)))
    integratedapp = AppDetailPage()
    event_log('case', 'manage app')
    integratedapp.click_element('sidebar_applist_loc')
    integratedapp.click_element('applist_firstapp_loc')
    integratedapp.get_url()
    # opentty()
    # sleep(1)
    # changerc(2)
    # sleep(1)
    changeimg('daocloud.io/daocloud/dao-2048:v1.0.3')
    sleep(1)
    # managedeploylist = ['stop', 'restart']
    # for i in managedeploylist:
    #     managedeployment(i)
    #     sleep(3)
    # sleep(2)
    # managelabel('add')
    # sleep(1)
    # changeresource('0.2', '0.2', '0.5')
    # scheduledeployment('autotest')
    # adddeployment('daocloud.io/daocloud/dao-2048:latest', 'autoadddeploy' + str(random.randint(1, 100)))
    integratedapp.close()

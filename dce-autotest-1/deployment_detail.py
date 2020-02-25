from base_element import event_log
from DeploymentDetailPage import DeploymentDetailPage
from login_test import login_test
from time import sleep
import random

deployment_detail = DeploymentDetailPage()

def deployment_opentty():
    event_log('case','deployment_detail open tty')
    deployment_detail.click_element('deploymentdetail_opentty_loc')
    sleep(1)
    deployment_detail.OpenTty()

def deployment_changerc(num):
    event_log('case','deployment_detail change rc')
    deployment_detail.click_element('deploymentdetail_more_loc')
    deployment_detail.click_element('deploymentdetail_more_changerc_loc')
    deployment_detail.ChangeRc(num)

def deployment_changeimg(imgaddr):
    event_log('case','deployment_detail change image')
    deployment_detail.click_element('deploymentdetail_more_loc')
    deployment_detail.click_element('deploymentdetail_more_changeimg_loc')
    deployment_detail.ChangeImg(imgaddr)

def deployment_managedeployment(mov):
    event_log('case','deployment_detail manage deployment')
    deployment_detail.click_element('deploymentdetail_more_loc')
    deployment_detail.click_element('deploymentdetail_more_status_loc')

def deployment_managelabel(mov):
    pass


if __name__ == '__main__':
    login_test('admin','changeme')
    integrateddeployment = DeploymentDetailPage()
    event_log('case','manage deployment')
    integrateddeployment.click_element('sidebar_workloadlist_loc')
    integrateddeployment.click_element('sidebar_workload_deploymentlist_loc')
    integrateddeployment.click_element('deploymentlist_firstdeploy_loc')
    integrateddeployment.get_url()
    # deployment_opentty()
    # integrateddeployment.click_element('sidebar_workload_deploymentlist_loc')
    # deployment_changerc(3)
    deployment_changeimg('daocloud.io/daocloud/dao-2048:v1.0.3')

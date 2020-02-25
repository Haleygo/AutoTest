from base_element import logger
from base_element import event_log
from login_test import login_test
from AppCreatePage import AppCreatePage
import random
from time import sleep

def app_create_byyaml(app_name):  # 创建应用
    # myapp = 'autobyyaml' + str(random.randint(1, 1000))
    logger.debug('开始创建应用{}'.format(app_name))
    create_app_byyaml = AppCreatePage()
    event_log('case','create app by yaml')
    create_app_byyaml.click_element('sidebar_applist_loc')
    create_app_byyaml.Create_App_by_Yml(app_name)
    sleep(2)
    create_app_byyaml.action_result('create app')
    create_app_byyaml.screenshot('create_app_byyaml')

def app_create_byimage(app_name):
    # myapp = 'autobyimage' + str(random.randint(1, 1000))
    logger.debug('开始创建应用{}'.format(app_name))
    create_app_byimage = AppCreatePage()
    event_log('case','create app by image')
    create_app_byimage.click_element('sidebar_applist_loc')
    create_app_byimage.Create_App_throughImage('daocloud.io/daocloud/dao-2048:latest',app_name)
    sleep(2)
    create_app_byimage.action_result('create app')
    create_app_byimage.screenshot('create_app_byimage')

if __name__ == '__main__':
    login_test('admin','changeme')
    app_create_byyaml('autobyyaml' + str(random.randint(1, 1000)))
    sleep(1)
    app_create_byimage('autobyimage' + str(random.randint(1, 1000)))
    sleep(4)



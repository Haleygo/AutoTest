from base_element import event_log
from PodDetailPage import PodDetailPage
from login_test import login_test
from time import sleep
import random

pod_detail = PodDetailPage()

def pod_opentty():
    event_log('case','pod_detail open tty')
    pod_detail.click_element('poddetail_more_loc')
    pod_detail.click_element('poddetail_more_opentty_loc')
    pod_detail.OpenTty()

def pod_delete():
    event_log('case','pod_detail delete pod')
    pod_detail.click_element('poddetail_more_loc')
    pod_detail.click_element('poddetail_more_delete_loc')
    pod_detail.click_element('poddetail_more_delete_ensure_loc')

if __name__ == '__main__':
    login_test('admin', 'changeme')
    integratedpod = PodDetailPage()
    event_log('case', 'manage pod')
    integratedpod.click_element('sidebar_podlist_loc')
    integratedpod.click_element('podlist_firstpod_loc')
    integratedpod.get_url()
    pod_opentty()
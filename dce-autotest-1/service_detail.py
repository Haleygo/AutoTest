from base_element import event_log
from ServiceDetailPage import ServiceDetailPage
from login_test import login_test
import app_create
from time import sleep
import random

servicedetail = ServiceDetailPage()

def addservice(service_name):
    event_log('case','add service')
    servicedetail.click_element()
    servicedetail.AddService(service_name)


if __name__ == '__main__':
    login_test('admin','changeme')
    integratedservice = ServiceDetailPage()
    addservice()
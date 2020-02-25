#coding=utf-8
from selenium import webdriver
from base_element import BasePage
from selenium.webdriver.common.by import By
from time import sleep
from base_element import allelement

username_loc = (By.XPATH, '//*[@class="login-page"]/div[2]/div[1]/div[1]/div[1]//input')
password_loc = (By.XPATH, '//*[@class="login-page"]/div[2]/div[1]/div[1]/div[2]//input')
submit_loc = (By.XPATH, '//*[@id="login"]//button[1]')

applist_loc = (By.XPATH, '//*[@id="app"]//menu//section[2]/menu/span')  # 侧边栏"应用"


class LoginPage(BasePage):
    pass



    # def type(self,key,value):
    #     loc = allelement[key]
    #     print(loc)
    #     self.find_element(*loc).send_keys(value)
    #
    # def submit(self):
    #     self.find_element(*submit_loc).click()


if __name__ == '__main__':
    self_base_url, self_pagetitle = 'http://10.6.150.22','dce'
    self_driver = webdriver.Chrome()
    login_page = LoginPage(self_driver,self_base_url)
    login_page.test_login(self_driver,self_base_url)
    self_driver.find_element('xpath','//*[@id="app"]//menu//section[2]/menu/span').click()
    sleep(5)

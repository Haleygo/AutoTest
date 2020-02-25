# coding=utf-8
# import driver
import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

ServerAddr = 'http://10.6.150.22'
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('lang=zh_CN.UTF-8')
options.add_argument('--start-maximized')
# options.add_argument('--disable-javascript')
TestWebDriver = webdriver.Chrome(chrome_options=options)
# TestWebDriver.implicitly_wait(10)



allelement = {'username_loc':(By.XPATH, '//*[@class="login-page"]/div[2]/div[1]/div[1]/div[1]//input'),
              'password_loc':(By.XPATH, '//*[@class="login-page"]/div[2]/div[1]/div[1]/div[2]//input'),
              'submit_loc':(By.XPATH, '//*[@id="login"]//button[1]'),
              'applist_loc':(By.XPATH, '//*[@id="app"]//menu//section[2]/menu/span'),
              'applist_loc_firstapp':(By.XPATH, '//*[@class="dao-table-view unselectable"]//tr[1]/td[1]/a'),
              'createapp_loc':(By.XPATH, '//*[@class="dao-btn blue has-icon"]'),
              'advancefuc_loc':(By.XPATH, '//*[@class="dao-radio-group"]/p/a'),
              'create_by_yaml_loc':(By.XPATH, '//*[@class="dao-radio-group"]/div[4]//input'),
              'continue_create_loc':(By.XPATH, '//*[@class="dao-btn blue has-icon compact"]'),
              'app_name_loc':(By.XPATH, '//*[@class="dao-input-inner"]//input'),
              'try2048_loc':(By.XPATH, '//*[@class="dao-setting-section"]//a[1]'),
              'confirm_create_loc':(By.XPATH, '//*[@class="dao-steps"]/div[2]//button[1]'),
              'opentty_loc':(By.XPATH,'//*[@class="dao-table-view-toolbar"]//span[1]/button[1]'),
              'changerc_loc':(By.XPATH,'//*[@class="dao-table-view-toolbar"]//span[1]/button[2]'),
              'changeimg_loc':(By.XPATH,'//*[@class="dao-table-view-toolbar"]//span[1]/button[3]'),
              'startdeployment_loc':(By.XPATH,'//*[@class="dao-table-view-toolbar"]//span[2]/button[1]'),
              'stopdeployment_loc':(By.XPATH,'//*[@class="dao-table-view-toolbar"]//span[2]/button[2]'),
              'restartdeployment_loc':(By.XPATH,'//*[@class="dao-table-view-toolbar"]//span[2]/button[3]'),
              'setlabel_loc':(By.XPATH,'//*[@class="dao-table-view-toolbar"]//span[3]/button[1]'),
              'toolbarconfig_loc':(By.XPATH,'//*[@class="dao-table-view-toolbar"]//span[3]/div'),
              'assure_loc':(By.XPATH, '//*[@class="dao-dialog-footer"]//button[2]'),
              'save_loc':(By.XPATH, '//*[@class="dao-dialog-backdrop alert-dialog"]//button[2]'),
              'targetnum_loc':(By.XPATH, '//*[@class="dao-setting-section"]/div[1]/div[1]/div[1]/div[2]//input'),
              'chooseversion_loc':(By.XPATH,'//*[@class="dao-dialog-body"]/div[1]/div[2]/div[2]/div[1]/div/div[1]/div/div[1]'),
              'versionsearch_loc':(By.XPATH,'//*[@class="search-container"]/input'),
              'foundversion_loc':(By.XPATH,'//*[@class="dao-select-category"]/div[3]/span'),
              'noty_loc':(By.XPATH,'//*[@class="noty_body"]'),
              }


class BasePage():
    def __init__(self):
        self.driver = TestWebDriver
        self.base_url = ServerAddr
        # self.pagetitle = pagetitle

    # def on_page(self,pagetitle):
    def on_page(self):
        return pagetitle in driver.dr.title  # 根据传过来的pagetitle判断是否在正确界面

    # def _open(self,url,pagetitle):
    def _open(self, url):
        self.driver.get(url)
        self.driver.set_window_size(1400, 1200)

    def open(self):
        # self._open(self.base_url,self.pagetitle)
        self._open(self.base_url)

    def find_element(self, key):
        # return self.driver.find_element(*loc)
        try:
            loc = allelement[key]
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))          #确保元素可见
            return self.driver.find_element(*loc)
        # except Exception as e:
        #     logging.exception(e)
        except:
        #     print('AttributeError:',e)

        # except:
        #     pass
        #     print('页面中未能找到{}元素'.format(key))
        #
            raise AttributeError('页面中未能找到{}元素'.format(key))

    def type(self, key, value):
        try:
            self.find_element(key).send_keys(value)
        except AttributeError:
            raise AttributeError('{}元素不能传值'.format(key))


    def click_element(self,loc):
        self.find_element(loc).click()

    def clearcontent(self,key):
        self.find_element(key).clear()

    # def send_key(self, *loc, value):
    #     # if click first:
    #     #     self.driver.find_element(*loc).click()
    #     # if clear first:
    #     #     self.driver.find_element(*loc).clear()
    #     return self.driver.find_element(*loc).send_keys(vaule)

    def close(self):
        self.driver.close()

    def screenshot(self,image_name = 'test',num = []):
        num.append(1)
        base_dir = os.path.dirname(os.path.dirname(__file__))
        file_path = base_dir + "/image/" + image_name + str(len(num)) + '.png'
        print(file_path)
        self.driver.get_screenshot_as_file(file_path)

    def action_result(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/nav/div[1]/div/ul/li/span/span'))
            )
            while element:
                print('login success')
                break
        finally:
            self.driver.close()


if __name__ == '__main__':
    login_page = BasePage()
    login_page.open()
    loginlist = {'username_loc': 'admin', 'password_loc': 'changeme'}
    for k, v in loginlist.items():
        login_page.type(k, v)
    login_page.click_element('submit_loc')
    login_page.screenshot('login')
    while login_page.action_result():
        pass
allelement = {'login_username_loc': (By.XPATH, '//*[@class="login-page"]/div[2]/div[1]/div[1]/div[1]//input'),
              'login_password_loc': (By.XPATH, '//*[@class="login-page"]/div[2]/div[1]/div[1]/div[2]//input'),
              'login_submit_loc': (By.XPATH, '//*[@id="login"]//button[1]'),    #登陆界面前缀 login
              'sidebar_applist_loc': (By.XPATH, '//*[@id="app"]//menu//section[2]/menu/span'),  #侧边栏 sidebar
              'applist_loc_firstapp': (By.XPATH, '//*[@class="dao-table-view unselectable"]//tr[1]/td[1]/a'),
              'applist_createapp_loc': (By.XPATH, '//*[@class="dao-btn blue has-icon"]'),   #应用列表界面 applist
              'applist_createapp_advancefuc_loc': (By.XPATH, '//*[@class="dao-radio-group"]/p/a'),
              'applist_createapp_createbyyaml_loc': (By.XPATH, '//*[@class="dao-radio-group"]/div[4]//input'),
              'applist_createapp_createbyimage_loc':(By.XPATH,'//*[@class="dao-radio-group"]/div[3]//input'),
              'applist_createapp_continue_create_loc': (By.XPATH, '//*[@class="dao-btn blue has-icon compact"]'),   #应用列表创建应用方式
              'applist_createappbyyml_app_name_loc': (By.XPATH, '//*[@class="dao-input-inner"]//input'),
              'applist_createappbyyml_try2048_loc': (By.XPATH, '//*[@class="dao-setting-section"]//a[1]'),
              'applist_createappbyyml_confirm_create_loc': (By.XPATH, '//*[@class="dao-steps"]/div[2]//button[1]'), #通过yml编排应用前缀 applist_createappbyyml
              'applist_createappbyimage_customedimage_loc':(By.XPATH,'//*[@class="nav-top lively"]/div[2]'),
              'applist_createappbyimage_imagename_loc':(By.XPATH,'//*[@class="dao-setting-section"]//div[2]/div/div/div[1]/div/div/div/div[1]/input'),
              'applist_createappbyimage_checkaddr_loc':(By.XPATH,'/html/body/div[3]/div[2]/div/div/div[2]/button'), #检验地址
              'applist_createappbyimage_continue_loc':(By.XPATH,'//*[@id="app"]/div[2]/div/div/div[2]/div/button[3]'),
              'applist_createappbyimage_auditapp_loc':(By.XPATH,'//*[@class="dao-btn green"]'),
              'applist_createappbyimage_confirm_loc':(By.XPATH,'//*[@id="app"]/div[2]/div/div/div[2]/div/button[2]/span'),
              'appdetail_opentty_loc': (By.XPATH, '//*[@class="dao-table-view-toolbar"]//span[1]/button[1]'),
              'appdetail_changerc_loc': (By.XPATH, '//*[@class="dao-table-view-toolbar"]//span[1]/button[2]'),
              'appdetail_changeimg_loc': (By.XPATH, '//*[@class="dao-table-view-toolbar"]//span[1]/button[3]'),
              'appdetail_startdeployment_loc': (By.XPATH, '//*[@class="dao-table-view-toolbar"]//span[2]/button[1]'),
              'appdetail_stopdeployment_loc': (By.XPATH, '//*[@class="dao-table-view-toolbar"]//span[2]/button[2]'),
              'appdetail_restartdeployment_loc': (By.XPATH, '//*[@class="dao-table-view-toolbar"]//span[2]/button[3]'),
              'appdetail_setlabel_loc': (By.XPATH, '//*[@class="dao-table-view-toolbar"]//span[3]/button[1]'),  #应用详情前缀 appdetail
              'toolbarconfig_loc': (By.XPATH, '//*[@class="dao-table-view-toolbar"]//span[3]/div'),
              'assure_loc': (By.XPATH, '//*[@class="dao-dialog-footer"]//button[2]'),
              'save_loc': (By.XPATH, '//*[@class="dao-dialog-backdrop alert-dialog"]//button[2]'),
              'targetnum_loc': (By.XPATH, '//*[@class="dao-setting-section"]/div[1]/div[1]/div[1]/div[2]//input'),
              'chooseversion_loc': (
                  By.XPATH, '//*[@class="dao-dialog-body"]/div[1]/div[2]/div[2]/div[1]/div/div[1]/div/div[1]'),
              'versionsearch_loc': (By.XPATH, '//*[@class="search-container"]/input'),
              'foundversion_loc': (By.XPATH, '//*[@class="dao-select-category"]/div[3]/span'),
              'noty_loc': (By.XPATH, '//*[@class="noty_body"]'),
              'managedeployment_assure_loc': (By.XPATH, '//*[@class="dao-dialog-footer"]//button[2]')
              }

# 元素查找根据前缀查表
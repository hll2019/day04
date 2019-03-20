"""
    编写：
        1. 类名：将模块名称以大驼峰写法抄进来，如果有下划线去掉下划线
        2. 函数：
            每一步操作单独封装一个函数，如果需要组装，最后进行调用单步函数进行组装业务调用方法

"""
from selenium.webdriver.common.by import By

from base.base import Base


"""配置数据，临时存放此地方"""
login_username = By.ID, "com.vcooline.aike:id/etxt_username"
login_pwd = By.ID, "com.vcooline.aike:id/etxt_pwd"
login_btn = By.ID, "com.vcooline.aike:id/btn_login"

# 新建 登录页面对象类
class PageLogin(Base):

    # 输入用户名 封装
    def page_input_username(self, usrename):
        self.base_input(login_username, usrename)

    # 输入密码 封装
    def page_input_pwd(self, pwd):
        self.base_input(login_pwd, pwd)

    # 点击登录 封装
    def page_click_login_btn(self):
        self.base_click(login_btn)

    # 组装登录方法 给业务层调用
    def page_login(self, username, pwd):
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()

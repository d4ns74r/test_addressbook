from selenium.webdriver.common.by import By

class SessionHelper():

    def __init__(self, app):
        self.app = app

    def Login(self, email, password):
        self.driver = self.app.driver
        self.driver.get("https://www.postable.com/login")
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "email").send_keys(email)
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.app.driver.find_element(By.CSS_SELECTOR, ".full-width:nth-child(4)").click()

    def Logout(self):
        self.driver = self.app.driver
        self.driver.find_element(By.CSS_SELECTOR, 'li.main-header__link.main-header__link--account>a').click()
        self.driver.find_element(By.CSS_SELECTOR, 'li.main-header__link.main-header__link--account>div>ul>li:nth-child(8)>a').click()

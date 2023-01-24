from selenium import webdriver
from selenium.webdriver.common.by import By

class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.vars = {}
        self.driver.implicitly_wait(30)


    def Logout(self):
        # Logout
        self.driver.find_element(By.CSS_SELECTOR, 'li.main-header__link.main-header__link--account>a').click()
        self.driver.find_element(By.CSS_SELECTOR, 'li.main-header__link.main-header__link--account>div>ul>li:nth-child(8)>a').click()

    def Add_new_contact(self, contact):
        # Add new contact
        self.driver.find_element(By.LINK_TEXT, "Address book").click()
        self.driver.find_element(By.CSS_SELECTOR, 'div.search-toolbar>span>button').click()
        self.driver.find_element(By.CSS_SELECTOR, '#modal-add-contacts>div>div>a:nth-child(4)').click()
        self.driver.find_element(By.CSS_SELECTOR, 'form>div:nth-child(1)>div>div:nth-child(2)>input[type=text]').click()
        self.driver.find_element(By.CSS_SELECTOR, 'form>div:nth-child(1)>div>div:nth-child(2)>input[type=text]').send_keys(contact.FirstName)
        self.driver.find_element(By.CSS_SELECTOR, 'form>div:nth-child(1)>div>div:nth-child(3)>input[type=text]').click()
        self.driver.find_element(By.CSS_SELECTOR, 'form>div:nth-child(1)>div>div:nth-child(3)>input[type=text]').send_keys(contact.LastName)
        self.driver.find_element(By.CSS_SELECTOR, 'form>div:nth-child(2)>div>div:nth-child(1)>div>input').click()
        self.driver.find_element(By.CSS_SELECTOR, 'form>div:nth-child(2)>div>div:nth-child(1)>div>input').send_keys(contact.Street)
        self.driver.find_element(By.CSS_SELECTOR, 'div>div.panel-next__footer>button').click()

    def Login(self, email, password):
        # Login
        self.driver.get("https://www.postable.com/login")
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "email").send_keys(email)
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, ".full-width:nth-child(4)").click()

    def Destroy(self):
        self.driver.quit()
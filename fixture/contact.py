from selenium.webdriver.common.by import By

class ContactHelper():
    def __init__(self, app):
        self.app = app

    def Add(self, contact):
        self.driver = self.app.driver
        self.driver.find_element(By.LINK_TEXT, "Address book").click()
        self.driver.find_element(By.CSS_SELECTOR, 'div.search-toolbar>span>button').click()
        self.driver.find_element(By.CSS_SELECTOR, '#modal-add-contacts>div>div>a:nth-child(4)').click()
        self.driver.find_element(By.CSS_SELECTOR, 'form>div:nth-child(1)>div>div:nth-child(2)>input[type=text]').click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 'form>div:nth-child(1)>div>div:nth-child(2)>input[type=text]').send_keys(
            contact.FirstName)
        self.driver.find_element(By.CSS_SELECTOR, 'form>div:nth-child(1)>div>div:nth-child(3)>input[type=text]').click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 'form>div:nth-child(1)>div>div:nth-child(3)>input[type=text]').send_keys(
            contact.LastName)
        self.driver.find_element(By.CSS_SELECTOR, 'form>div:nth-child(2)>div>div:nth-child(1)>div>input').click()
        self.driver.find_element(By.CSS_SELECTOR, 'form>div:nth-child(2)>div>div:nth-child(1)>div>input').send_keys(
            contact.Street)
        self.driver.find_element(By.CSS_SELECTOR, 'div>div.panel-next__footer>button').click()


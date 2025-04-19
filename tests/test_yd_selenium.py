import time
from unittest import TestCase

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome, ChromeOptions, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


login = 'логин'
password = 'пароль'

class TestAuthYD(TestCase):
    def setUp(self):
        self.chrom_path = ChromeDriverManager().install()
        self.service = Service(executable_path=self.chrom_path)
        self.browser = Chrome(service=self.service)

    def test_auth(self):
        self.browser.get('https://passport.yandex.ru/auth/add/login')
        item = self.browser.find_element(by=By.ID, value='passp-field-login')
        item.send_keys(login)
        self.browser.find_element(by=By.ID, value='passp:sign-in').click()
        time.sleep(2)
        item = self.browser.find_element(by=By.ID, value='passp-field-passwd')
        item.send_keys(password)
        self.browser.find_element(by=By.ID, value='passp:sign-in').click()
        time.sleep(10)

    def tearDown(self):
        self.browser.close()




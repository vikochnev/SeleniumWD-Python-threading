from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import threading


class AutoTests():

    def __init__(self):
        self.setUp()
        self.tstBody()
        self.tearDown()

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def tstBody(self):
        pass

    def typeAndClick(self, finder_type, finder, search_text):
        element = self.driver.find_element(finder_type, finder)
        element.send_keys(search_text)
        element.send_keys(Keys.ENTER)

    def tearDown(self):
        self.driver.quit()


class ChromeTest1(AutoTests):

    def tstBody(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.google.com/")
        self.typeAndClick(By.NAME, 'q', 'Котята')
        time.sleep(3)


class ChromeTest2(AutoTests):

    def tstBody(self):
        driver = self.driver
        driver.get("https://yandex.ru/metro/moscow?scheme_id=sc34974011")
        self.typeAndClick(By.XPATH, '//*[@placeholder="Откуда"]', 'Новаторская')
        self.typeAndClick(By.XPATH, '//*[@placeholder="Куда"]', 'Преображенская площадь')
        time.sleep(3)


class ChromeTest3(AutoTests):

    def tstBody(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.google.com/")
        self.typeAndClick(By.NAME, 'q', 'Поссумы')
        time.sleep(3)


def run_threads(atests):
    threads = []

    for atest in atests:
        threads.append(threading.Thread(target=atest))

    for t in threads:
        t.start()

    for t in threads:
        t.join()

autoTests = [ChromeTest1, ChromeTest2, ChromeTest3]
run_threads(autoTests)

print("Done!")

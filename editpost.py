import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Blog_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        user = "Astha1"
        pwd = "Saujanya11"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000/admin")
        assert "Logged In"
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr/td[2]").click()
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[2]/table/tbody/tr[1]/th/a")
        elem.click()
        time.sleep(3)

        elem = driver.find_element_by_id("id_title")
        elem.click()
        elem.clear()git
        elem.send_keys("Dr. Royce is the best.")
        time.sleep(5)

        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/input[1]")
        elem.click()
        time.sleep(3)


        def tearDown(self):
            self.driver.quit()

        if __name__ == "__main__":
         unittest.main()
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Blog_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        user = "instructor1"
        pwd = "maverick1a"
        driver = self.driver
        #driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin/")
        #elem = driver.find_element_by_xpath("//*[@id=\"myNavbar\"]/ul[2]/li/a").click()

        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        assert "Logged In"
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr[2]/td[2]")
        elem.click()
        time.sleep(1)
        #elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/div[3]/table/tbody/tr[1]/td[13]/a").click()
        time.sleep(1)
        #driver.switch_to.alert.accept()

        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[2]/table/tbody/tr[1]/td[1]")
        elem.click()
        time.sleep(1)

        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[1]/label/select/option[2]")
        elem.click()
        time.sleep(3)

        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[1]/button")
        elem.click()
        time.sleep(3)

        elem = driver.find_element_by_xpath("/html/body/div/div[3]/form/div/input[4]")
        elem.click()
        time.sleep(4)


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
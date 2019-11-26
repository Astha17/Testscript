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
        driver.get("http://127.0.0.1:8000/admin")
        #elem = driver.find_element_by_xpath("//*[@id=\"myNavbar\"]/ul[2]/li/a").click()

        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        #driver.get("http://127.0.0.1:8000/admin")
        assert "Logged In"
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr[2]/td[1]")
        elem.click()
        time.sleep(3)
        #elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/div[3]/div/a/span").click()
        time.sleep(3)


        elem = driver.find_element_by_xpath("//*[@id=\"id_cust_name\"]/option[2]").click()

        elem = driver.find_element_by_id("id_product")
        elem.send_keys("Sports shoes")
        time.sleep(3)

        elem = driver.find_element_by_id("id_p_description")
        elem.send_keys("Nike  Air Zoom Vapor X Tennis Shoes Wheat and Metallic Silver")
        time.sleep(3)

        elem = driver.find_element_by_id("id_quantity")
        elem.send_keys("3")
        time.sleep(3)

        elem = driver.find_element_by_id("id_charge")
        elem.send_keys("140")
        time.sleep(3)

        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/input[1]")
        elem.click()
        time.sleep(3)





    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
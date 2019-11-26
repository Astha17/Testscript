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
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[1]/a").click()
        time.sleep(1)
       # elem = driver.find_element_by_xpath ("//*[@id="id_cust_name\"]").click()
        time.sleep(2)


        elem = driver.find_element_by_xpath("//*[@id=\"id_cust_name\"]")
        elem.click()
        elem.send_keys("Anvi Dhakal")
        time.sleep(5)

        elem = driver.find_element_by_xpath("//*[@id=\"id_organization\"]")
        elem.click()
        elem.send_keys("UNO")
        time.sleep(5)

        elem = driver.find_element_by_xpath("//*[@id=\"id_role\"]")
        #// *[ @ id = "id_role"]
        elem.click()
        elem.send_keys("Student")
        time.sleep(4)

        elem = driver.find_element_by_xpath("//*[@id=\"id_email\"]")
        elem.click()
        elem.send_keys("smani@unomaha.edu")
        time.sleep(4)

        elem = driver.find_element_by_xpath("//*[@id=\"id_bldgroom\"]")
        elem.click()
        elem.send_keys("11")
        time.sleep(2)

        elem = driver.find_element_by_xpath("//*[@id=\"id_address\"]")
        elem.click()
        elem.send_keys("Nepal")
        time.sleep(4)

        elem = driver.find_element_by_xpath("//*[@id=\"id_account_number\"]")
        elem.click()
        elem.send_keys("75")
        time.sleep(5)

        elem = driver.find_element_by_xpath("//*[@id=\"id_city\"]")
        elem.click()
        elem.send_keys("Boston")
        time.sleep(5)

        elem = driver.find_element_by_xpath("//*[@id=\"id_state\"]")
        elem.click()
        elem.send_keys("NE")
        time.sleep(5)

        elem = driver.find_element_by_xpath("//*[@id=\"id_zipcode\"]")
        elem.click()
        elem.send_keys("68175")
        time.sleep(5)

        elem = driver.find_element_by_xpath("//*[@id=\"id_phone_number\"]")
        elem.click()
        elem.send_keys("565122547")
        time.sleep(5)

        elem = driver.find_element_by_xpath("//*[@id=\"id_created_date_0\"]")
        #// *[ @ id = "id_created_date_0"]
        elem.click()
        elem.clear()
        elem.send_keys("11/22/2019")
        time.sleep(5)

        elem = driver.find_element_by_xpath("//*[@id=\"id_created_date_1\"]")
        # // *[ @ id = "id_created_date_0"]
        elem.click()
        elem.clear()
        elem.send_keys("10:30:00")
        time.sleep(5)

        elem = driver.find_element_by_xpath(" / html / body / div[1] / div[3] / div / form / div / div / input[1]")
        elem.click()
        time.sleep(2)



    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
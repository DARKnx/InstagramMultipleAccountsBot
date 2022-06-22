from selenium.webdriver.common.keys import Keys 
import time


def run(self):

        username = self.username
        passowrd = self.password
        driver = self.driver

        driver.get("https://www.instagram.com")
        time.sleep(5)
 
        userForm = driver.find_element_by_xpath("//input[@name='username']")
        userForm.click()
        userForm.clear()
        userForm.send_keys(self.username)

        passwordForm = driver.find_element_by_xpath("//input[@name='password']")
        passwordForm.click()
        passwordForm.clear()
        passwordForm.send_keys(self.password)
        passwordForm.send_keys(Keys.RETURN)

        time.sleep(5)
        driver.get(self.post)
        time.sleep(3)

        try:
           checkInput = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea")   
        except:
            return 'user not logged'

        return 'user logged'

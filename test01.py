import fileinput
import time
from selenium import webdriver
import const as con
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class pimtest01(webdriver.Firefox):
    def __init__(self):
        super(pimtest01, self).__init__()
        self.implicitly_wait(10)

    def landing_page(self):
        self.get(con.URL)
    def forgotpass(self):
        forgotpasslink = self.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p")
        forgotpasslink.click()
        username = self.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div/form/div[1]/div/div[2]/input")
        if bool(username.is_displayed()) == True:
            try:
                print("User name field is displayed")
                username.send_keys("Testuser123")
                resetpass = self.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div/form/div[2]/button[2]").click()
                sucessmsg = self.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div/h6")
                if bool(sucessmsg.is_displayed()) == True:
                    print(f"{sucessmsg.text}  for the Given User")
                else:
                    print("Unable to access the Pop up Window")
            except:
                print("User name field is Not dispalyed")
        else:
            print("Not access")
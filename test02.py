import time

from selenium import webdriver
from selenium.webdriver.common.by import By

import const
import const as con


class pim_test_02(webdriver.Firefox):
    def __init__(self):
        super(pim_test_02, self).__init__()
        self.implicitly_wait(10)
    def landing_page(self):
        self.get(con.URL)
    def titlepage(self):
        webpagetitle = self.title
        print(webpagetitle)
        if str(webpagetitle) == str(con.LOGIN_TITLE):
            print(f"You are loggin in Successfully and the Current page title is {webpagetitle}")
        else:
            print("You are landing in wrong page")
    def login(self):
        username = self.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input")
        username.send_keys(con.USER_NAME)
        password = self.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input")
        password.send_keys(con.PASSWORD)
        login = self.find_element(By.CSS_SELECTOR, 'button[type = "submit"]')
        login.click()
    def adminpage(self):
        Admin = self.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span")
        Admin.click()
    def backbutton(self):
        self.back
    def menus(self):
        usermgmt = bool(self.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]").is_displayed())
        if usermgmt == True:
            print("The Usermanagement icon is Displayed")
            usersinmgmt = self.find_element(By.XPATH,
                                            "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span").click()
            userinmgmt1 = self.find_element(By.XPATH,
                                            "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li/a").click()
            time.sleep(5)
            userinmgmt3 = self.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span")
            print(f"The  {userinmgmt3.text} in User management Number of employees")
            self.backbutton()
        else:
            print("The Usermanagement icon is Not Displayed ")
        job = self.find_element(By.CSS_SELECTOR, "li.oxd-topbar-body-nav-tab:nth-child(2) > span").is_displayed()
        if bool(job) == True:
            print("The Job icon is Displayed")
            jobtitles = self.find_element(By.CSS_SELECTOR, "li.oxd-topbar-body-nav-tab:nth-child(2) > span").click()
            shifts = self.find_element(By.CSS_SELECTOR, ".oxd-dropdown-menu > li:nth-child(5) > a:nth-child(1)").click()
            time.sleep(5)
            no_of_shifts = self.find_element(By.CSS_SELECTOR, "span.oxd-text:nth-child(1)")
            print(f"The {no_of_shifts.text} in number of shifts")
        else:
            print("The Job icon os not displayed")

        organization = bool(self.find_element(By.CSS_SELECTOR, "li.oxd-topbar-body-nav-tab:nth-child(3) > span").is_displayed())
        if organization == True:
            print("The Organization icon is displayed")
            organization1 = self.find_element(By.CSS_SELECTOR, "li.oxd-topbar-body-nav-tab:nth-child(3) > span").click()
            locations = self.find_element(By.CSS_SELECTOR, ".oxd-dropdown-menu > li:nth-child(2) > a:nth-child(1)").click()
            time.sleep(5)
            com_locations = self.find_element(By.CSS_SELECTOR, "span.oxd-text:nth-child(1)")
            print(f"{com_locations.text} in Company Locations")
        else:
            print("The Organization icon is not displayed")
        qualification = bool(self.find_element(By.CSS_SELECTOR, "li.oxd-topbar-body-nav-tab:nth-child(4) > span:nth-child(1)").is_displayed())
        if qualification == True:
            print("The Qualification icon is displayed")
            qualification1 = self.find_element(By.CSS_SELECTOR, "li.oxd-topbar-body-nav-tab:nth-child(4) > span:nth-child(1)").click()
            skills = self.find_element(By.CSS_SELECTOR, ".oxd-dropdown-menu > li:nth-child(1)").click()
            time.sleep(5)
            skillstext = self.find_element(By.CSS_SELECTOR, "span.oxd-text:nth-child(1)")
            print(f"{skillstext.text} in Skills menu")
        else:
            print("The Qualification icon not displayed")
        nationality = bool(self.find_element(By.CSS_SELECTOR, "li.oxd-topbar-body-nav-tab:nth-child(5) > a:nth-child(1)").is_displayed())
        if nationality == True:
            print("The nationality icon is Displayed")
            nationality1 = self.find_element(By.CSS_SELECTOR, "li.oxd-topbar-body-nav-tab:nth-child(5) > a:nth-child(1)").click()
            time.sleep(5)
            nationality2 = self.find_element(By.CSS_SELECTOR, "span.oxd-text:nth-child(1)")
            print(f"{nationality2.text} in Nationality menu")
        else:
            print("The nationality icon not displayed")
        corporatebrand = bool(self.find_element(By.CSS_SELECTOR, "li.oxd-topbar-body-nav-tab:nth-child(6) > a:nth-child(1)").is_displayed())
        if corporatebrand == True:
            print("The Corporate Branding menu is Displayed")
            corporatebrand1 = self.find_element(By.CSS_SELECTOR, "li.oxd-topbar-body-nav-tab:nth-child(6) > a:nth-child(1)").click()
            colour = self.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div").click()
            time.sleep(5)
            colourhexvalue = self.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[2]/input[2]")
            print(f"The Primary colour hex value is {colourhexvalue.text}")
        else:
            print("The Corporate Branding icon not displayed")
        config = bool(self.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[7]/span"))
        if config == True:
            print("The Configuration icon displayed")
            config1 = self.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[7]/span").click()
            lang_in_config = self.find_element(By.CSS_SELECTOR, ".oxd-dropdown-menu > li:nth-child(4) > a:nth-child(1)").click()
            time.sleep(5)
            languages = self.find_element(By.CSS_SELECTOR, "span.oxd-text:nth-child(1)")
            print(f"{languages.text} in Languages Module")
        else:
            print("The Configuration icon not displayed")











    def logout(self):
        self.find_element(By.CSS_SELECTOR, "i.oxd-icon:nth-child(3)").click()
        self.find_element(By.CSS_SELECTOR, ".oxd-dropdown-menu > li:nth-child(4) > a:nth-child(1)").click()
        print("you Are logged Out Successfully")


















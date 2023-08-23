import fileinput
import time
from selenium import webdriver
import const as con
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait





class pimtest03(webdriver.Firefox):

    def __init__(self):
        super(pimtest03, self).__init__()
        self.implicitly_wait(10)

    def landing_page(self):
        self.get(con.URL)

    def login(self):
        username = self.find_element(By.XPATH,
                                     "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input")
        username.send_keys(con.USER_NAME)
        password = self.find_element(By.XPATH,
                                     "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input")
        password.send_keys(con.PASSWORD)
        login = self.find_element(By.CSS_SELECTOR, 'button[type = "submit"]')
        login.click()

    def admin(self):
        adminmenu = self.find_element(By.CSS_SELECTOR, ".active > span:nth-child(2)")
        if bool(adminmenu.is_displayed()) == True:
            print("Admin Menu is Diaplayed")
            adminmenu1 = self.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span").click()
            time.sleep(5)
            users = self.find_element(By.CSS_SELECTOR, "span.oxd-text:nth-child(1)")
            print(f"{users.text} in User Management")
        else:
            print("Admin Menu is Not Diaplayed")
    def pim(self):
        pimmmenu = self.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span")
        if bool(pimmmenu.is_displayed()) == True:
            try:
                print("PIM Menu is Displayed")
                pimmmenu.click()
                time.sleep(5)
                pimemplist = self.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span")
                print(f"{pimemplist.text} in PIM Employee List")
            except:
                print("PIM Employee List is Unable to Access")
        else:
            print("PIM Menu is Not Displayed")
    def leave(self):
        leavemenu = self.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a/span")
        if bool(leavemenu.is_displayed()) == True:
            try:
                print("leave Menu is Displayed")
                leavemenu.click()
                time.sleep(5)
                leaverec = self.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/span")
                print(f"{leaverec.text} in Leave Menu")
            except:
                print("Unable to find Leave Records")
        else:
            print("Leave Menu is Not Displayed")

    def timesheet(self):
        timemenu = self.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a/span")
        if bool(timemenu.is_displayed()) == True:
            try:
                print("Time menu is Displayed")
                timemenu.click()
                time.sleep(5)
                timesheetpending = self.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span")
                print(f"{timesheetpending.text} in Time Sheet Pending Action")
            except:
                print("Time Sheet Pending Action menu Not Dispalyed")
        else:
            print("Time menu is Not Displayed")
    def recruitment(self):
        recmenu = self.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a/span")
        if bool(recmenu.is_displayed()) == True:
            try:
                print("Recruitment Menu is Displayed")
                recmenu.click()
                time.sleep(5)
                reccount = self.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span")
                print(f"{reccount.text} in candidate Recruitment Menu")
            except:
                print("The Candidate Recruitment Menu is Not Shown")
        else:
            print("Recruitment Menu is Not Displayed")
    def myinfo(self):
        myinfomenu = self.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a/span")
        if bool(myinfomenu.is_displayed()) == True:
            try:
                print("MY Info Menu is Displayed")
                myinfomenu.click()
                time.sleep(5)
                loggedinuser = self.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[1]/div[1]/h6")
                print(f"The Current LoggedIn User is {loggedinuser.text} ")
            except:
                print("My Info Menu is not shown")
        else:
            print("My Info Menu is Not Displayed")
    def performance(self):
        performance1 = self.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a/span")
        if bool(performance1.is_displayed()) == True:
            try:
                print("Performance Menu is Displayed")
                performance1.click()
                time.sleep(5)
                mytrackers = self.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]").click()
                time.sleep(5)
                mytrackers1 = self.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div[2]/div/span")
                print(f"{mytrackers1.text} in My Performance Trackers")
            except:
                print("Unable to find My Performance Tracker")
        else:
            print("Performance Menu is Not Displayed")
    def dashboard(self):
        dashboardmenu = self.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a/span")
        if bool(dashboardmenu.is_displayed()) == True:
            try:
                print("Dashboard Menu is Displayed")
                dashboardmenu.click()
                punchedintime = self.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/div[2]/p[2]")
                print(f" The Current User is {punchedintime.text}")
            except:
                print("Unable to find Dashboard Menu")
        else:
            print("Dashboard Menu is Not Displayed")
    def directory(self):
        directorymenu = self.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a/span")
        if bool(directorymenu.is_displayed()) == True:
            try:
                print("Directory option is Displayed")
                directorymenu.click()
                time.sleep(5)
                dir = self.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/span")
                print(f"{dir.text} in Directory")
            except:
                print("Unable to find the Directory option")
        else:
            print("Directory option is Not Displayed")
    def maintanance(self):
        maintainancemenu = self.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[10]/a/span")
        if bool(maintainancemenu.is_displayed()) == True:
            try:
                print("Maintanamce Menu is Displayed")
                maintainancemenu.click()
                time.sleep(5)
                win = self.switch_to.alert
                print(self.current_window_handle)
                alertmsg = self.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/form/div[1]/toast-message")
                print(f" The Alert Message dispalyed is {alertmsg.text}")

            except:
                print("Unable to access the alert Window")
        else:
            print("Maintanamce Menu is Not Displayed")
        self.back()
    def claim(self):
        claimmenu = self.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[11]/a/span")
        if bool(claimmenu.is_displayed()) == True:
            try:
                print("The Claim menu is Displayed")
                claimmenu.click()
                time.sleep(5)
                empclaims = self.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/span")
                print(f"{empclaims.text} in Employees Claim")
            except:
                print("Unable to access Emp Claim Menu")
        else:
            print("The Claim menu is Not Displayed")
    def buzz(self):
        buzzmenu = self.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[12]/a/span")
        if bool(buzzmenu.is_displayed()) == True:
            try:
                print("Buzz Menu is Displayed")
                buzzmenu.click()
                time.sleep(5)
                user = self.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[2]/p[1]")
                usermsg = self.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div[2]/div/div[2]/div/p[5]")
                print(f"{user.text} wrote {usermsg.text}")
            except:
                print("Unable to access Buzz menu")
        else:
            print("Buzz Menu is Not Displayed")





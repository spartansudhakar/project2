from test01 import pimtest01
from test02 import pim_test_02
from test03 import pimtest03
import time
import const as con
ins2 = pimtest01()
ins2.landing_page()
ins2.forgotpass()

inst = pim_test_02()
inst.landing_page()
time.sleep(5)
inst.login()
inst.titlepage()
inst.adminpage()
inst.menus()
inst.backbutton()

ins1 = pimtest03()
ins1.landing_page()
time.sleep(5)
ins1.login()
ins1.admin()
ins1.pim()
ins1.leave()
ins1.timesheet()
ins1.recruitment()
ins1.myinfo()
ins1.performance()
ins1.dashboard()
ins1.directory()
ins1.maintanance()
ins1.claim()
ins1.buzz()







#time.sleep(15)
#inst.logout()

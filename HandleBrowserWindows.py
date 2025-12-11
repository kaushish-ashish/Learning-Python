import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")

# Initialize driver with options
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=chrome_options
)

driver.implicitly_wait(10)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

# window_id=driver.current_window_handle
# print(window_id) #CDwindow-24CFB4FFB7CB60C7309293A9217B9F2A
#               #CDwindow-E7283DA0F55EF107A63C1CD349434080

driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
windowsIDs=driver.window_handles

#Approach1
# parent_window_id=windowsIDs[0] #CDwindow-A82AD2C060A4BBCAFAD3DF3C6172CCBE
# child_window_id=windowsIDs[1] #CDwindow-F63E2A3D2324F7132FFD60C9A8E16A95
# print(parent_window_id,child_window_id)
#
# driver.switch_to.window(child_window_id)
# print("title of the child window",driver.title)
#
# driver.switch_to.window(parent_window_id)
# print("title of the parent window",driver.title)

#Approach2

# for win_id in windowsIDs:
#     driver.switch_to.window(win_id)
#     print(driver.title)

time.sleep(3)

#Close specific browser windows   1 2 3
for win_id in windowsIDs:
    driver.switch_to.window(win_id)
    if driver.title=="Human Resources Management Software | HRMS | OrangeHRM" or driver.title=='XYZ':
        driver.close()
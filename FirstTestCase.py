#Test Case
#------------------
# 1) Open Web Browser(Chrome/firefox/Edge).
# 2) Open URL  https://opensource-demo.orangehrmlive.com/
# 3) Enter username  (Admin).
# 4) Enter password  (admin123).
# 5) Click on Login.
# 6) Capture title of the home page.(Actual title)
# 7) Verify title of the page: OrangeHRM    (Expected)
# 8) close browser

from selenium import webdriver

#Selenium 3
#driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
    ## driver=webdriver.Chrome()
# driver.get("https://opensource-demo.orangehrmlive.com/")
# driver.find_element_by_name("txtUsername").send_keys("Admin")
# driver.find_element_by_id("txtPassword").send_keys("admin123")
# driver.find_element_by_id("btnLogin").click()
# act_title=driver.title
# exp_title="OrangeHRM"
# if act_title==exp_title:
#     print("Login Test Passed")
# else:
#     print("Login Test Failed")
# driver.close()

#Selenium4
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
# driver=webdriver.Chrome(service=serv_obj)
# ##driver=webdriver.Chrome()
# driver.get("https://opensource-demo.orangehrmlive.com/")
# driver.find_element(By.NAME,"txtUsername").send_keys("Admin")
# driver.find_element(By.ID,"txtPassword").send_keys("admin123")
# driver.find_element(By.ID,"btnLogin").click()

# act_title=driver.title
# exp_title="OrangeHRM"
# if act_title==exp_title:
#     print("Login Test Passed")
# else:
#     print("Login Test Failed")
# driver.close()

#Selenium5
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
##driver=webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/login")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@id='Email']").clear()
driver.find_element(By.XPATH,"//input[@id='Email']").send_keys("admin@yourstore.com")
driver.find_element(By.XPATH,"//input[@id='Password']").clear()
driver.find_element(By.XPATH,"//input[@id='Password']").send_keys("admin")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

act_title=driver.title
exp_title="Dashboard / nopCommerce administration"
if act_title==exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")
driver.close()
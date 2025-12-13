from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")

# Initialize driver with options
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=chrome_options
)

driver.implicitly_wait(10)

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)  #switch to frame

#driver.find_element(By.XPATH,"//*[@id='datepicker']").send_keys("05/30/2022") #mm/dd/yyyy

year="2024"
month="April"
date="30"

driver.find_element(By.XPATH,"//*[@id='datepicker']").click() # opens datepicker


while True:
    mon=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yr=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text

    if mon==month and yr==year:
        break
    else:
        # driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[2]/span").click()  #Next arrow
        driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[1]/span").click() # Previous Arrow - old date

#select date

dates=driver.find_elements(By.XPATH,"//div[@id='ui-datepicker-div']//table/tbody/tr/td/a")

for ele in dates:
    if ele.text==date:
        ele.click()
        break

driver.quit()



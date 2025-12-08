import time

from selenium import webdriver
from selenium.webdriver import Keys
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

driver.get("https://demoqa.com/auto-complete")
driver.maximize_window()

element = driver.find_element(By.XPATH, "//span[normalize-space()='Type multiple color names']")
driver.execute_script("arguments[0].scrollIntoView();", element)

#Absulte xpath
# driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div/div/div/div[1]/div[2]/div/input").send_keys("R")
# time.sleep(1)

#Relative xpath
# driver.find_element(By.ID, "autoCompleteMultipleInput").send_keys('R')
# time.sleep(1)

# or  and
# driver.find_element(By.XPATH,"//input[@id='autoCompleteMultipleInput' or @type='text']").send_keys("R")
# time.sleep(1)

# driver.find_element(By.XPATH,"//input[@id='autoCompleteMultipleInput' and @type='text']").send_keys("R")
# time.sleep(1)

# contains() & start-with()
# driver.find_element(By.XPATH,"//input[contains(@id,'autoCompleteMultipleInput')]").send_keys("R")
# time.sleep(1)

# driver.find_element(By.XPATH,"//button[starts-with(@name,'submit_')]").click()
# driver.find_element(By.XPATH,"//input[starts-with(@id,'autoCompleteMultipleInput')]").send_keys("R")
# time.sleep(1)
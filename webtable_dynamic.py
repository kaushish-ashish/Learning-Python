import time

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

driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()

#Login
driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.TAG_NAME,"button").click()
time.sleep(3)

#Admin-->user management-->users
driver.find_element(By.XPATH,"//span[normalize-space()='Admin']").click()

#total rows in a table
rows = len(driver.find_elements(By.XPATH, "//div[@class='oxd-table-body']//div[@class='oxd-table-card']"))
print("total number of rows in a table:", rows)

count = 0
for r in range(1, rows + 1):
    status = driver.find_element(By.XPATH,"(//div[@class='oxd-table-body']//div[@class='oxd-table-card'])[" + str(r) + "]//div[text()='Enabled' or text()='Disabled']").text

    if status == "Enabled":
        count = count + 1

print("Total Number of users:", rows)
print("Number of enabled users:", count)
print("Number of disabled users:", (rows-count))

print("==================================================")

# Fetching users with ESS role
rows = driver.find_elements(By.XPATH, "//div[@class='oxd-table-body']//div[@class='oxd-table-card']")

print("Users with ESS role:\n")

for row in rows:
    username = row.find_element(By.XPATH, ".//div[@class='oxd-table-cell oxd-padding-cell'][2]").text
    role = row.find_element(By.XPATH, ".//div[@class='oxd-table-cell oxd-padding-cell'][3]").text

    if role == "ESS":
        print(f"Username: {username} | Role: {role}")

driver.close()



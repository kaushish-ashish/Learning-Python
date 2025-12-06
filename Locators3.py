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

driver.get("https://www.facebook.com/")
driver.maximize_window()

# tag & id
# driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc")
# driver.find_element(By.CSS_SELECTOR,"#email").send_keys("abc")

# tag and class
# driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("abc@gmail.com")

# driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys("abc@gmail.com")

# tag & attribute
# driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal-email]").send_keys("abc@gmail.com")
# driver.find_element(By.CSS_SELECTOR,"[data-testid=royal-email]").send_keys("abc@gmail.com")


# tag , class & attribute
# driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal-pass]").send_keys("xyz")


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

driver.implicitly_wait(10) # seconds  # implicit wait

driver.get("https://www.google.com/")
driver.maximize_window()

search_box=driver.find_element(By.NAME,'q')

search_box.send_keys("Selenium")
search_box.submit()


driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()

driver.quit()

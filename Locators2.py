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
##driver=webdriver.Chrome()
driver.get("https://demoqa.com/links")
driver.maximize_window()  #maximize the browser window

sliders=driver.find_elements(By.CLASS_NAME,'menu-list')
print(len(sliders)) #5    total number of sliders on home page

links=driver.find_elements(By.TAG_NAME,'a')
print(len(links)) #  149 total number of links on home page



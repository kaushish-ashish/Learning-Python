from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")

# Initialize driver with options
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=chrome_options
)


#mywait=WebDriverWait(driver,10) # explicit wait declaration # basic
my_wait=WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[NoSuchElementException,
                                                   ElementNotVisibleException,
                                                   ElementNotSelectableException,
                                                   Exception]
                     )


driver.get("https://www.google.com/")
driver.maximize_window()

search_box=driver.find_element(By.NAME,'q')

search_box.send_keys("Selenium")
search_box.submit()

search_link=my_wait.until(EC.presence_of_element_located((By.XPATH,"//h3[text()='Selenium']")))
search_link.click()


driver.quit()

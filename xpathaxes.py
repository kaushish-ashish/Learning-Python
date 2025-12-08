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
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()

#self
text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'Raymond Lifestyle L')]/self::a").text
print(text_msg) # Raymond Lifestyle L

#parent
text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'Raymond Lifestyle L')]/parent::td").text
print(text_msg) #Raymond Lifestyle L

#child
childs=driver.find_elements(By.XPATH,"//a[contains(text(),'Raymond Lifestyle L')]/ancestor::tr/child::td")
print(len(childs))  #6

#Ancestor
text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'Raymond Lifestyle L')]/ancestor::tr").text
print(text_msg) #Raymond Lifestyle L A 1,035.20 1,050.10 + 1.44 Buy  |  Sell

#Decendant
descendants=driver.find_elements(By.XPATH,"//a[contains(text(),'Raymond Lifestyle L')]/ancestor::tr/descendant::*")
print("Number of descendant nodes:",len(descendants)) #10

#Following
followings=driver.find_elements(By.XPATH,"//a[contains(text(),'Raymond Lifestyle L')]/ancestor::tr/following::*")
print("Number of following nodes:",len(followings)) #767

#Folowing-sibling
followingsiblings=driver.find_elements(By.XPATH,"//a[contains(text(),'Raymond Lifestyle L')]/ancestor::tr/following-sibling::*")
print("Number of following-sibling nodes:",len(followingsiblings)) #51

#preceding
precedings=driver.find_elements(By.XPATH,"//a[contains(text(),'Raymond Lifestyle L')]/ancestor::tr/preceding::*")
print("Number of preceding nodes:",len(precedings)) #301

#preceding-sibling
precedingsiblings=driver.find_elements(By.XPATH,"//a[contains(text(),'Raymond Lifestyle L')]/ancestor::tr/preceding-sibling::tr")
print("Number of preceding-sibling nodes:",len(precedingsiblings)) #10
#
driver.close()


from selenium import webdriver
import getpass
import os, time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver

def WebElement_click(self):
    self._parent.execute_script("arguments[0].click();", self)
WebElement.click = WebElement_click

def WebDriver_find_element_by_xpath(self, x):
  x = WebDriverWait(self, 10).until(
        EC.presence_of_element_located((By.XPATH, x))
    )
  return x
WebDriver.find_element_by_xpath = WebDriver_find_element_by_xpath

os.system('cls' if os.name == 'nt' else 'clear')
print("#######               ######                  ")
print("   #      ##   #####  #     # # #####  ###### ")
print("   #     #  #  #    # #     # # #    # #      ")
print("   #    #    # #    # ######  # #    # #####  ")
print("   #    ###### #####  #   #   # #    # #      ")
print("   #    #    # #      #    #  # #    # #      ")
print("   #    #    # #      #     # # #####  ######\n ")

chromedriver = "<INSERT PATH TO CHROMEDRIVER EXECUTABLE>"
os.environ["webdriver.chrome.driver"] = chromedriver
chrome_options = Options()  
chrome_options.add_argument("--headless")  
chrome_options.binary_location = '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'
driver = webdriver.Chrome(chromedriver, chrome_options=chrome_options)

word = getpass.getpass("UMICH Password:")
pickup_addr = input("\nWhat is your pickup location?\n")
dropoff_addr = input("\nWhat is your dropoff location?\n")

for i in range(3):
  try:
    driver.get("https://tapride-umich.herokuapp.com/ride/")

    login = driver.find_element_by_xpath('//*[@id="ride-wrapper"]/div[8]/div/div[1]/div/button')
    login.click()

    login = driver.find_element_by_xpath('/html/body/a')
    login.click()

    user = driver.find_element_by_xpath('//*[@id="login"]')
    user.send_keys("<CHANGE TO UNIQNAME>")
    passw = driver.find_element_by_xpath('//*[@id="password"]') 
    passw.send_keys(word)
    submit = driver.find_element_by_xpath('//*[@id="loginSubmit"]')
    submit.click()
    time.sleep(1)
    request = driver.find_element_by_xpath('//button[text()="REQUEST RIDE"]')
    request.click() 


    pickup = driver.find_element_by_xpath('//*[@id="pickup-location-input"]')
    pickup.send_keys(pickup_addr)
    choice = driver.find_element_by_xpath('/html/body/div[3]/div[2]/ul/li[1]/span')
    choice.click()

    dropoff = driver.find_element_by_xpath('//*[@id="dropoff-location-input"]')
    dropoff.send_keys(dropoff_addr)
    time.sleep(1)
    choice = driver.find_element_by_xpath('/html/body/div[3]/div[2]/ul/li[1]/span')
    choice.click()

    order = driver.find_element_by_xpath('//*[@id="ride-wrapper"]/div[8]/div/div[6]/div[2]/button')
    order.click()
    order = driver.find_element_by_xpath('//*[@id="ride-wrapper"]/div[9]/div/div[7]/div[2]/button')
    print("\n"+order.text+" DONE") 
    order.click()
    driver.quit()
    break
  except:
    print("\nHold up retrying..")
    driver.quit()
    driver = webdriver.Chrome(chromedriver, chrome_options=chrome_options)





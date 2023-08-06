from selenium import webdriver
from selenium.webdriver.common.by import By
import string
import random
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

N = 7

res = ''.join(random.choices(string.ascii_lowercase + 'a', k=N))
letters = string.ascii_lowercase


options = FirefoxOptions();driver=webdriver.Firefox();a=ActionChains(driver);
driver.get('https://mail.tm/en/')
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="accounts-menu"]').click()
time.sleep(5)
email = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[2]/div[4]/div[3]/div/div[1]/p[2]').text
print(email)
window_before = driver.window_handles[0]

driver.execute_script("window.open('about:blank','secondtab');")
driver.switch_to.window("secondtab")

driver.get('https://www.wekeo.eu/register')
time.sleep(10)
driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/form/div[1]/div[1]/div[1]/div').click()

a.send_keys(email).perform()
userName = (''.join(random.choice(letters) for i in range(10)))
a.send_keys(Keys.TAB).perform()
a.send_keys(userName).perform()
password = '@Richa12345'

a.send_keys(Keys.TAB).perform()
a.send_keys(password).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.ARROW_DOWN).perform()
a.send_keys(Keys.ENTER).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.ARROW_DOWN).perform()
a.send_keys(Keys.ENTER).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.SPACE).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.SPACE).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.ENTER).perform()

time.sleep(10)
driver.switch_to.window(window_before)
driver.refresh()
time.sleep(5)
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div[2]/ul/li/a').click()

time.sleep(10)

for x in range(1, 41):
    a.send_keys(Keys.TAB).perform()

time.sleep(2)
partial_href = "identity.apps.mercator.dpi.wekeo.eu/accountrecoveryendpoint/confirmregistration.do"
iframe = driver.find_element(By.XPATH, '//*[@id="iFrameResizer0"]')
driver.switch_to.frame(iframe)
matching_a_element = driver.find_element(By.XPATH, f'//a[contains(@href, "{partial_href}")]')
matching_href = matching_a_element.get_attribute("href")
driver.switch_to.window("secondtab")
driver.get(matching_href)
time.sleep(10)
driver.get('https://www.wekeo.eu/register')
time.sleep(5)
driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/form/div[2]/span').click()
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="usernameUserInput"]')
a.send_keys(userName).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(password).perform()
a.send_keys(Keys.ENTER).perform()
time.sleep(10)
driver.get('https://jupyterhub-wekeo.apps.eumetsat.dpi.wekeo.eu')
time.sleep(5)
driver.switch_to.window(window_before)
driver.get('https://mail.tm/en/')
time.sleep(5)
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div[2]/ul/li[1]/a').click()
time.sleep(5)
iframe = driver.find_element(By.XPATH, '//*[@id="iFrameResizer0"]')
driver.switch_to.frame(iframe)
time.sleep(5)
try:
    val = driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td/table/tbody/tr[3]/td/p[2]/b').text
    print(val)
except:
    print('not found')

driver.switch_to.window("secondtab")
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="OTPCode"]').click()
a.send_keys(val).perform()
a.send_keys(Keys.ENTER).perform()

time.sleep(10)
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/div[2]').click()
time.sleep(120)
driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[1]/div[3]/div[3]/div[3]/div/div/div[4]/div[2]/div[1]').click()
time.sleep(20)
a.send_keys(Keys.ENTER).perform()
time.sleep(864000)

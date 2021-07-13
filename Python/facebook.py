from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

email = "*********"
morsecode = "**********"
driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()

email_id = driver.find_element_by_xpath("//input[@class='inputtext _55r1 _6luy']").send_keys(email)
time.sleep(2)

passw = driver.find_element_by_xpath("//input[@class='inputtext _55r1 _6luy _9npi']").send_keys(morsecode)
time.sleep(2)

login_click = driver.find_element_by_xpath("//button[@class='_42ft _4jy0 _6lth _4jy6 _4jy1 selected _51sy']")

login_click.click()

search = driver.find_element_by_xpath("//input[@placeholder='Search Facebook']").send_keys("aaditya mul")
time.sleep(5)

search_click = driver.find_element_by_xpath("//a[@href='https://www.facebook.com/aaditya.muleva']").click()
time.sleep(5)

msg = driver.find_element_by_xpath("//div[@aria-label='Message']").click()
time.sleep(3)

messaging = driver.find_element_by_xpath("//div[@class='orhb3f3m h905i5nu jinzq4gt emzo65vh j83agx80 e5nlhep0 mrt03zmi ecm0bbzt h4z51re5 gvyehdmr mu0vl6fp msuhji6j iqy7zqfr rj1gh0hx cbu4d94t buofh1pr ni8dbmo4 ll8tlv6m b3i9ofy5 oo9gr5id flx89l3n dpja2al7 hedjyaoh']/../div[@class='orhb3f3m h905i5nu jinzq4gt emzo65vh j83agx80 e5nlhep0 mrt03zmi ecm0bbzt h4z51re5 gvyehdmr mu0vl6fp msuhji6j iqy7zqfr rj1gh0hx cbu4d94t buofh1pr ni8dbmo4 ll8tlv6m b3i9ofy5 oo9gr5id flx89l3n dpja2al7 hedjyaoh']").send_keys("testing..testing..123")


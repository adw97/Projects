from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
input("please scan qr code then enter any key:")
Am = driver.find_element_by_css_selector("span[title='Aaditya Muleva']")
Am.click()
testinput =driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]")
for i in range(3):
     testinput.send_keys("hello bhai")
     testinput.send_keys(Keys.RETURN)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



driver = webdriver.Chrome(executable_path="C:\Intel\chromedriver.exe")
driver.get("https://www.tasvir.pk/")
print(driver.title)
links = driver.find_elements(By.TAG_NAME,"a")
print("Number of links present:", len(links))
for links in links:
    print(links.text)
#Clicking on links
driver.find_element(By.LINK_TEXT,"START FRAMING").click()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(executable_path="C:\Intel\chromedriver.exe")
driver.maximize_window()
driver.get("https://tasvir.pk/review")

print(driver.title)
#FIRST IMAGE
driver.find_element_by_id("image").send_keys("C://Users/Abuzar/OneDrive/Desktop/Wallpapers/938229.png")
driver.find_element_by_xpath("//*[@id='crop']").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='selectframe']/div/div/div[1]/div[2]/div[1]/img").click()
time.sleep(3)
#SECOND IMAGE
driver.find_element_by_id("images").send_keys("C://Users/Abuzar/OneDrive/Desktop/Wallpapers/608335.jpg")
driver.find_element_by_xpath("//*[@id='crop']").click()
time.sleep(5)
#THIRD IMAGE
driver.find_element_by_id("images").send_keys("C://Users/Abuzar/OneDrive/Desktop/Wallpapers/985999.png")
driver.find_element_by_xpath("//*[@id='crop']").click()
time.sleep(5)
#FOURTH IMAGE
driver.find_element_by_id("images").send_keys("C://Users/Abuzar/OneDrive/Desktop/Wallpapers/986230.png")
driver.find_element_by_xpath("//*[@id='crop']").click()
time.sleep(5)
#FIFTH IMAGE
driver.find_element_by_id("images").send_keys("C://Users/Abuzar/OneDrive/Desktop/Wallpapers/715918.jpg")
driver.find_element_by_xpath("//*[@id='crop']").click()
time.sleep(5)
#SIXTH IMAGE
driver.find_element_by_id("images").send_keys("C://Users/Abuzar/OneDrive/Desktop/Wallpapers/938229.png")
driver.find_element_by_xpath("//*[@id='crop']").click()
time.sleep(5)
#SEVENTH IMAGE
driver.find_element_by_id("images").send_keys("C://Users/Abuzar/OneDrive/Desktop/Wallpapers/938229.png")
driver.find_element_by_xpath("//*[@id='crop']").click()
time.sleep(5)
#EIGHTH IMAGE
driver.find_element_by_id("images").send_keys("C://Users/Abuzar/OneDrive/Desktop/Wallpapers/938229.png")
driver.find_element_by_id("crop").click()
driver.find_element_by_xpath("//*[@id='next_page_frame_btn']")
#driver.find_element_by_xpath("//*[@id='next_page_frame_btn']").click()

#driver.find_element(By.LINK_TEXT,"Upload Photo").click()
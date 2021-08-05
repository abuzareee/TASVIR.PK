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
time.sleep(2)
driver.find_element_by_xpath("//*[@id='crop']").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='selectframe']/div/div/div[1]/div[2]/div[1]/img").click()
time.sleep(3)
#SECOND IMAGE
driver.find_element_by_id("images").send_keys("C://Users/Abuzar/OneDrive/Desktop/Wallpapers/608335.jpg")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='crop']").click()
time.sleep(4)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/section/div/div/div[2]/div[1]/div[2]/div[2]/div[3]/img").click()
driver.find_element_by_xpath("//*[@id='selectframe']/div/div/div[1]/div[2]/div[1]/img").click()
time.sleep(2)
#THIRD IMAGE
driver.find_element_by_id("images").send_keys("C://Users/Abuzar/OneDrive/Desktop/Wallpapers/985999.png")
time.sleep(4)
driver.find_element_by_xpath("//*[@id='crop']").click()
time.sleep(4)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/section/div/div/div[2]/div[1]/div[3]/div[2]/div[3]/img").click()
driver.find_element_by_xpath("//*[@id='selectframe']/div/div/div[1]/div[2]/div[1]/img").click()
time.sleep(2)
#FOURTH IMAGE
driver.find_element_by_id("images").send_keys("C://Users/Abuzar/OneDrive/Desktop/Wallpapers/986230.png")
time.sleep(4)
driver.find_element_by_xpath("//*[@id='crop']").click()
time.sleep(4)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/section/div/div/div[2]/div[1]/div[4]/div[2]/div[3]/img").click()
driver.find_element_by_xpath("//*[@id='selectframe']/div/div/div[1]/div[2]/div[1]/img").click()
time.sleep(2)
#FIFTH IMAGE
driver.find_element_by_id("images").send_keys("C://Users/Abuzar/OneDrive/Desktop/Wallpapers/715918.jpg")
time.sleep(6)
driver.find_element_by_xpath("//*[@id='crop']").click()
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/section/div/div/div[2]/div[1]/div[5]/div[2]/div[3]/img").click()
driver.find_element_by_xpath("//*[@id='selectframe']/div/div/div[1]/div[2]/div[1]/img").click()
time.sleep(2)
#SIXTH IMAGE
driver.find_element_by_id("images").send_keys("C://Users/Abuzar/OneDrive/Desktop/Wallpapers/938229.png")
time.sleep(7)
driver.find_element_by_xpath("//*[@id='crop']").click()
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/section/div/div/div[2]/div[1]/div[6]/div[2]/div[3]/img").click()
driver.find_element_by_xpath("//*[@id='selectframe']/div/div/div[1]/div[2]/div[1]/img").click()
time.sleep(2)
#SEVENTH IMAGE
driver.find_element_by_id("images").send_keys("C://Users/Abuzar/OneDrive/Desktop/Wallpapers/938229.png")
time.sleep(7)
driver.find_element_by_xpath("//*[@id='crop']").click()
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/section/div/div/div[2]/div[1]/div[7]/div[2]/div[3]/img").click()
driver.find_element_by_xpath("//*[@id='selectframe']/div/div/div[1]/div[2]/div[1]/img").click()
time.sleep(2)
#EIGHTH IMAGE
driver.find_element_by_id("images").send_keys("C://Users/Abuzar/OneDrive/Desktop/Wallpapers/938229.png")
time.sleep(8)
driver.find_element_by_id("crop").click()
time.sleep(4)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/section/div/div/div[2]/div[1]/div[8]/div[2]/div[3]/img").click()
driver.find_element_by_xpath("//*[@id='selectframe']/div/div/div[1]/div[2]/div[1]/img").click()
time.sleep(2)




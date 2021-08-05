from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\Intel\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.tasvir.pk/")
print(driver.title)
driver.find_element_by_xpath("//*[@id='navbarSupportedContent-555']/ul[2]/li/a").click()
email = driver.find_element_by_name("Email")
print(email.is_displayed())
print(email.is_enabled())
password = driver.find_element_by_name("Password")
print(password.is_displayed())
print(password.is_enabled())
#radio = driver.find_element_by_css_selector("input[value=roundtrip]")
#driver.find_element_by_id("Result_Radio_Button").click()
#print("Status of radio button "radio.is_selected())

driver.find_element_by_xpath("//*[@id='login']/div/div/form/div[1]/input").send_keys("Abuzar@gmail.com")
driver.find_element_by_xpath("//*[@id='login']/div/div/form/div[2]/input").send_keys("123456")
driver.find_element_by_xpath("//*[@id='login']/div/div/form/div[4]/button").click()

#FIRST IMAGE
#driver.find_element_by_id("image").send_keys("C://Users/Abuzar/OneDrive/Desktop/Wallpapers/938229.png")
#time.sleep(2)
#driver.find_element_by_xpath("//*[@id='crop']").click()
#time.sleep(3)
#driver.find_element_by_xpath("//*[@id='selectframe']/div/div/div[1]/div[2]/div[1]/img").click()
#time.sleep(3)
#REMOVING BANNER
time.sleep(4)
driver.find_element_by_xpath("//*[@id='myModalS']/div/div/button/img").click()

#FIRST IMAGE
driver.find_element_by_id("images").send_keys("C://Users/Abuzar/OneDrive/Desktop/Wallpapers/938229.png")
time.sleep(4)
driver.find_element_by_xpath("//*[@id='crop']").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='selectframe']/div/div/div[1]/div[2]/div[1]/img").click()
time.sleep(3)
#SECOND IMAGE
driver.find_element_by_id("images").send_keys("C://Users/Abuzar/OneDrive/Desktop/Wallpapers/608335.jpg")
time.sleep(4)
driver.find_element_by_xpath("//*[@id='crop']").click()
time.sleep(4)
driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/section/div/div/div[2]/div[1]/div[2]/div[2]/div[3]/img").click()
driver.find_element_by_xpath("//*[@id='selectframe']/div/div/div[1]/div[2]/div[1]/img").click()
time.sleep(2)
#THIRD IMAGE
driver.find_element_by_id("images").send_keys("C://Users/Abuzar/OneDrive/Desktop/Wallpapers/985999.png")
time.sleep(4)
driver.find_element_by_xpath("//*[@id='crop']").click()
time.sleep(4)
driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/section/div/div/div[2]/div[1]/div[3]/div[2]/div[3]/img").click()
driver.find_element_by_xpath("//*[@id='selectframe']/div/div/div[1]/div[2]/div[1]/img").click()
time.sleep(2)
#FOURTH IMAGE
driver.find_element_by_id("images").send_keys("C://Users/Abuzar/OneDrive/Desktop/Wallpapers/986230.png")
time.sleep(4)
driver.find_element_by_xpath("//*[@id='crop']").click()
time.sleep(4)
driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/section/div/div/div[2]/div[1]/div[4]/div[2]/div[3]/img").click()
driver.find_element_by_xpath("//*[@id='selectframe']/div/div/div[1]/div[2]/div[1]/img").click()
time.sleep(2)
#FIFTH IMAGE
driver.find_element_by_id("images").send_keys("C://Users/Abuzar/OneDrive/Desktop/Wallpapers/715918.jpg")
time.sleep(6)
driver.find_element_by_xpath("//*[@id='crop']").click()
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/section/div/div/div[2]/div[1]/div[5]/div[2]/div[3]/img").click()
driver.find_element_by_xpath("//*[@id='selectframe']/div/div/div[1]/div[2]/div[1]/img").click()
time.sleep(2)
#SIXTH IMAGE
driver.find_element_by_id("images").send_keys("C://Users/Abuzar/OneDrive/Desktop/Wallpapers/938229.png")
time.sleep(7)
driver.find_element_by_xpath("//*[@id='crop']").click()
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/section/div/div/div[2]/div[1]/div[6]/div[2]/div[3]/img").click()
driver.find_element_by_xpath("//*[@id='selectframe']/div/div/div[1]/div[2]/div[1]/img").click()
time.sleep(2)
#SEVENTH IMAGE
driver.find_element_by_id("images").send_keys("C://Users/Abuzar/OneDrive/Desktop/Wallpapers/842585.jpg")
time.sleep(7)
driver.find_element_by_xpath("//*[@id='crop']").click()
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/section/div/div/div[2]/div[1]/div[7]/div[2]/div[3]/img").click()
driver.find_element_by_xpath("//*[@id='selectframe']/div/div/div[1]/div[2]/div[1]/img").click()
time.sleep(2)
#EIGHTH IMAGE
driver.find_element_by_id("images").send_keys("C://Users/Abuzar/OneDrive/Desktop/Wallpapers/595156.jpg")
time.sleep(8)
driver.find_element_by_id("crop").click()
time.sleep(4)
driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/section/div/div/div[2]/div[1]/div[8]/div[2]/div[3]/img").click()
driver.find_element_by_xpath("//*[@id='selectframe']/div/div/div[1]/div[2]/div[1]/img").click()
time.sleep(2)

driver.find_element(By.LINK_TEXT,"NEXT").click()
#COLORS
#YELLOW = //*[@id='selectframe']/div/div/div[1]/div[2]/div/div[2]/img
#PINK = //*[@id='selectframe']/div/div/div[1]/div[2]/div/div[3]/img
#RED = //*[@id='selectframe']/div/div/div[1]/div[2]/div/div[4]/img
#GREEN = //*[@id='selectframe']/div/div/div[1]/div[2]/div/div[5]/img
#BLACK = //*[@id='selectframe']/div/div/div[1]/div[2]/div/div[6]/img


#FIRST IMAGE COLOR
driver.find_element_by_xpath("//*[@id='selectframe']/div/div/div[1]/div[2]/div/div[2]/img").click()

#SECOND IMAGE COLOR
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/section/div/div/div[2]/div[1]/div[2]/div[2]/div[3]/img").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='selectframe']/div/div/div[1]/div[2]/div/div[6]/img").click()

#THIRD IMAGE COLOR
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/section/div/div/div[2]/div[1]/div[3]/div[2]/div[3]/img").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='selectframe']/div/div/div[1]/div[2]/div/div[4]/img").click()

#FOURTH IMAGE COLOR
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/section/div/div/div[2]/div[1]/div[4]/div[2]/div[3]/img").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='selectframe']/div/div/div[1]/div[2]/div/div[5]/img").click()

#FIFTH IMAGE COLOR
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/section/div/div/div[2]/div[1]/div[5]/div[2]/div[3]/img").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='selectframe']/div/div/div[1]/div[2]/div/div[3]/img").click()

#SIXTH IMAGE COLOR
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/section/div/div/div[2]/div[1]/div[6]/div[2]/div[3]/img").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='selectframe']/div/div/div[1]/div[2]/div/div[4]/img").click()

#SEVENTH IMAGE COLOR
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/section/div/div/div[2]/div[1]/div[7]/div[2]/div[3]/img").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='selectframe']/div/div/div[1]/div[2]/div/div[5]/img").click()

#EIGHTH IMAGE COLOR
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/section/div/div/div[2]/div[1]/div[8]/div[2]/div[3]/img").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='selectframe']/div/div/div[1]/div[2]/div/div[6]/img").click()
time.sleep(2)

#FINDING LINKS
links = driver.find_elements(By.TAG_NAME,"a")
print("Number of links present:", len(links))
for links in links:
    print(links.text)


#driver.find_element_by_xpath("//*[@id='selectframe']/div/div/div[1]/div[2]/div/div[4]/img").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT,"NEXT").click()

driver.find_element_by_id("submit_order_information").click()
driver.find_element_by_xpath("//*[@id='couponcode']").send_keys("AB_TEST")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='payment']/div/div/div[2]/form/div/div/a").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='payment']/div/div/div[2]/div[3]/a").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='confirmation']/div/div/div[2]/div[5]/a").click()
#driver.find_element_by_xpath("//*[@id='next_page_frame_btn']").click()
#driver.find_element_by_xpath("//*[@id='image']").click()
#driver.find_element_by_xpath("//*[@id='images']").send_keys("C:\\Users\Abuzar\OneDrive\Desktop\IMG_9037.JPG")

#driver.back()
#driver.forward()


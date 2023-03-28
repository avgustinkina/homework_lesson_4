import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0, 600);")
selenium_ruby = driver.find_element_by_id("text-22-sub_row_1-0-2-0-0").click()
reviews = driver.find_element_by_css_selector(".reviews_tab > a ").click()
star5 = driver.find_element_by_class_name("star-5").click()
review = driver.find_element_by_id("comment")
review.send_keys("Nice book!")
name = driver.find_element_by_id("author")
name.send_keys("Vika")
email = driver.find_element_by_id("email")
email.send_keys("vikacamp@gmail.com")
submit = driver.find_element_by_id("submit").click()
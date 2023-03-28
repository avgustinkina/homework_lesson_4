import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.implicitly_wait(5)
driver.maximize_window()

#регистрация аккаунта

driver.get("https://practice.automationtesting.in/")
my_accaunt_btn = driver.find_element_by_id("menu-item-50").click()
email = driver.find_element_by_id("reg_email")
email.send_keys("vikacamprg@gmail.com")
password = driver.find_element_by_id("reg_password")
password.send_keys("963shas852tun")
register_btn = driver.find_element_by_css_selector(".woocomerce-FormRow.form-row > :nth-child(3)").click()



#логин в систему

driver.get("https://practice.automationtesting.in/")
my_accaunt_btn = driver.find_element_by_id("menu-item-50").click()
email = driver.find_element_by_id("username")
email.send_keys("vikacamprg@gmail.com")
password = driver.find_element_by_id("password")
password.send_keys("963shas852tun")
login_btn = driver.find_element_by_name("login").click()
some_element= WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce > .woocommerce-MyAccount-navigation"), "Logout"))


driver.quit()

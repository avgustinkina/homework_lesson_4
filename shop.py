import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.implicitly_wait(5)
driver.maximize_window()

#отображение страницы товара

driver.get("https://practice.automationtesting.in/")
my_accaunt_btn = driver.find_element_by_id("menu-item-50").click()
username = driver.find_element_by_id("username")
username.send_keys("vikacamprg@gmail.com")
password = driver.find_element_by_id("password")
password.send_keys("963shas852tun")
login_btn = driver.find_element_by_name("login").click()
shop_btn = driver.find_element_by_id("menu-item-40").click()
html5forms_btn = driver.find_element_by_css_selector(".products.masonry-done > :nth-child(3)").click()
html5forms_element= WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.ID, "product-181"), "HTML5 Forms"))

#количество товаров в категории


my_accaunt_btn = driver.find_element_by_id("menu-item-50").click()
username = driver.find_element_by_id("username")
username.send_keys("vikacamprg@gmail.com")
password = driver.find_element_by_id("password")
password.send_keys("963shas852tun")
login_btn = driver.find_element_by_name("login").click()
shop_btn = driver.find_element_by_id("menu-item-40").click()
html_btn = driver.find_element_by_css_selector(".cat-item.cat-item-19 > a").click()
items_count = driver.find_elements_by_class_name("type-product.status-publish")
if len(items_count) == 3:
   print("На странице 3 товара")
else:
   print("Ошибка. Количество товаров на странице: " + str(len(items_count)))


#сортировка товаров



my_accaunt_btn = driver.find_element_by_id("menu-item-50").click()
username = driver.find_element_by_id("username")
username.send_keys("vikacamprg@gmail.com")
password = driver.find_element_by_id("password")
password.send_keys("963shas852tun")
login_btn = driver.find_element_by_name("login").click()
shop_btn = driver.find_element_by_id("menu-item-40").click()
status_select = driver.find_element_by_class_name("orderby")
status_select_selected = status_select.get_attribute("value")
print("value of status_select: ", status_select_selected)
if status_select_selected == "menu_order":
   print("Селектор по умолчанию")
else:
   print("Селектор не отмечен")
from selenium.webdriver.support.select import Select
element = driver.find_element_by_class_name("orderby")
select = Select(element)
select.select_by_value("price-desc")
status_select = driver.find_element_by_class_name("orderby")
status_select_selected = status_select.get_attribute("value")
print("value of status_select: ", status_select_selected)
if status_select_selected == "price-desc":
   print("Выбран верный селектор")
else:
   print("Выбран не верный селектор")


#отображение, скидка товара




my_accaunt_btn = driver.find_element_by_id("menu-item-50").click()
username = driver.find_element_by_id("username")
username.send_keys("vikacamprg@gmail.com")
password = driver.find_element_by_id("password")
password.send_keys("963shas852tun")
login_btn = driver.find_element_by_name("login").click()
shop_btn = driver.find_element_by_id("menu-item-40").click()
android_quick_start_guide = driver.find_element_by_css_selector(".products.masonry-done > :nth-child(1)").click()
old_price = driver.find_element_by_css_selector(".price > del > span")
old_price_text = old_price.text
assert old_price_text == "₹600.00"
new_price = driver.find_element_by_css_selector(".price > ins > span")
new_price_text = new_price.text
assert new_price_text == "₹450.00"
img_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "attachment-shop_single.size-shop_single")) )
img_btn.click()
close_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")) )


#проверка цены в корзине




shop_btn = driver.find_element_by_id("menu-item-40").click()
mastering_java_script = driver.find_element_by_css_selector(".products.masonry-done > :nth-child(6) > :nth-child(2)").click()
cart_contents = driver.find_element_by_css_selector(".wpmenucart-contents > span")
cart_contents_text = cart_contents.text
assert cart_contents_text == "1 item"
amount = driver.find_element_by_class_name("amount")
amount_text = amount.text
assert amount_text == "₹350.00"
shopping_cart = driver.find_element_by_id("wpmenucartli").click()
subtotal_element = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal > td > span"), "₹350.00"))
total_element= WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total > td > strong "), "357.00"))


#работа в корзине



shop_btn = driver.find_element_by_id("menu-item-40").click()
driver.execute_script("window.scrollBy(0, 300);")
mastering_java_script = driver.find_element_by_css_selector(".products.masonry-done > :nth-child(6) > :nth-child(2)").click()
time.sleep(5)
shopping_cart = driver.find_element_by_id("wpmenucartli").click()
time.sleep(5)
remove_btn = driver.find_element_by_class_name("remove").click()
undo_btn = driver.find_element_by_link_text("Undo?").click()
quantity = driver.find_element_by_class_name("input-text.qty.text")
quantity.clear()
quantity.send_keys(3)
update_bascet = driver.find_element_by_css_selector(".actions > .button").click()
time.sleep(5)
quantity2 = driver.find_element_by_css_selector(".product-quantity > .quantity")
quantity2_check = quantity2.get_attribute("value")
assert quantity2_check == "3"
time.sleep(3)
apply_coupon_btn = driver.find_element_by_name("apply_coupon").click()
message = driver.find_element_by_css_selector(".woocommerce-error > li")
message_text = message.text
assert message_text == "Please enter a coupon code."



#покупка товара


shop_btn = driver.find_element_by_id("menu-item-40").click()
driver.execute_script("window.scrollBy(0, 300);")
mastering_java_script = driver.find_element_by_css_selector(".products.masonry-done > :nth-child(6) > :nth-child(2)").click()
time.sleep(5)
shopping_cart = driver.find_element_by_id("wpmenucartli").click()
proceed_to_checkout_btn = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button")) )
proceed_to_checkout_btn.click()
first_name = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, "billing_first_name")) )
first_name.send_keys("Vika")
last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys("Ivanova")
email = driver.find_element_by_id("billing_email")
email.send_keys("vikacamp@gmail.com")
phone = driver.find_element_by_id("billing_phone")
phone.send_keys("89856412463")
country = driver.find_element_by_class_name("select2-arrow").click()
country_2 = driver.find_element_by_id("s2id_autogen1_search")
country_2.send_keys("Russia")
country_3 = driver.find_element_by_class_name("select2-result-label").click()
addres = driver.find_element_by_id("billing_address_1")
addres.send_keys("Pushkina")
city = driver.find_element_by_id("billing_city")
city.send_keys("Moscow")
state_country = driver.find_element_by_id("billing_state")
state_country.send_keys("Russia")
postcode = driver.find_element_by_id("billing_postcode")
postcode.send_keys("123654")
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)
payments = driver.find_element_by_id("payment_method_cheque").click()
place_order = driver.find_element_by_id("place_order").click()
text_element= WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".page-content.entry-content > .woocommerce"), "Thank you. Your order has been received."))
payment_method = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".shop_table.order_details > tfoot > :nth-child(3)"), "Check Payments"))



driver.quit()

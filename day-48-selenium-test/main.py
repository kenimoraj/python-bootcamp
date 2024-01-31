from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options)


#Python.org

# driver.get("https://python.org/")
# li_css_sel = "div.event-widget div.shrubbery ul.menu li"
# time_tags = driver.find_elements(By.CSS_SELECTOR, f"{li_css_sel} time")
# event_tags = driver.find_elements(By.CSS_SELECTOR, f"{li_css_sel} a")
#
# dictionary = {}
# for i in range(len(event_tags)):
#     time = time_tags[i].get_attribute(name="datetime").split("T")[0]
#     name = event_tags[i].text
#
#     dictionary[i] = {time: name}
#
# print(dictionary)

#Wikipedia
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# count_elem = driver.find_element(By.CSS_SELECTOR, "div#articlecount a")
# count = count_elem.text
# print(count)

#Signup
# driver.get("https://secure-retreat-92358.herokuapp.com/")
# inputs = driver.find_elements(By.CSS_SELECTOR, value=".form-control")
# for input in inputs:
#     input.send_keys("werwer")
# input.send_keys("@sdfsdf.com")
# btn = driver.find_element(By.TAG_NAME, "button")
# btn.click()

#Cookie clicker
NAMES = ["million", "billion", "trillion", "quadrillion", "quintillion", "sextillion", "septillion",
             "octillion", "nonillion", "decillion", "undecillion", "duodecillion", "tredecillion", "quattuordecillion"]
def get_cookie_count(count_str):



    if count_str.__contains__("illion"):
        tokens = count_str.split(" ")[0].split("\n")
        number = tokens[0]
        qual = tokens[1]
        result = float(number)*1000
        for i in range(NAMES.index(qual)+1):
            result *= 1000

    else:
        result = count_str.split(" ")[0].replace(",","")

    return int(result)

def get_price(price_str):
    tokens = price_str.split(" ")
    number = tokens[0]
    if len(tokens) > 1:
        qual = tokens[1]
        result = float(number)*1000
        for i in range(NAMES.index(qual)+1):
            result *= 1000
    else:
        result = number.replace(",", "")
    return int(result)

save = "Mi4wNTJ8fDE3MDYxODgyMjA1Njg7MTcwNjE4ODIyMDU2ODsxNzA2MjI3NTE5MzI0O1NwYWNlIE1lYXRiYWxsO3R3cXl2OzAsMSwwLDAsMCwwLDB8MTExMTExMDExMDAxMDExMDAxMDEwMTEwMDAxfDIzMzQ1OTUzMi44MzM4OTkxNDs0MTQxMjgwNDM2LjgyMDE5OTsyNTYwNTY7MTs0MDQ4Njc5MzIuOTAxNzM1Nzs4MjswOzA7MDswOzA7MDswOzA7MDsxOzA7MDswOzA7MDswOzswOzA7MDswOzA7MDswOy0xOy0xOy0xOy0xOy0xOzA7MDswOzA7NzU7MDswOzA7MDsxNzA2MjE3MzU2MTg1OzA7MTs7NDE7MDswOzU3NjI4OC44MDY5OTM0MzEyOzUwOzA7MDt8MTAxLDEwMSw0NTU3NzYwMywwLCwwLDEwMTs4OCw4OCwzNTIxNTMxMSwwLCwwLDg4OzcxLDcxLDM1MjMxNjM3LDAsLDAsNzE7NTUsNTUsMTE0MzkxNDkyLDAsLDAsNTU7MzgsMzgsMjUwNzQ5NTUzLDAsLDAsMzg7MjcsMjcsNTgzOTU4MzI0LDAsLDAsMjc7MTUsMTUsMTQxNDEyNjU0OCwwLCwwLDE1OzQsNCwxMjU3MTYyMDI0LDAsLDAsNDswLDAsMCwwLCwwLDA7MCwwLDAsMCwsMCwwOzAsMCwwLDAsLDAsMDswLDAsMCwwLCwwLDA7MCwwLDAsMCwsMCwwOzAsMCwwLDAsLDAsMDswLDAsMCwwLCwwLDA7MCwwLDAsMCwsMCwwOzAsMCwwLDAsLDAsMDswLDAsMCwwLCwwLDA7MCwwLDAsMCwsMCwwOzAsMCwwLDAsLDAsMDt8MTExMTExMTExMTEwMDAxMTExMTExMTExMTExMTExMTAxMTExMTEwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAxMTEwMTExMTExMTExMDEwMTAxMDEwMTAwMDExMTAwMDEwMDAwMDAwMDAwMDAwMDAwMDAwMTExMTExMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMTExMTEwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAxMTEwMTAwMDAwMDAxMDEwMDAwMDAwMDAxMDAwMDAwMDAwMDAxMDEwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAxMDEwMTAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAxMDEwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMHwxMTExMTEwMDAwMDAwMDAwMTExMTEwMDAwMDAwMDAxMTEwMTExMTAwMTEwMTEwMTAwMTEwMDAwMDAwMDAwMDAwMDAwMTAwMDExMDEwMDAwMDAwMDAwMDAwMDAwMDEwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAxMDAwMDEwMDAwMTAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwfHw%3D%21END%21%21END%21%3D%21END%21%3D%3D%21END%21"

driver.get("https://orteil.dashnet.org/cookieclicker/")


time.sleep(2)
consent = driver.find_element(By.CSS_SELECTOR, "button.fc-cta-consent")
consent.click()
time.sleep(2)
lang = driver.find_element(By.CSS_SELECTOR, ".langSelectButton")
lang.click()

time.sleep(2)

#load save
options = driver.find_element(By.CSS_SELECTOR, "div#prefsButton.panelButton")
options.click()
import_save = driver.find_element(By.LINK_TEXT, "Import save")
import_save.click()

text_area = driver.find_element(By.CSS_SELECTOR, "div#promptContentImportSave textarea")
text_area.send_keys(save, Keys.ENTER)

close_options = driver.find_element(By.CSS_SELECTOR, "div#menu div.close.menuClose")
close_options.click()
#Play
cookie = driver.find_element(By.CSS_SELECTOR, "button#bigCookie")

try:

    while True:
        timeout = time.time()+5
        while time.time() < timeout:
            cookie.click()

        products = driver.find_elements(By.CSS_SELECTOR, ".storeSection div.product.unlocked.enabled")

        for product in products:
            products = [u for u in products if u is not None]
            # cookie_count = int(driver.find_element(By.CSS_SELECTOR, "div#cookies").text.split(" ")[0].split('\n')[0].replace(",","").replace(".", ""))

            cookie_count = get_cookie_count(driver.find_element(By.CSS_SELECTOR, "div#cookies").text)
            for product in products[::-1]:
                print(product.text)
                price_str = product.text.split('\n')[1]
                price = get_price(price_str)

                while price < cookie_count:
                    product.click()
                    cookie_count -= price

        timeout = time.time() + 5
        while time.time() < timeout:
            cookie.click()

        upgrades = driver.find_elements(By.CSS_SELECTOR, "div#upgrades div")
        for upgrade in upgrades[:5]:
            upgrade.click()
except KeyboardInterrupt:
    pass




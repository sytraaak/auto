from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import csv

PATH = "C:\Program Files (x86)\chromedriver.exe"
s = Service(PATH)
driver = webdriver.Chrome(service=s) #nastavení jaký prohlížeč budeme používat

def css(css_path, text):
    element = driver.find_element(By.CSS_SELECTOR, css_path.replace(" ", "."))
    element.send_keys(str(text))

def search_name(name_path, text):
    element = driver.find_element(By.NAME, name_path)
    element.send_keys(str(text))

def css_click(css_path):
    driver.find_element(By.CSS_SELECTOR, css_path.replace(" ", ".")).click()

def wait(time):
    driver.implicitly_wait(time)

#exe
# driver.get("https://letenky.cz")
driver.get("https://dpl-dev-ares-qa.sa.cz/booking/?id_dealer=4247")
driver.maximize_window()

departure = driver.find_element(By.ID, "departure_destination_1")
destination = driver.find_element(By.ID, "arrival_destination_1")
dep_date = driver.find_element(By.ID, "date_picker_1")
ret_date = driver.find_element(By.ID, "date_picker_2")

#strana vyhledávání
departure.clear()
departure.send_keys("PRG")
destination.send_keys("LON" + Keys.RETURN)

#odmítnutí cookies
wait(5)
refuse = driver.find_element(By.CLASS_NAME, "cc-nb-reject")
refuse.click()

#čekání na výsledky
wait(30)

#vyhledávání na stránce první nabídky
offer = driver.find_element(By.CSS_SELECTOR, "a.text-center.tariff-btn.big-btn.smaller.p-3.p-md-0.justify-content-center")
first_offer = offer.get_attribute("id")

driver.find_element(By.ID, first_offer).click() #kliknutí na první nabídku

wait(10)

css_click("div.form-check.small") #vyhledání pan
css("input.form-control.foxentry-init.foxentry-input.foxentry-input-name.foxentry-input-name-name", "Jan") #křestní jméno
css("input.form-control.foxentry-init.foxentry-input.foxentry-input-name.foxentry-input-name-surname", "Burda") #příjmení
css("input.form-control.date-day", "31") #věk
css("select.form-control.form-select.date-month", "k") #měsíc
css("input.form-control date-year", "1990")
search_name("invoice:street", "Nám svobody")
search_name("invoice:houseNumber", "17")
search_name("invoice:city", "Brno")
search_name("invoice:zip", "60200")
css("input.form-control foxentry-init foxentry-input foxentry-input-phone foxentry-input-phone-phoneNumber", "702065657")
css("input.form-control foxentry-init foxentry-input foxentry-input-email foxentry-input-email-email", "mail@gmail.com")
price_1 = driver.find_elements(By.CSS_SELECTOR, "strong.d-inline-block")[1].text

css_click("div.next-arrow mb-1 ml-2 float-right white-arrow-right")

#finální stránka
ancilaries = driver.find_elements(By.CSS_SELECTOR, "label.form-check-label checkbox-custom-label round d-flex".replace(" ", "."))
ancilaries[0].click()
ancilaries[2].click()
css("input.form-control mr-2", "Putin je píča")
css_click("button.btn btn-info btn-sm px-4 py-2 discount-btn")
css_click("div.custom-checkbox")

price_2 = driver.find_elements(By.CSS_SELECTOR, "strong.d-inline-block")[2].text

print(f"Cena před: {price_1}\nCena po: {price_2}")









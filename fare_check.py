from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from send_text import send_sms
import time


PATH = "/usr/local/bin/chromedriver"
URL = "https://www.uber.com/global/en/price-estimate/"
PICKUP = "Hartsfield-Jackson Atlanta International Airport (ATL), 6000 N Terminal Pkwy Ste 4000, Atlanta"
DROPOFF = "Midtown Atlanta, Atlanta, GA"

def main():

    price = get_price()
    send_sms(price)
    time.sleep(2)





def get_price():
    global PATH, URL, PICKUP, DROPOFF

    driver = webdriver.Chrome(service=Service(PATH))

    driver.get(URL)

    try:
        pickup_location = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "pickup"))
        )
    except:
        driver.quit()

    time.sleep(1)

    body = driver.find_element(By.TAG_NAME, "body")

    pickup_location = driver.find_element(By.NAME, "pickup")
    pickup_location.send_keys(PICKUP)
    time.sleep(3)
    body.send_keys(Keys.RETURN)
    destination = driver.find_element(By.NAME, "destination").send_keys(DROPOFF)
    time.sleep(3)
    body.send_keys(Keys.RETURN)


    time.sleep(4)

    price1 = str(driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/main/section[1]/div/div[2]/div/div/div[1]/div/div[3]/div[2]/div[1]/div[1]/div/span").text)
    price1 = float(price1.replace("$", ""))

    price2 = str(driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/main/section[1]/div/div[2]/div/div/div[1]/div/div[3]/div[2]/div[2]/div[1]/div/span").text)
    price2 = float(price2.replace("$", ""))
    
    price3 = str(driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/main/section[1]/div/div[2]/div/div/div[1]/div/div[3]/div[2]/div[3]/div[1]/div/span").text)
    price3 = float(price3.replace("$", ""))

    driver.close()

    return min(price1, price2, price3)

if __name__ == "__main__":
    main()

    
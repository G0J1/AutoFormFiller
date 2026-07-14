from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import random




maxIterations = int(input("Enter the numbers of times you want this to loop: "))
iterations = 0

driver = webdriver.Chrome()
driver.get("https://g0j1.github.io/AutoFormFiller/")
driver.set_page_load_timeout(5)
wait = WebDriverWait(driver, 5)


while maxIterations > 0:
    try:
        iterations += 1
        print("Iterations: "+ str(iterations))

        time.sleep(1)

        name_input = wait.until(
            EC.presence_of_element_located((By.ID, "nameField"))
        )

        name_input.send_keys("Kiryu Kazuma")



        phone_input = wait.until(
            EC.presence_of_element_located((By.ID, "phoneField"))
        )

        phone_input.send_keys("8675309")



        email_input = wait.until(
            EC.presence_of_element_located((By.ID, "emailField"))
        )

        email_input.send_keys("kiryukazuma@fakemail.com")

        submit_btn = wait.until(
            EC.presence_of_element_located((By.ID, "submitButton"))
        )

        driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            submit_btn
        )

        wait.until(lambda d: submit_btn.is_displayed() and submit_btn.is_enabled())

        driver.execute_script("arguments[0].click();", submit_btn)

        delay = random.randint(10, 20)
        print("delay: " + str(delay))
        time.sleep(delay)

        maxIterations -= 1
        driver.get("https://g0j1.github.io/AutoFormFiller/")

    except Exception as e:
        print("page failed", e)
        driver.refresh()


import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C://Users/eduardo.cafiero/Downloads/Python_udemy_course/chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(executable_path=chrome_driver_path), options=options)

driver.get("https://www.linkedin.com/jobs/view/3616837475/?eBP=JOBS_BLENDING_SERVICE_FAILED&refId=%2FONP8ogLDuvWJ5LtUKk0%2Bg%3D%3D&trackingId=82U%2BoxM7oSHGwmiLpz5NFQ%3D%3D&trk=flagship3_search_srp_jobs")

apply_button = driver.find_element(By.XPATH, value='//*[@id="main-content"]/section[1]/div/section[2]/div/div[1]/div/div/button[1]')
apply_button.click()

email = driver.find_element(By.NAME, "email-address")
password = driver.find_element(By.NAME, "password")

email.send_keys("skyflye@inwind.it")
password.send_keys("xxxxxx")

agree_and_join = driver.find_element(By.ID, value="join-form-submit")
agree_and_join.click()

driver.find_element(By.NAME, "first-name").send_keys("Eduardo")
driver.find_element(By.NAME, "last-name").send_keys("Cafiero")
agree_and_join.click()

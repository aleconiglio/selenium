from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://katalon-demo-cura.herokuapp.com/")
driver.find_element(By.ID, "btn-make-appointment").click()
driver.find_element(By.XPATH, "//*[@id='login']/div/div/div[1]/h2")
driver.find_element(By.ID, "txt-username").send_keys("John Doe")
driver.find_element(By.ID, "txt-password").send_keys("ThisIsNotAPassword")
driver.find_element(By.ID, "btn-login").click()
driver.find_element(By.XPATH, "//*[@id='combo_facility']/option[2]").click()
driver.find_element(By.ID, "chk_hospotal_readmission").click()
driver.find_element(By.ID, "radio_program_medicaid").click()
driver.find_element(By.ID, "txt_visit_date").send_keys("13/02/2024")
driver.find_element(By.ID, "txt_comment").send_keys("I want to make an appointment")
driver.find_element(By.ID, "btn-book-appointment").click()
if len(driver.find_elements(By.XPATH, '//*[@id="summary"]/div/div/div[1]/h2'))>0:
    print("SUCCESS")
else: print("FAILED")

time.sleep(2)

driver.close()
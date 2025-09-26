from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demoqa.com/text-box")

driver.find_element(By.ID, "userName").send_keys("Jean")
driver.find_element(By.ID, "userEmail").send_keys("hracime@gmail.com")
driver.find_element(By.ID, "currentAddress").send_keys("une adresse quoi")
driver.find_element(By.ID, "permanentAddress").send_keys("une adresse quoi")

submit_button = driver.find_element(By.ID, "submit")
driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)

WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "submit"))).click()

nom = driver.find_element(By.ID, "name").text
print("Nom écrit dans le textfield Full  Name :", nom)

mail = driver.find_element(By.ID, "email").text
print("mail écrit dans le textfield Email:", mail)

cadress = driver.find_element(By.CSS_SELECTOR, "p#currentAddress").text
print("adresse écrit dans le textfield Current Address :", cadress)

padress = driver.find_element(By.CSS_SELECTOR, "p#permanentAddress").text
print("adresse écrit dans le textfield Permanenet Address :", padress)

# Fermer le navigateur
driver.quit()
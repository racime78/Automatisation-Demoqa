from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Lancer le navigateur
driver = webdriver.Chrome()
driver.maximize_window()

# Accéder au formulaire
driver.get("https://demoqa.com/checkbox")

# cocher la checkbox
checkbox = driver.find_element(By.ID, "hobbies-checkbox-1")
checkbox.click()


# Faire défiler jusqu'au bouton "Submit"
submit_button = driver.find_element(By.ID, "submit")
driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)

# Attendre que le bouton soit cliquable et cliquer
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "submit"))).click()

# Fermer le navigateur
driver.quit()
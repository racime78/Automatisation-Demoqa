from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

# Lancer le navigateur
driver = webdriver.Chrome()
driver.maximize_window()

# Accéder à la page
driver.get("https://demoqa.com/buttons")

# Trouver le bouton double clic
doubleclique = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "doubleClickBtn")))

# Scroll vers le bouton si nécessaire
driver.execute_script("arguments[0].scrollIntoView(true);", doubleclique)

# Initialiser ActionChains une seule fois
actions = ActionChains(driver)

# Double clic
actions.double_click(doubleclique).perform()

# Attendre que le message apparaisse
messagedbclique = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "doubleClickMessage"))).text

print("Message affiché après double clic :", messagedbclique)


# Attendre que le bouton soit cliquable
cliquedroit = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "rightClickBtn")))

# Scroll vers le bouton si nécessaire
driver.execute_script("arguments[0].scrollIntoView(true);", cliquedroit)

# Effectuer un clic droit avec ActionChains
actions.context_click(cliquedroit).perform()

# Attendre que le message apparaisse
messagecliquedroit = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "rightClickMessage"))).text
print("Message affiché après clic droit :", messagecliquedroit)

# Fermer le navigateur
driver.quit()
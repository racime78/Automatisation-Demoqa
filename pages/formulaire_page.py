from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormulairePage:
    def __init__(self, driver):
        self.driver = driver

    def ouvrir(self):
        self.driver.get("https://demoqa.com/automation-practice-form")

    def remplir_formulaire(self, prenom, nom, email, genre, telephone):
        self.driver.find_element(By.ID, "firstName").send_keys(prenom)
        self.driver.find_element(By.ID, "lastName").send_keys(nom)
        self.driver.find_element(By.ID, "userEmail").send_keys(email)
        self.driver.find_element(By.XPATH, f"//label[text()='{genre}']").click()
        self.driver.find_element(By.ID, "userNumber").send_keys(telephone)

    def soumettre(self):
        bouton = self.driver.find_element(By.ID, "submit")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", bouton)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, "submit"))).click()

    def get_confirmation(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg"))
        ).text

    def fermer_modal(self):
        bouton = self.driver.find_element(By.ID, "closeLargeModal")
        self.driver.execute_script("arguments[0].click();", bouton)

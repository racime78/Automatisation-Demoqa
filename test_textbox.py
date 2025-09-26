import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_textbox(driver):
    driver.get("https://demoqa.com/text-box")
    driver.find_element(By.ID, "userName").send_keys("Jean")
    driver.find_element(By.ID, "userEmail").send_keys("hracime@gmail.com")
    driver.find_element(By.ID, "currentAddress").send_keys("une adresse quoi")
    driver.find_element(By.ID, "permanentAddress").send_keys("une adresse quoi")
    submit_button = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "submit"))).click()

    confirmation = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID,"output"))).text
    #confirmation = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(name, email, currentAddress, permanentAddress))
    assert "Name:Jean" in confirmation
    assert "Email:hracime@gmail.com" in confirmation
    assert "Current Address :une adresse quoi" in confirmation
    assert "Permananet Address :une adresse quoi" in confirmation

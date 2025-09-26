import pytest
from pages.formulaire_page import FormulairePage

def test_formulaire_submission(driver):
    page = FormulairePage(driver)
    page.ouvrir()
    page.remplir_formulaire("Racime", "Houhou", "hracime@gmail.com", "Male", "0601020304")
    page.soumettre()
    assert "Thanks for submitting the form" in page.get_confirmation()
    page.fermer_modal()

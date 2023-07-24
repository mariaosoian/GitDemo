import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItems()
        log.info("getting all the card titles")
        cards = checkOutPage.getCardTitle()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkOutPage.getCardFooter()[i].click()
        checkOutPage.getCheckOutButton().click()
        time.sleep(2)
        confirmPage = checkOutPage.getCheckOutItems()
        log.info("Entering country name as ind")
        confirmPage.getInputField().send_keys("ind")
        self.verifyLinkPresence("India")
        confirmPage.getSuggestCountry().click()
        confirmPage.getCheckBox().click()
        confirmPage.getSuccessBtn().click()
        textMatch = confirmPage.getSuccessAlert().text
        log.info("Text received from application is " + textMatch)
        time.sleep(2)
        print("Maria")
        print("Maria")
        print("Maria")


        assert "Success! Thank you!" in textMatch

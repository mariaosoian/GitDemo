from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    inputField = (By.ID, "country")
    suggestCountry = (By.LINK_TEXT, "India")
    checkBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    successBtn = (By.XPATH, "//input[@class='btn btn-success btn-lg']")
    successAlert = (By.CLASS_NAME, "alert-success")
    def getInputField(self):
        return self.driver.find_element(*ConfirmPage.inputField)

    def getSuggestCountry(self):
        return self.driver.find_element(*ConfirmPage.suggestCountry)

    def getCheckBox(self):
        return self.driver.find_element(*ConfirmPage.checkBox)

    def getSuccessBtn(self):
        return self.driver.find_element(*ConfirmPage.successBtn)

    def getSuccessAlert(self):
        return self.driver.find_element(*ConfirmPage.successAlert)

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from TestData.HomePageData import HomePageData


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        homePage.getName().send_keys(getData["firstname"])
        homePage.getEmail().send_keys(getData["lastname"])
        homePage.getPasswordd().send_keys(getData["password"])
        homePage.getCheckme().click()
        self.selectOptionByText(homePage.getGender(), getData["gender"])
        homePage.getSubmitbtn().click()
        message = homePage.getSuccessmsg().text
        log.info("Verify the success message"+message)
        assert "Succekoimk" in message
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("TestCase2"))
    def getData(self, request):
        return request.param


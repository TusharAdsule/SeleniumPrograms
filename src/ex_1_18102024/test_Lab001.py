from selenium import webdriver
import allure
import pytest

@allure.title("Verify the title of web page app.vwo.com")
def test_sample():
    driver = webdriver.Chrome()
    driver.get("https://sdet.live")
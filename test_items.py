import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_exist(browser):
    browser.get(link)
    button = browser.find_element(By.XPATH, "//button[contains(@class, 'btn-add-to-basket')]")
    assert button is not None, "Button with class 'btn-add-to-basket' not found on the page"


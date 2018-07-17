from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webium import BasePage, Find


class Display(WebElement):
    display = Find(By=By.ID, value='display')


class Digits(WebElement):
    zero = Find(by=By.XPATH, value='.//li[text()="0"]')
    one = Find(by=By.XPATH, value='.//li[text()="1"]')
    two = Find(by=By.XPATH, value='.//li[text()="2"]')
    three = Find(by=By.XPATH, value='.//li[text()="3"]')
    four = Find(by=By.XPATH, value='.//li[text()="4"]')
    five = Find(by=By.XPATH, value='.//li[text()="5"]')
    six = Find(by=By.XPATH, value='.//li[text()="6"]')
    seven = Find(by=By.XPATH, value='.//li[text()="7"]')
    eight = Find(by=By.XPATH, value='.//li[text()="8"]')
    nine = Find(by=By.XPATH, value='.//li[text()="9"]')
    dot = Find(by=By.XPATH, value='.//li[text()="."]')


class Operations(WebElement):
    clear_all = Find(by=By.XPATH, value='.//li[text()="AC"]')
    clear = Find(by=By.XPATH, value='.//li[text()="C"]')
    add = Find(by=By.XPATH, value='.//li[text()="+"]')
    substract = Find(by=By.XPATH, value='.//li[text()="-"]')
    divide = Find(by=By.XPATH, value='.//li[text()="/"]')
    multiply = Find(by=By.XPATH, value='.//li[text()="x"]')
    equal = Find(by=By.XPATH, value='.//li[text()="="]')


class Calculator(BasePage):
    display = Find(Display, By.ID, 'display')
    digits = Find(Digits, By.CLASS_NAME, 'digits')
    operations = Find(Operations, By.CLASS_NAME, 'operations')

    def displays(self, expected):
        return self.display.text == expected

    def __repr__(self):
        return self.__class__.__name__

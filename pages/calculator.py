from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class Display(WebElement):
    """Display element"""
    display = (By.ID, 'display')


class Digits(WebElement):
    """Digits block"""
    zero = (By.XPATH, './/li[text()="0"]')
    one = (By.XPATH, './/li[text()="1"]')
    two = (By.XPATH, './/li[text()="2"]')
    three = (By.XPATH, './/li[text()="3"]')
    four = (By.XPATH, './/li[text()="4"]')
    five = (By.XPATH, './/li[text()="5"]')
    six = (By.XPATH, './/li[text()="6"]')
    seven = (By.XPATH, './/li[text()="7"]')
    eight = (By.XPATH, './/li[text()="8"]')
    nine = (By.XPATH, './/li[text()="9"]')
    point = (By.XPATH, './/li[text()="."]')


class Operations(WebElement):
    """Operations block"""
    clear_all = (By.XPATH, './/li[text()="AC"]')
    clear = (By.XPATH, './/li[text()="C"]')
    addition = (By.XPATH, './/li[text()="+"]')
    subtraction = (By.XPATH, './/li[text()="-"]')
    division = (By.XPATH, './/li[text()="/"]')
    multiplication = (By.XPATH, './/li[text()="x"]')
    equality = (By.XPATH, './/li[text()="="]')


class Calculator(object):
    """
    Calculator page object.

    Chars to buttons is used to input more than one char numbers.
    Each operation could apply any number of operands,
    tests are designed to use 2 only though.
    Each operation includes clear before input.
    Result function process 3 possible cases, but with variation for infinity.
    """
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://qa-test.klika-tech.com/')
        self.chars_to_buttons = {
            '0': self.driver.find_element(*Digits.zero),
            '1': self.driver.find_element(*Digits.one),
            '2': self.driver.find_element(*Digits.two),
            '3': self.driver.find_element(*Digits.three),
            '4': self.driver.find_element(*Digits.four),
            '5': self.driver.find_element(*Digits.five),
            '6': self.driver.find_element(*Digits.six),
            '7': self.driver.find_element(*Digits.seven),
            '8': self.driver.find_element(*Digits.eight),
            '9': self.driver.find_element(*Digits.nine),
            '.': self.driver.find_element(*Digits.point),
            '-': self.driver.find_element(*Operations.subtraction)
        }

    def input_number(self, value):
        for char in str(value):
            self.driver.implicitly_wait(5)
            self.chars_to_buttons[char].click()

    def clear(self):
        self.driver.find_element(*Operations.clear).click()

    def clear_all(self):
        self.driver.find_element(*Operations.clear_all).click()

    def result(self):
        self.driver.implicitly_wait(5)
        result = self.driver.find_element(*Display.display).text
        if '.' in result:
            return round(float(result), 3)
        elif result == 'Infinity' or result == '-Infinity':
            return result
        else:
            return int(result)

    def add(self, *args):
        self.clear_all()
        self.driver.implicitly_wait(5)
        for arg in args[:-1]:
            self.input_number(arg)
            self.driver.find_element(*Operations.addition).click()
        self.input_number(args[-1])
        self.driver.find_element(*Operations.equality).click()
        return self.result()

    def subtract(self, *args):
        self.clear_all()
        self.driver.implicitly_wait(5)
        for arg in args[:-1]:
            self.input_number(arg)
            self.driver.find_element(*Operations.subtraction).click()
        self.input_number(args[-1])
        self.driver.find_element(*Operations.equality).click()
        return self.result()

    def multiply(self, *args):
        self.clear_all()
        self.driver.implicitly_wait(5)
        for arg in args[:-1]:
            self.input_number(arg)
            self.driver.find_element(*Operations.multiplication).click()
        self.input_number(args[-1])
        self.driver.find_element(*Operations.equality).click()
        return self.result()

    def divide(self, *args):
        self.clear_all()
        self.driver.implicitly_wait(5)
        for arg in args[:-1]:
            self.input_number(arg)
            self.driver.find_element(*Operations.division).click()
        self.input_number(args[-1])
        self.driver.find_element(*Operations.equality).click()
        return self.result()

    def __repr__(self):
        return self.__class__.__name__

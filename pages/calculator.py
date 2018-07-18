from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class Display(WebElement):
    display = (By.ID, 'display')


class Digits(WebElement):
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
    clear_all = (By.XPATH, './/li[text()="AC"]')
    clear = (By.XPATH, './/li[text()="C"]')
    addition = (By.XPATH, './/li[text()="+"]')
    subtraction = (By.XPATH, './/li[text()="-"]')
    division = (By.XPATH, './/li[text()="/"]')
    multiplication = (By.XPATH, './/li[text()="x"]')
    equality = (By.XPATH, './/li[text()="="]')


class Calculator():
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
            self.chars_to_buttons[char].click()

    def clear(self):
        self.driver.find_element(*Operations.clear).click()

    def clear_all(self):
        self.driver.find_element(*Operations.clear_all).click()

    def add(self, *args):
        for arg in args[:-1]:
            self.input_number(arg)
            self.driver.find_element(*Operations.addition).click()
        self.input_number(args[-1])
        self.driver.find_element(*Operations.equality).click()

    def subtract(self, *args):
        for arg in args[:-1]:
            self.input_number(arg)
            self.driver.find_element(*Operations.subtraction).click()
        self.input_number(args[-1])
        self.driver.find_element(*Operations.equality).click()

    def multiply(self, *args):
        for arg in args[:-1]:
            self.input_number(arg)
            self.driver.find_element(*Operations.multiplication).click()
        self.input_number(args[-1])
        self.driver.find_element(*Operations.equality).click()

    def divide(self, *args):
        for arg in args[:-1]:
            self.input_number(arg)
            self.driver.find_element(*Operations.division).click()
        self.input_number(args[-1])
        self.driver.find_element(*Operations.equality).click()

    def is_result_match(self, expected):
        result = self.driver.find_element(*Display.display).text
        if '.' in result:
            return float(result) == expected
        elif result == 'Infinity':
            return result == expected
        else:
            return int(result) == expected

    def __repr__(self):
        return self.__class__.__name__

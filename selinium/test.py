import os
import pathlib
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


def file_url(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()


driver = webdriver.Chrome()


class TestCounter(unittest.TestCase):
    def setUp(self):
        driver.get(file_url("counter.html"))

    def test_atitle(self):
        self.assertEqual(driver.title, "Counter")

    def test_bincrease(self):
        increase = driver.find_element(By.ID, "increase")
        counter = driver.find_element(By.TAG_NAME, "h1")

        for i in range(100):
            increase.click()
            self.assertEqual(counter.text, str(i + 1))

    def test_cdecrease(self):
        decrease = driver.find_element(By.ID, "decrease")
        counter = driver.find_element(By.TAG_NAME, "h1")

        for i in range(100):
            decrease.click()
            self.assertEqual(counter.text, str(-(i + 1)))

    @classmethod
    def tearDownClass(cls):
        driver.quit()


# class TestCounter(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         driver.get(file_url("counter.html"))

#     def test_increase_then_decrease(self):
#         increase = driver.find_element(By.ID, "increase")
#         decrease = driver.find_element(By.ID, "decrease")
#         counter = driver.find_element(By.TAG_NAME, "h1")

#         # Step 1: increase 100 times
#         for i in range(100):
#             increase.click()
#             self.assertEqual(counter.text, str(i + 1))

#         # Step 2: decrease 100 times (continuing from 100)
#         for i in range(100):
#             decrease.click()
#             self.assertEqual(counter.text, str(100 - (i + 1)))

#     @classmethod
#     def tearDownClass(cls):
#         driver.quit()

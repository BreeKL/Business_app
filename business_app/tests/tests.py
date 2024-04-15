from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import unittest

# driver = webdriver.Chrome()
# driver.get("https://www.google.com/")
# driver.quit()

class HomePageTest(TestCase):
    def setUp(self):
        # Set up ChromeDriver (make sure you have downloaded ChromeDriver)
        chromedriver_path = r"C:\Users\leath\OneDrive\Documents\School\UCCS\2024 Spring\Software Development\MyProject\chromedriver-win64\chromedriver.exe"  # Adjust the path
        self.service = Service(executable_path=chromedriver_path)
        self.driver = webdriver.Chrome(service=self.service)

    def tearDown(self):
        # Clean up after the test
        self.driver.quit()

    def test_homepage_title(self):
        # Open Chrome browser and navigate to the homepage
        self.driver.get("http://127.0.0.1:8000/")  # Replace with your actual local server URL

        # Assert that the title is as expected
        expected_title = "Massage Therapy"  # Adjust as needed
        actual_title = self.driver.title
        self.assertEqual(actual_title, expected_title)

if __name__ == "__main__":
    unittest.main()
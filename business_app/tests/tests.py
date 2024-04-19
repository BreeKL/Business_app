from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest

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

class LoginTestCase(unittest.TestCase):
    def setUp(self):
        # Initialize the WebDriver (choose the appropriate browser driver)
        self.driver = webdriver.Chrome()  # Example: Chrome driver

    def tearDown(self):
        # Clean up: close the browser
        self.driver.quit()

    def test_user_login(self):
        # Navigate to the login page
        self.driver.get("http://127.0.0.1:8000/accounts/login")  # Replace with your actual login page URL

        # Find the username and password input fields
        username_input = self.driver.find_element(By.ID, "id_username")
        password_input = self.driver.find_element(By.ID, "id_password")

        # Enter valid credentials
        username_input.send_keys("your_valid_username")
        password_input.send_keys("your_valid_password")

        # Submit the form
        password_input.send_keys(Keys.RETURN)

        # Wait for redirection (you can use WebDriverWait here)
        # Example: WebDriverWait(self.driver, 10).until(lambda d: d.current_url == "http://yourwebsite.com/dashboard")

        # Verify successful login (e.g., check if user profile or dashboard page is displayed)
        self.assertIn("Massage Therapy", self.driver.title)  # Adjust based on your expected page title

if __name__ == "__main__":
    unittest.main()
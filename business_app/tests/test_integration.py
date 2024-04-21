from django.test import TestCase
from django.contrib.auth.models import User
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import time

class HomePageTest(TestCase):
    """Ensures website is active and homepage comes up"""
    def setUp(self):
        # Initialize the WebDriver 
        self.driver = webdriver.Chrome() 

    def tearDown(self):
        # Clean up after the test
        self.driver.quit()

    def test_homepage_title(self):
        # Open Chrome browser and navigate to the homepage
        self.driver.get("http://127.0.0.1:8000/") 

        # Assert that the title is as expected
        expected_title = "Massage Therapy" 
        actual_title = self.driver.title
        self.assertEqual(actual_title, expected_title)

class LoginSuccessTestCase(unittest.TestCase):
    """Ensures a correct username and password can log in"""
    def setUp(self):
        # Initialize the WebDriver 
        self.driver = webdriver.Chrome() 

    def tearDown(self):
        # Clean up: close the browser
        self.driver.quit()

    def test_user_login(self):
        # Navigate to the login page
        self.driver.get("http://127.0.0.1:8000/accounts/login")  

        # Find the username and password input fields
        username_input = self.driver.find_element(By.ID, "id_username")
        password_input = self.driver.find_element(By.ID, "id_password")

        # Enter valid credentials
        username_input.send_keys("test1")
        password_input.send_keys("CS3300SU")

        # Submit the form
        password_input.send_keys(Keys.RETURN)

        # Wait for redirection 
        # WebDriverWait(self.driver, 10).until(lambda d: d.current_url == "http://127.0.0.1:8000/accounts/login_successful")

        # Verify successful login (e.g., check if successful login page is displayed)
        self.assertIn("Login Successful", self.driver.title)  

class LoginFailTestCase(unittest.TestCase):
    """Ensures an incorrect username and password does not get logged in"""
    def setUp(self):
        # Initialize the WebDriver 
        self.driver = webdriver.Chrome() 

    def tearDown(self):
        # Clean up: close the browser
        self.driver.quit()
     
    def test_user_login(self):
        # Navigate to the login page
        self.driver.get("http://127.0.0.1:8000/accounts/login")  

        # Find the username and password input fields
        username_input = self.driver.find_element(By.ID, "id_username")
        password_input = self.driver.find_element(By.ID, "id_password")

        # Enter valid credentials
        username_input.send_keys("fake_username")
        password_input.send_keys("fake_password")

        # Submit the form
        password_input.send_keys(Keys.RETURN)

        # Wait for redirection 
        # WebDriverWait(self.driver, 10).until(lambda d: d.current_url == "http://127.0.0.1:8000/accounts/login")

        # Verify login failed (e.g., check if login page is displayed again)
        self.assertIn("Login", self.driver.title)  

class RegistrationSuccessTestCase(unittest.TestCase):
    """Ensures a new therapist can create an account"""
    def setUp(self):
        # Initialize the WebDriver 
        self.driver = webdriver.Chrome() 

    def tearDown(self):
        # Clean up: close the browser
        self.driver.quit()
        try:
            user_to_delete = User.objects.get(username='fake_username')
            user_to_delete.delete()
            print("user deleted2")
        except User.DoesNotExist:
            # Handle the case where the user doesn't exist (optional)
            print("user not deleted2")
            pass

    # test currently only working when run by itstelf, will fail when run with other tests
    # def test_user_registration(self):
    #     # Navigate to the registration page
    #     self.driver.get("http://127.0.0.1:8000/accounts/register/")  

    #     # Find the username and password input fields
    #     username_input = self.driver.find_element(By.ID, "id_username")
    #     email_input = self.driver.find_element(By.ID, "id_email")
    #     password1_input = self.driver.find_element(By.ID, "id_password1")
    #     password2_input = self.driver.find_element(By.ID, "id_password2")

    #     # Enter valid credentials
    #     username_input.send_keys("fake_username")
    #     email_input.send_keys("test@test.edu")
    #     password1_input.send_keys("HardPwd5!")
    #     password2_input.send_keys("HardPwd5!")

    #     time.sleep(2)

    #     # Submit the form
    #     password2_input.send_keys(Keys.RETURN)

    #     # Wait for redirection 
    #     time.sleep(5)

    #     # Verify registration successful (e.g., check if therapist login page is displayed)
    #     with self.subTest(msg='Registration check'):    
    #         self.assertIn("Therapist Login", self.driver.title)  

    #     # Deletes test user from database
    #     try:
    #         user_to_delete = User.objects.get(username='fake_username')
    #         user_to_delete.delete()
    #         print("user deleted1")
    #     except User.DoesNotExist:
    #         # Handle the case where the user doesn't exist (optional)
    #         print("user not deleted1")
    #         pass
        

if __name__ == "__main__":
    unittest.main()
import unittest
from selenium import webdriver
from HTMLTemplates import HTMLTemplates
from selenium.webdriver.common.by import By

class TestHTMLTemplates(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # You can use any webdriver you prefer

    def tearDown(self):
        self.driver.quit()

    def assertElementText(self, element_locator, expected_text):
        element = self.driver.find_element(*element_locator)
        self.assertEqual(expected_text, element.text)

    def test_scheduler_page(self):
        self.driver.get("data:text/html;charset=utf-8," + HTMLTemplates.scheduler_page())

        self.assertIn("Scheduler", self.driver.title)
        self.assertElementText((By.TAG_NAME, "h1"), "Scheduler")
        self.assertElementText((By.CSS_SELECTOR, "form label[for='date']"), "Select a date:")
        self.assertElementText((By.CSS_SELECTOR, "form label[for='username']"), "Assign a username:")
        self.assertElementText((By.CSS_SELECTOR, "form button[type='submit']"), "Assign Deadline")
        self.assertElementText((By.CSS_SELECTOR, "a[href='/forum']"), "Go to Forum")
        self.assertElementText((By.CSS_SELECTOR, "a[href='/logout']"), "Logout")



    def test_login_page(self):
        # Test the login page content
        self.driver.get("data:text/html;charset=utf-8," + HTMLTemplates.get_login())
        self.assertElementText((By.TAG_NAME, "h1"), "Login")
        self.assertElementText((By.CSS_SELECTOR, "form label[for='username']"), "Username:")
        self.assertElementText((By.CSS_SELECTOR, "form label[for='password']"), "Password:")
        self.assertElementText((By.CSS_SELECTOR, "form button[type='submit']"), "Login")

    def test_forum_page(self):
        # Test the forum page content
        self.driver.get("data:text/html;charset=utf-8," + HTMLTemplates.get_forum())
        self.assertElementText((By.TAG_NAME, "h1"), "Forum")
        # Add more assertions for other elements in the forum page as needed

    def test_profile_page(self):
        # Test the profile page content
        self.driver.get("data:text/html;charset=utf-8," + HTMLTemplates.get_profile())
        self.assertElementText((By.TAG_NAME, "h1"), "Welcome, {{username}}!")
        self.assertElementText((By.TAG_NAME, "p"), "This is your profile page.")
        # Add more assertions for other elements in the profile page as needed



    def test_register_page(self):
        # Test the registration page content
        self.driver.get("data:text/html;charset=utf-8," + HTMLTemplates.get_register())
        self.assertElementText((By.TAG_NAME, "h1"), "Register")
        self.assertTrue(self.driver.find_element(By.XPATH, "//form/label[contains(text(), 'Username:')]"))
        self.assertTrue(self.driver.find_element(By.XPATH, "//form/label[contains(text(), 'Password:')]"))
        self.assertTrue(self.driver.find_element(By.XPATH, "//form/button[contains(text(), 'Register')]"))


    def test_homepage(self):
        # Test the homepage content
        self.driver.get("data:text/html;charset=utf-8," + HTMLTemplates.get_homepage())
        self.assertElementText((By.TAG_NAME, "h1"), "Welcome to the Homepage")
        self.assertElementText((By.XPATH, "//p[contains(text(), 'This is the homepage')]"),
                               "This is the homepage of the website.")
        self.assertTrue(self.driver.find_element(By.XPATH, "//a[@href='/login']"))
        self.assertTrue(self.driver.find_element(By.XPATH, "//a[@href='/register']"))

    def test_change_password_page(self):
        # Test the change password page content
        self.driver.get(f"data:text/html;charset=utf-8,{HTMLTemplates.change_password_page()}")
        self.assertElementText((By.TAG_NAME, "h1"), "Change Password")
        self.assertTrue(self.driver.find_element(By.XPATH, "//label[contains(text(), 'Old Password')]"))
        self.assertTrue(self.driver.find_element(By.XPATH, "//label[contains(text(), 'New Password')]"))
        self.assertTrue(self.driver.find_element(By.XPATH, "//button[contains(text(), 'Change Password')]"))

    def test_create_team_page(self):
        # Test the create team page content
        self.driver.get(f"data:text/html;charset=utf-8,{HTMLTemplates.createTeamPage()}")
        self.assertElementText((By.TAG_NAME, "h1"), "New Team")
        self.assertTrue(self.driver.find_element(By.XPATH, "//label[contains(text(), 'Team Name:')]"))
        self.assertTrue(self.driver.find_element(By.XPATH, "//button[contains(text(), 'Create Team')]"))






if __name__ == '__main__':
    unittest.main()


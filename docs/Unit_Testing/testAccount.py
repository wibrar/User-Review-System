import unittest
from docs.TestFiles.account import Account
from docs.TestFiles.TestDatabase import Database


class TestAccount(unittest.TestCase):
    def setUp(self) :
        Database.TestDatabaseReset()  # Clears data from previous Unit Test

        # Create Account objects
        a1 = Account("Tim", "Timpassword")
        a2 = Account("Jim", "Jimpassword")
        a3 = Account("John", "Johnpassword")

        self.TestData = [("Tim", "Timpassword"), ("Jim", "Jimpassword"), ("John", "Johnpassword")]
        self.newPasswords = ["Password1", "Password2", "Password3"]
        self.Team = "TeamX"
    def tearDown(self):
        Database.TestDatabaseReset()  # Clears data from previous Unit Test

    def test_log_in_log_out(self):
        """
        The log_in function is a class method which loads the specified account
        The log_out function simply saves the change made during an account session
        :return:
        """
        for username, password in self.TestData:
            account = Account.log_in(username, password)  # Loads Account Object
            self.assertEqual(account.username, username, "Usernames should match")
            self.assertEqual(account.password, password, "Password should match")

        #  Make one change to an account and test if log_out saved account correctly
        testAcc = Account.log_in("Tim", "Timpassword")
        testAcc.joinTeam("TeamX")
        testAcc.log_out()  # Save changes to Account object
        # The test below confirms that both logout and joinTeam works as intended
        testAcc= Account.log_in("Tim", "Timpassword")  # Reload account to test for changes
        self.assertEqual(testAcc.getTeamName(), "TeamX")

        # Log in with non-existing account
        self.assertRaises(KeyError, Account.log_in, "Fake", "Account")
        # Attempts to create accounts with same username are blocked
        self.assertRaises(NameError, Account, "Tim", "Duplicate")



    def test_accessor_mutator_methods(self):
        """
        Test accessor methods get_username and get_review_history
        and mutator method get_review history, change password
        :return:
        """
        for username, password in self.TestData:
            account = Account.log_in(username, password)
            self.assertEqual(account.username, account.get_username(), "Username should match")
            account.joinTeam(self.Team)
            self.assertEqual(self.Team, account.getTeamName(), "Team name should be the same")


        account = Account.log_in("Tim", "Timpassword")
        account.change_password(self.newPasswords[0])
        self.assertEqual(account.password, self.newPasswords[0], "Passwords should match")

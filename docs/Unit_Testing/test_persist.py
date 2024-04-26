"""
Unit Test for Database Module, The main dependencies on the
database module are the account and review classes, so these
class are also imported.

Instruction: To run the unit test simply press the run button,
however subsequent runs will require the "TestDataBase" shelve
files to be deleted first before re-running.
"""
import unittest
from docs.TestFiles.account import Account
from docs.TestFiles.Persistreview import Review
from docs.TestFiles.TestDatabase import Database

accTestData = {"user": "Tim", "password": "Timmy"}

r1 = Review("Jimmy", "Project", "Meeting", 1)
r2 = Review("Timmy", "Project", "Meeting1", 2)
r3 = Review("Lilly", "Project", "Meeting", 3)
r4 = Review("Jim", "Project", "Meeting", 4)

reviewTestData = [r1, r2, r3, r4]

TeamNames = ["TeamA", "TeamB", "TeamC"]
TeamMembers = ["Jim", "Fallon", "Chris"]
ScheduleDates = ["27-11-2023", "28-11-2023", "29-11-2023"]

class TestPersist(unittest.TestCase):
    def setUp(self):
        Database.TestDatabaseReset()
        # Creating an account automatically saves it to Database
        self.DB = Database()
        self.acc = Account("Tim", "Timmy")



    def tearDown(self):
        Database.TestDatabaseReset()
        Account.USER_REGISTRY = []


    def test_save_load_account(self):
        # May have to refactor save, and decouple account and database
        # key error should be handle initially at database level
        self.DB.save(self.acc, "a", "Timmy")

        # Account.log_in uses database load function.
        #account = Account.log_in("Tim", "Timmy")
        account = self.DB.load("a", "Timmy")
        self.assertEqual(account.username, accTestData["user"], "Loaded account should have same username")
        self.assertEqual(account.password, accTestData["password"], "Loaded account should have password")

        # Assert raises Test
        # Note: Overwriting a previously saved account is handled in the account module.
        # Because the account module is delegated the responsibility of knowing
        # what an illegal account creation should be. Thus, the save method does not raise IOError
        try:
            self.assertRaises(TypeError, Database.save, self.acc, "a", 1)  # Database does not accept non string data types as a key
        except NameError:  # This error is raised by account class, not the database
            pass
        self.assertRaises(KeyError, Database.load, "a", "WrongPassword")

    def test_save_load_destroy_review(self):

        for i in range(len(reviewTestData)):
            # Save all review objects
            self.DB.save(reviewTestData[i], "f")

        # Loads a list of review objects
        reviews = self.DB.load("f")

        for x in range(len(reviewTestData)):
            self.assertEqual(reviews[x], reviewTestData[x], "Loaded review object was not the same as Test Data")

        # There are no IOerrors for saving a review object, as duplicated review objects are allowed
        # because different users may need to make a post with the same topic and or content.

        isReviewDeleted = reviews[0]  # Picks arbitrary review object for assertRaise test
        newReview= Review("JohnDoe", "New", "New", 10) # this review object was never added to Database

        # Will raise IOError as this item was never added
        self.assertRaises(IOError, self.DB.delete_data, "f", newReview)

        # Account typed passed in when Review type is expected
        self.assertRaises(TypeError, self.DB.delete_data, "f", self.acc)

        for x in range(len(reviews)):
            self.DB.delete_data("f", reviews[x])

        reviews = self.DB.load("f")
        self.assertEqual(len(reviews), 0, "All review objects were not destroyed.")

        # List is empty so there is no possible object to delete
        self.assertRaises(IOError, self.DB.delete_data, "f", isReviewDeleted)

    def test_save_load_Teams_Schedule(self):
        # Save eac team name in database
        for name in TeamNames:
            Database.save(["John"], "t", name)

        #  Load TeamNames
        LoadedTeamNames = list(Database.load("t"))
        for i in range(len(LoadedTeamNames)):
            self.assertEqual(LoadedTeamNames[i], TeamNames[i], "Loaded Team name should be the same.")
            LoadedTeamMate = Database.load("t").get(TeamNames[i])
            self.assertCountEqual(LoadedTeamMate, ["John"], "Loaded teammate should be the same.")

        #  Database saves and load a scheduled date
        Database.save(ScheduleDates[0], "s", "John")
        self.assertEqual(ScheduleDates[0], Database.load("s").get("John"))


if __name__ == '__main__':
    unittest.main()

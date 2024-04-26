import unittest
from docs.TestFiles.Persistreview import ReviewSchedule
from docs.TestFiles.TestDatabase import Database
from docs.TestFiles.account import Account

class TestSchedules(unittest.TestCase):
    def setUp(self):
        Database.TestDatabaseReset()
        self.users = ["Jack", "Jill", "Hillard"]
        self.ScheduleDates = ["27-11-2023", "28-11-2023", "29-11-2023"]
        self.TeamA = ["Jack", "Jill"]

        # Populate Database with usernames.
        for user in self.users:
            Account(user, "password")


    def tearDown(self):
        Database.TestDatabaseReset()

    def testGetUserDate(self):

        for i in range(len(self.users)):
            ReviewSchedule(self.users[i], self.ScheduleDates[i])

        for i in range(len(self.users)):
            self.assertEqual(ReviewSchedule.getUserDate(self.users[i]), self.ScheduleDates[i], "Dates should be the same.")

    def testGet_Scheduled_UnscheduledTeamMembers(self):
        # Assign a Date to one Team Member Only
        ReviewSchedule(self.TeamA[0], self.ScheduleDates[0])

        # Team Member Jack is scheduled, and Jill is unscheduled

        # Retrieve Schedule Team member: Should be team member at index 0 : ["Jack"]
        scheduledMemberList = ReviewSchedule.getScheduledTeammates(self.TeamA)
        self.assertCountEqual(scheduledMemberList, ["Jack"], "Scheduled list was not returned")

        # Retrieve Unschedule Team Member: Should be team member at index 1 : ["Jill"]
        unscheduledMemberList = ReviewSchedule.getUnscheduledTeamates(self.TeamA)
        self.assertCountEqual(unscheduledMemberList, ["Jill"], "UnScheduled list was not returned")







import unittest
from docs.TestFiles.account import Team
from docs.TestFiles.TestDatabase import Database


class TestTeam(unittest.TestCase):

    def setUp(self):
        Database.TestDatabaseReset()
        self.TeamData = ["TeamX", "TeamY", "TeamZ"]
        self.UserData = ["Jack", "Jill", "Hillary"]
        self.Teams = []
        for team in range(len(self.TeamData)):
            self.Teams.append(Team(self.TeamData[team]))

    def tearDown(self):
        Database.TestDatabaseReset()

    def test_Constructor(self):
        # Attempt to create an existing team name should raise a ValueError
        Team("TeamQ")
        self.assertRaises(ValueError, Team, "TeamQ")

    def test_getTeamNames_addTeamMembers_getTeamMembers(self):
        TeamNames = Team.getTeamNames()
        #  Test if list of Team names are the same as TeamDate
        self.assertCountEqual(TeamNames, self.TeamData, "List of team names should be the same.")
        # Add team members to each team

        for i in range(len(self.Teams)):
            for teamMember in range(len(self.UserData)):
                # Add team members to each team
                self.Teams[i].addTeamMember(TeamNames[i], self.UserData[teamMember])
        # Test if each group of team members is equal to original list of users
        # If test is passed then addTeamMember and get TeamMembers functions as intended
        for i in range(len(self.Teams)):
            members = self.Teams[i].getTeamMembers(TeamNames[i])
            self.assertCountEqual(members, self.UserData, "User names should be the same")

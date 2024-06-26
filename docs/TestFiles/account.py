"""Provides access to an Account object with log in and log out capabilities.

Each Account is capable of storing the review items associated with the User ID.
"""
from docs.TestFiles.TestDatabase import Database


class Account:
    """Creates an Account with a username and password.

    """
    # Load array of used usernames or an empty if no account is created yet.
    session = Database()
    USER_REGISTRY = Database.load("r")

    @classmethod
    def log_in(cls, username, password):
        """
        :param username:
        :param password:
        :return:

        raises : KeyError : Incorrect username or password.
        """
        key = username + "?" + password
        # Load object from persistent storage
        # Return object from persistent storage
        return Database.load("a", key)

    def __init__(self, username, password):
        """Create an account with specified username and password.

        :param username: User ID
        :param password:
        :return: Account object
        """
        #  Test if username is still valid
        if username in Database.load("r"):
            print("Account name is already in use.")
            raise NameError
        else:
            self.USER_REGISTRY.append(username)
            Database.save(username, "r")

        # Continue initialization
        self.username = username
        self.password = password
        self.key = self.username + "?" + self.password
        self.__teamName = "N/A"
        Database.save(self, "a", self.key)

    def get_username(self):
        """
        return Account username
        """
        return self.username

    def change_password(self, password):
        """Change the user's password.

        :param password: New password
        :return: None
        """
        Database.delete_data('a', key=self.key)  # Delete previous password key to account
        # Update changes
        self.password = password
        self.key = self.username + "?" + self.password
        Database.save(self, "a", self.key)


    def joinTeam(self, team_name):
        self.__teamName = team_name
        Database.save(self, "a", self.key)

    def getTeamName(self):
        return self.__teamName

    def log_out(self):
        """End current account session and update changes made.

        :return: None
        """
        Database.save(self, "a", self.key)


class Team:
    __ALL_TEAMS = Database.load("t")

    @classmethod
    def getTeamNames(cls):
        """
        Get the list of all existing team names.
        :return: List of strings
        """
        return list(Database.load("t"))
    @classmethod
    def getTeamMembers(cls, name):
        """
        Return a list of users on the same team.
        :param name: The name of the team.
        :return: List of strings
        """
        teams = Database.load("t")
        if name in list(teams):
            return teams.get(name)
        else:
            raise ValueError('This team does not exists: ' + str(name))
    @classmethod
    def addTeamMember(cls, teamName, teammate):
        """
        Add a new team member to a team
        :param teamName: Name of team user wants to join.
        :param teammate: Name of new team member.
        :return: None
        """
        # Load team dictionary
        teams = Database.load("t")
        # Check if team is in keys
        if teamName in list(teams):
            # Team exist
            members = teams.get(teamName)  # Access members
            members.append(teammate)  # update members
            Database.save(members, "t", teamName)
            #teams.update({teamName: members})  # update team

        else:
            raise ValueError('This team does not exists: ' + str(teamName))

    def __init__(self, team_Name):
        """
        Create a new team with the specified name.
        :param name:
        """
        peek1 = Database.load("t")
        peek = list(Database.load("t"))
        if team_Name in list(Database.load("t")):
            raise ValueError('This team name already exists.')
        else:
            # self.__ALL_TEAMS.update({name: []})
            Database.save([], "t", team_Name)
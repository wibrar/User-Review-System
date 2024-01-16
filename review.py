from database import Database

"""To be implemented by App logic developer: Wasif
    Prototype created by: Jurez Evans """


class Review:
    reviewID = Database.load("id")

    @classmethod
    def get_review(cls, user, topic, index):
        """
        :param user: Account username
        :param topic: Topic of the review to search for
        :param index: Review index
        :return:
        """
        reviews = Database.load("f")

        for obj in reviews:
            if obj.author == user and obj.topic == topic and obj.index == index:
                return obj

    @classmethod
    def updateID(cls):
        """
        Create unique review item id each time a review object is created.
        :return:
        """
        cls.reviewID += 1
        Database.save(cls.reviewID, "id")

    def __init__(self, author, topic, content, rating):
        self.author = author
        self.topic = topic
        self.content = content
        self.index = self.reviewID
        self.rating = rating
        self.comments = []
        self.updateID()
        Database.save(self, "f")

    def edit_review(self, topic, content):
        """

        :param topic: Change topic name
        :param content: Change content name
        :return: None
        """
        # Remove old copy
        Database.delete_data("f", self)

        # Make changes
        self.topic = topic
        self.content = content

        # Save
        Database.save(self, "f")

    def remove_review(self):
        """
        Removes a review from Database
        Return: None
        """
        Database.delete_data("f", self)

    def get_author(self):
        """
        Get method for Author or username
        """
        return self.author

    def __eq__(self, other):
        if type(self) is type(other):
            return self.index == other.index and self.author == other.author and self.topic == other.topic
        else:
            return False


class ReviewRating:
    """ STUB """

    def __init__(self, effort, communication, participation, attendance):
        self.effort = effort
        self.communication = communication
        self.participation = participation
        self.attendance = attendance
        self.average = (int(effort) + int(communication) + int(participation) + int(attendance)) / 4


class ReviewSchedule:
    """
    Assign the date that a team member's performance
    review is scheduled for.
    """
    # Author: Jurez Evans
    __Schedule = Database.load("s")  # Loads empty dictionary, or dictionary of Schedule

    @classmethod
    def getUserDate(cls, user):
        """

        :param user: The (str) username of the account you are requesting a date for.
        :return: The Scheduled date for that user.
        """
        # Check if key exist first then returns result.
        validUsers = list(Database.load("s"))
        if user in validUsers:
            # Then Access key
            return Database.load("s").get(user)
        else:
            raise ValueError("This user has not been scheduled for a review.")

    @classmethod
    def getScheduledTeammates(cls, teamMembers):
        """
        Uses a list of the user's team members to filter out the scheduled team members.

        :param teamMembers: A list of team members.
        :return: (list of strings) A list of the team members who have been scheduled for a performance review.
        """
        if not isinstance(teamMembers, list):
            raise TypeError("userTeam parameter must be a list  type, but type is: " + str(type(teamMembers)))

        scheduledUsers = set(list(Database.load("s")))  # list( dict obj) -> list of keys
        scheduledTeamMates = []
        for x in range(len(teamMembers)):
            if teamMembers[x] in scheduledUsers:
                # This team member is scheduled
                scheduledTeamMates.append(teamMembers[x])

        return scheduledTeamMates

    @classmethod
    def getUnscheduledTeamates(cls, teamMembers):
        """
        Uses a list of the user's team members to filter out the unscheduled team members.
        :param userTeam: A list of the currently logged-in user team members
        :return: (list of strings) A list of unscheduled users.
        """

        if not isinstance(teamMembers, list):
            raise TypeError("userTeam parameter must be a list  type, but type is: " + str(type(teamMembers)))

        unscheduledTeammembers = set()  # Stores unscheduled users
        results = []

        scheduledSet = set(list(Database.load("s")))  # List of scheduled users

        users = Database.load("r")  # All created Users
        if len(scheduledSet) == len(users):
            # There are no unscheduled users or no user accounts created yet.
            return ["No User to be Scheduled"]
        else:
            for userIdx in range(len(users)):
                if users[userIdx] in scheduledSet:
                    # This user has been scheduled already
                    pass
                else:
                    # This user is unscheduled
                    unscheduledTeammembers.add(users[userIdx])
            for x in range(len(teamMembers)):
                if teamMembers[x] in unscheduledTeammembers:
                    results.append(teamMembers[x])
            return results

    def __init__(self, user, date):
        """
        Schedules the specified user's performance review for the given date.
        :param user: (str) The user to be scheduled
        :param date: (str) The date of the performance review
        """

        # self.__Schedule.update({user: date})
        Database.save(date, "s", user)


class ReviewComment:
    """
    Makes a comment object for a review post
    """

    def __init__(self, user, text):
        self.user = user
        self.text = text

    @classmethod
    def add_comment(cls, user, review, text):
        """
        :param user: Account username
        :param review: Review Object
        :param text: Comment content
        :return: None
        """
        review.remove_review()
        # creates a comment object
        comment = ReviewComment(user, text)
        # appends the comment to the list in review
        review.comments.append(comment)
        Database.save(review, "f")

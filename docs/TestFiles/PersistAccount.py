"""Provides access to an Account object with log in and log out capabilities.

Each Account is capable of storing the review items associated with the User ID.
"""
from docs.TestFiles.TestDatabase import Database

class Account:
    """Creates an Account with a username and password.

    """
    # Load array of used usernames or an empty if no account is created yet.
    session = Database()
    USER_REGISTRY = session.load("r")

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
        return cls.session.load("a", key)



    def __init__(self, username, password):
        """Create an account with specified username and password.

        :param username: User ID
        :param password:
        :return: Account object
        """
        #  Test if username is still valid
        if username in self.USER_REGISTRY:
            print("Account name is already in use.")
            raise NameError
        else:
            self.USER_REGISTRY.append(username)


        # Continue initialization
        self.username = username
        self.password = password
        self.key = self.username + "?" + self.password
        self.review_History = []
        #self.session.save(self, "a", self.key) This line removed for database unit test
        # Account names are unique
        # (self.username,self.password)

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
        new_key = self.username + "?" + password
        self.session.change_key(self.key, new_key)
        self.password = password
        self.key = self.username + "?" + self.password

    def add_review(self, review):
        """
        Add review object to account review history

        :param review: Review object
        :return: None
        """
        self.review_History.append(review)
        self.session.save(review, "f")  # Save review object.

    def remove_review(self, ):
        """
        Stub function
        :return:
        """

    def get_review_history(self):
        """
        Returns a collection of all reviews associated with this account.

        :return: An array of reviews created for this account
        """
        return self.review_History

    def log_out(self):
        """End current account session and update changes made.

        :return: None
        """
        self.session.save(self, "a", self.key)
        self.session.save(self.USER_REGISTRY, "r")

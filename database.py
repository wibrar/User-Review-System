"""Contains a persistent storage database to store all relevant data.
Author: Jurez Evans
"""
import shelve


class Database:
    """Persistent storage database that stores all relevant data needed for the server to
    function."""
    DBName = "Database"

    try:
        db = shelve.open(DBName, "r")
        db.close()
    except:
        # Initializes database if not created already.
        db = shelve.open(DBName, flag="c")

        # Store all created accounts in one dictionary
        db["a"] = {}

        # Store all review objects into one array
        db["f"] = []

        # Username registry
        db["r"] = []

        # Stores Last used Review ID
        db["review_id"] = 0

        # Stores ScheduledReviews
        db["s"] = dict()

        # Stores Existing Teams
        db["t"] = dict()

        db.close()

    @classmethod
    def load(cls, mode, key=None):
        """Load item from storage. A key is provided for the data that can be publicly accessed.

        :param mode: 'a' load single account, 'f' load all review items, 'r' Username registry
        :param key: key to access a single account (account mode only)
        :return: a -> Account object, f -> Review History, r -> Username Registry.
        :raises: KeyError if username or password is incorrect or does not exist.
        """
        # Private modes: "id" Private value for Review Class, "s" Private value for ScheduleReivew Class
        # "t" Private value for Team Class
        cls.db = shelve.open(Database.DBName, flag="c")

        if mode.lower() == "a":
            try:
                # Account mode enabled
                data = cls.db[mode.lower()]  # Retrieve account dictionary

                return data[key]  # Retrieve account


            except KeyError as e:
                print("Username or password incorrect.")
                raise KeyError


        elif mode.lower() == "f":
            # Forum mode enabled
            return cls.db["f"]

        elif mode.lower() == "r":
            return cls.db["r"]

        elif mode.lower() == "id":
            return cls.db["review_id"]

        elif mode.lower() == "s":
            return cls.db["s"]

        elif mode.lower() == "t":
            return cls.db["t"]

        cls.db.close()

    @classmethod
    def save(cls, item, mode, key=None):
        """Save item to storage

        :param item: Object to store
        :param mode: 'a' Save single account, 'f' Save review item, 'r' Register username 'id' store review ID
        :param key:  key to store a single account (account mode only)
        :return: None
        """
        cls.db = shelve.open(Database.DBName, flag="c")

        if mode.lower() == "a":
            # Account mode enable
            try:
                if not(isinstance(key, str)):
                    raise TypeError
                else:
                    data = cls.db['a']
                    data[key] = item
                    cls.db['a'] = data
            except TypeError:
                print("Key must be a string, type detected is :", type(key))
                raise TypeError

        elif mode.lower() == "f":
            # Forum mode enabled
            data = cls.db['f']
            data.append(item)
            cls.db['f'] = data

        elif mode.lower() == "r":
            # Username registry enabled
            data = cls.db['r']
            data.append(item)
            cls.db['r'] = data

        elif mode.lower() == "id":
            # Update review id integer
            cls.db["review_id"] = item

        elif mode.lower() == "s":
            data = cls.db["s"]
            data[key] = item
            cls.db["s"] = data

        elif mode.lower() == "t":
            data = cls.db["t"]
            data[key] = item
            cls.db["t"] = data

        cls.db.close()

    @classmethod
    def change_key(cls, old, new, acc):
        """Replace old key with new key.

        :param old: Old key that will be replaced
        :param new: New key that replaces the old one
        :return:
        """
        cls.db = shelve.open(Database.DBName, flag="c")

        account = cls.db['a'][old]
        del cls.db['a'][old]
        cls.db['a'][new] = account

        cls.db.close()

    @classmethod
    def delete_data(cls, mode, item=None, key=None):
        """Delete data no longer in use.

        :param key: The key to the account to delete
        :param item: The item to delete (review only)
        :param mode: "f" delete review object, "a" delete account
        :return:
        """
        cls.db = shelve.open(cls.DBName, "c")

        if mode.lower() == "a":
            data = cls.db['a']
            try:
                del data[key]
            except KeyError:
                print('Item does not exist or has already been deleted')


        elif mode.lower() == "f":
            found = False
            try:

                reviews = cls.db["f"]
                if len(reviews) > 0:
                    # Compare type
                    if type(reviews[0]) != type(item):
                        raise TypeError
                else:
                    # No review object recorded
                    raise IOError
                for obj in reviews:
                    if item == obj:
                        found = True
                        reviews.remove(obj)
                        cls.db["f"] = reviews
                        break
                if not found:
                    raise IOError

            except IOError:
                print("This item does not exist, or has already been deleted.")
                raise IOError


            except TypeError:
                print("The passed in item is not a review object.")
                raise TypeError

        cls.db.close()



    def __init__(self):
        """
        Stub, no instance is ever created.
        :param self:
        :return:
        """

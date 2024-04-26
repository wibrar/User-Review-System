import unittest
from HTMLTemplatesUT import HTMLTemplatesUT



class TestHTMLTemplates(unittest.TestCase):
    def setUp(self):
        # Set self.maxDiff to None to see the entire diff output for failures
        self.maxDiff = None
    def test_get_login(self):
        # Get the rendered HTML from the get_login() method
        rendered_html = HTMLTemplatesUT.get_login()

        # Define the expected HTML output based on your get_login() method
        expected_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>
    <form action="/login" method="post">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br>
        <button type="submit">Login</button>
    </form>
</body>
</html>"""

        # Assert that the rendered HTML matches the expected HTML
        self.assertEqual(rendered_html, expected_html)

    def test_get_forum(self):
        # Get the rendered HTML from the get_forum() method
        rendered_html = HTMLTemplatesUT.get_forum()

        # Define the expected HTML output based on your get_forum() method
        expected_html ="""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Forum</title>
</head>
<body>
    <h1>Forum</h1>
    <ul>
        % for obj in reviews:
            <li>
                <strong>{{ obj.author }}:</strong>
                <em>{{ obj.topic }}</em> - {{ obj.content }}
                <a href="/update_review/{{obj.index}}">Edit</a>
            </li>
        % end
    </ul>
    <br>
    <label for="search">Search by:</label>
        <select name="search" id="search">
            <option value="topic">Topic</option>
            <option value="author">Author</option>
        </select><br>
        <input type="text" id="search" name="search">
        <input type="submit" value="Search"><br><br>
    <label for="filter">Filter by Topic:</label><br>
        <input type="text" id="filter" name="filter">
        <input type="submit" value="Filter"><br><br>
    <a href="/logout">Logout</a>
</body>
</html>
"""


        # Assert that the rendered HTML matches the expected HTML
        self.assertEqual(rendered_html, expected_html)

    def test_get_profile(self):
        # Get the rendered HTML from the get_forum() method
        rendered_html = HTMLTemplatesUT.get_profile()

        # Define the expected HTML output based on your get_forum() method
        expected_html ="""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Profile</title>
</head>
<body>
    <h1>Welcome, {{username}}!</h1>
    <p>This is your profile page.</p>
    <button onclick="window.location.href='/forum'">Go to Forum</button>
    <button onclick="window.location.href='/writereview'">Write a Review</button>
    <br>
    <a href="/logout">Logout</a>
</body>
</html>"""


        # Assert that the rendered HTML matches the expected HTML
        self.assertEqual(rendered_html, expected_html)


    def test_get_register(self):
        # Get the rendered HTML from the get_forum() method
        rendered_html = HTMLTemplatesUT.get_register()

        # Define the expected HTML output based on your get_forum() method
        expected_html ="""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register</title>
</head>
<body>
    <h1>Register</h1>
    <form action="/register" method="post">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br>
        <button type="submit">Register</button>
    </form>
</body>
</html>
"""



        # Assert that the rendered HTML matches the expected HTML
        self.assertEqual(rendered_html, expected_html)


    def test_get_register(self):
    # Get the rendered HTML from the get_forum() method
        rendered_html = HTMLTemplatesUT.get_register()

    # Define the expected HTML output based on your get_forum() method
        expected_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register</title>
</head>
<body>
    <h1>Register</h1>
    <form action="/register" method="post">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br>
        <button type="submit">Register</button>
    </form>
</body>
</html>
"""

    # Assert that the rendered HTML matches the expected HTML
        self.assertEqual(rendered_html, expected_html)


    def test_get_reviews(self):
    # Get the rendered HTML from the get_forum() method
        rendered_html = HTMLTemplatesUT.get_reviews()

    # Define the expected HTML output based on your get_forum() method
        expected_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Write Review</title>
</head>
<body>
    <h1>Write a Review</h1>
    <form action="/submit_review" method="post">
        <label for="review">Your Review:</label><br>
        <textarea id="review" name="review" rows="4" cols="50" required></textarea><br>
        <button type="submit">Submit Review</button>
    </form>
    <br>
    <a href="/forum">Go to Forum</a>
    <br>
    <a href="/logout">Logout</a>
</body>
</html>
"""
    # Assert that the rendered HTML matches the expected HTML
        self.assertEqual(rendered_html, expected_html)

    def test_get_homepage(self):
    # Get the rendered HTML from the get_forum() method
        rendered_html = HTMLTemplatesUT.get_homepage()

    # Define the expected HTML output based on your get_forum() method
        expected_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Homepage</title>
</head>
<body>
    <h1>Welcome to the Homepage</h1>
    <p>This is the homepage of the website.</p>
    <p><a href="/login">Login</a> or <a href="/register">Register</a></p>
</body>
</html>"""
    # Assert that the rendered HTML matches the expected HTML
        self.assertEqual(rendered_html, expected_html)



if __name__ == "__main__":
    unittest.main()

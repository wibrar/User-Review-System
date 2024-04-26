import unittest
from HTMLTemplates import HTMLTemplates



class TestHTMLTemplates(unittest.TestCase):
    def setUp(self):
        # Set self.maxDiff to None to see the entire diff output for failures
        self.maxDiff = None
    def test_get_login(self):
        # Get the rendered HTML from the get_login() method
        rendered_html = HTMLTemplates.get_login()

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
        rendered_html = HTMLTemplates.get_forum()

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
                <em>{{ obj.topic }}</em> - {{ obj.content }} <br>
                &nbsp <strong>Effort:</strong> {{obj.rating.effort}} 
                &nbsp <strong>Communication:</strong> {{obj.rating.communication}} 
                &nbsp <strong>Participation:</strong> {{obj.rating.participation}}
                &nbsp <strong>Attendance:</strong> {{obj.rating.attendance}}
                <p>&nbsp Average Rating: {{obj.rating.average}} / 10</p>
                <a href="/update_review/{{obj.index}}">Edit</a>
                <em>{{ obj.topic }}</em> - {{ obj.content }}
                <a href="/update_review/{{obj.index}}">Edit</a>
                <a href="/delete_review/{{obj.index}}">Delete</a>
            </li>
            % end
    </ul>
    <br>
    <form action="/search" method="post">
        <label for="search">Search by:</label>
            <select name="searchchoice" id="searchchoice">
                <option value="topic">Topic</option>
                <option value="author">Author</option>
                <option value="content">Content</option>
            </select><br>
            <input type="text" id="search" name="search">
            <input type="submit" value="Search"><br><br>
    </form>
    <label for="filter">Filter by Topic:</label><br>
        <input type="text" id="filter" name="filter">
        <input type="submit" value="Filter"><br><br>
    <a href="/forum">Return</a>
    <a href="/logout">Logout</a>
</body>
</html>
"""


        # Assert that the rendered HTML matches the expected HTML
        self.assertEqual(rendered_html, expected_html)

    def test_get_profile(self):
        # Get the rendered HTML from the get_forum() method
        rendered_html = HTMLTemplates.get_profile()

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
    <h2>Your Reviews:</h2>
    <ul id="reviews-list"></ul>
    <button onclick="window.location.href='/forum'">Go to Forum</button>
    <button onclick="window.location.href='/writereview'">Write a Review</button>
    <br>
    <a href="/logout">Logout</a>

    <script>
        // Fetch user reviews and populate the reviews list
        var username = "{{username}}"; // Replace this with the actual username
        var reviewsList = document.getElementById('reviews-list');

        fetch('/api/my_reviews?username=' + username)
            .then(response => response.json())
            .then(data => {
                data.forEach(review => {
                    var li = document.createElement('li');
                    li.textContent = review.topic + ': ' + review.content;
                    reviewsList.appendChild(li);
                });
            })
            .catch(error => console.error('Error fetching reviews:', error));
    </script>
</body>

</html>
"""


        # Assert that the rendered HTML matches the expected HTML
        self.assertEqual(rendered_html, expected_html)


    def test_get_register(self):
        # Get the rendered HTML from the get_forum() method
        rendered_html = HTMLTemplates.get_register()

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
        rendered_html = HTMLTemplates.get_register()

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


    def test_write_reviews(self):
    # Get the rendered HTML from the get_forum() method
        rendered_html = HTMLTemplates.writereview()

    # Define the expected HTML output based on your get_forum() method
        expected_html = """
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>New Review</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
        }

        .container {
            margin-top: 20px;
        }

        .review-form {
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            background-color: #f9f9f9;
        }

        .form-input {
            display: block;
            margin: 10px;
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        .save-button {
            background-color: #007bff;
            color: #fff;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <h1>New Review</h1>
    <div class="container">
        <form action="/add_review" method="POST" class="review-form">
            <label for="topic">Topic:</label>
            <input type="text" id="topic" name="topic" class="form-input" required>
            <label for="content">Review Content:</label>
            <textarea id="content" name="content" class="form-input" required></textarea>
            <p>Rate the following on a scale from 1 to 5:</p>
            <input type="number" min="1" max="10" name="effort"> Effort expended on this topic.</input><br>
            <input type="number" min="1" max="10" name="communication"> Communication with team.</input><br>
            <input type="number" min="1" max="10" name="participation"> Participation in critical reviews.</input><br>
            <input type="number" min="1" max="10" name="attendance"> Attending team meetings.</input><br><br>
        <input type="submit" value="Save Review" class="save-button"><br><br>
        </form>
    </div>
</body>
</html>"""
    # Assert that the rendered HTML matches the expected HTML
        self.assertEqual(rendered_html, expected_html)

    def test_get_homepage(self):
    # Get the rendered HTML from the get_forum() method
        rendered_html = HTMLTemplates.get_homepage()

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

class HTMLTemplates:
    @staticmethod
    def scheduler_page():
        """Returns HTML content for the scheduler page."""
        return """<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="/static/styles.css">
        
        <title>Scheduler</title>
    </head>
    <body>
        <h1>Scheduler</h1>
        <form action="/schedule" method="post">
            <label for="date">Select a date:</label>
            <input type="date" id="date" name="date" required><br>
            <label for="username">Assign a username:</label>
            <input type="text" id="username" name="username" required><br>
            <button type="submit">Assign Deadline</button>
        </form>
        <br>
        <a href="/forum">Go to Forum</a>
        <a href="/logout">Logout</a>
    </body>
    </html>"""

    @staticmethod
    def profile():
        return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/static/styles.css">

    <title>User Profile - {{ username }}</title>
</head>
<body>
    <h1>User Profile - {{ username }}</h1>
    <h2>Reviews Written by or About {{ username }}:</h2>
    <ul>
        % for review in userreviews:
            <li>
                <strong>{{ review.author }}:</strong>
                <em>{{ review.topic }}</em> - {{ review.content }} <br>
                &nbsp <strong>Effort:</strong> {{ review.rating.effort }} 
                &nbsp <strong>Communication:</strong> {{ review.rating.communication }} 
                &nbsp <strong>Participation:</strong> {{ review.rating.participation }}
                &nbsp <strong>Attendance:</strong> {{ review.rating.attendance }}
                <p>&nbsp Average Rating: {{ review.rating.average }} / 10</p>
            </li>
        % end
    </ul>
    <br>
    <a href="/forum">Go to Forum</a>
    <a href="/logout">Logout</a>
</body>
</html>
"""

    @staticmethod
    def get_login():
        """Returns HTML content for the login page."""
        return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link rel="stylesheet" href="/static/styles.css">

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

    @staticmethod
    def get_forum():
        """Returns HTML content for the forum page."""
        return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Forum</title>
    <link rel="stylesheet" href="/static/styles.css">

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
                <a href="/edit_review/{{obj.index}}/{{obj.topic}}">Edit</a>
                <a href="/comment/{{obj.author}}/{{obj.index}}/{{obj.topic}}">Comment</a>
                <a href="/view_comments/{{obj.author}}/{{obj.index}}/{{obj.topic}}">View Comments</a>
                <a href="/delete_post/{{obj.index}}/{{obj.topic}}"method="GET">Delete</a>
                
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
    <a href="/sort">Sort Revies</a>
    <a href="/profile">Return</a>
    <a href="/logout">Logout</a>
    <a href="/scheduler">Go to Scheduler</a>
</body>
</html>
"""

    @staticmethod
    def get_profile():
        """Returns HTML content for the user profile page."""
        return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Profile</title>
    <link rel="stylesheet" href="/static/styles.css">

</head>
<body>
    <h1>Welcome, {{username}}!</h1>
    <p>This is your profile page.</p>
    <h2>Your Reviews:</h2>
    <h3> Team:  </h3>
    <p> {{teams}}</p>
    
    <ul id="reviews-list"></ul>
    <button onclick="window.location.href='/forum'">Go to Forum</button>
    <button onclick="window.location.href='/writereview'">Write a Review</button>
    <button onclick="window.location.href='/change_password'">Change password</button>
    <button onclick="window.location.href='/formteam'">Create a new team</button>
    <button onclick="window.location.href='/teams'">Join a team</button>
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

    @staticmethod
    def get_team_page():
        return """<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Team Page</title>
        </head>
        <body>
            <h3> Teams:  </h3>
                <ul>
                    % for team in teams:
                        <strong> "{{team}}" </strong>
                        <a href="/addmember/{{team}}/{{username}}">Join</a>
                        <br>
                    % end
                </ul>
        </body>
        </html>
        """

    @staticmethod
    def get_register():
        """Returns HTML content for the registration page."""
        return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register</title>
    <link rel="stylesheet" href="/static/styles.css">

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

    @staticmethod
    def edit_reviews(review, topic, content):
        """Returns HTML content for writing a review."""
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit Review</title>
    <link rel="stylesheet" href="/static/styles.css">

</head>
<body>
    <h1>Edit Review</h1>
        <form action="/update_review" method="post">
            <label for="review">Topic:</label>
            <input type="hidden" name="review_index" value="{review.index}">
            <input type="hidden" name="review_topic" value="{review.topic}">
            <textarea id="review" name="topic" rows="1" cols="10" required>{topic}></textarea><br>
            <textarea id="review" name="content" rows="4" cols="50" required>{content}></textarea><br>
            <p>Rate the following on a scale from 1 to 10:</p>
            <input type="number" min="1" max="10" name="effort"> Effort expended on this topic.</input><br>
            <input type="number" min="1" max="10" name="communication"> Communication with team.</input><br>
            <input type="number" min="1" max="10" name="participation"> Participation in critical reviews.</input><br>
            <input type="number" min="1" max="10" name="attendance"> Attending team meetings.</input><br><br>
        <input type="submit" value="Save Review" class="save-button"><br><br>
        </form>
    <br>
    <a href="/forum">Go to Forum</a>
    <br>
    <a href="/logout">Logout</a>
</body>
</html>
"""

    @staticmethod
    def writereview():
        """Returns HTML content for writing a new review."""
        return """
        <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>New Review</title>
    <link rel="stylesheet" type="text/css" href="/static/styles.css"> <!-- Link to your CSS file -->
    <style>
        body {
            font-family: 'Arial', sans-serif;
            text-align: center;
            background-color: #1a1a1a; /* Dark background */
            color: #fff;
            margin: 0;
            padding: 0;
        }

        h1 {
            font-size: 2em;
            color: #4CAF50; /* Green header */
        }

        .container {
            margin-top: 20px;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
            background-color: #262626; /* Dark content background */
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
            border-radius: 8px;
            padding: 20px;
        }

        .review-form {
            border: 1px solid #4CAF50; /* Green border */
            border-radius: 5px;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            background-color: #333; /* Darker form background */
        }

        .form-input {
            display: block;
            margin: 10px;
            width: calc(100% - 20px);
            padding: 10px;
            border: 1px solid #4CAF50; /* Green border */
            border-radius: 5px;
            background-color: #fff; /* White input background */
            color: #000; /* Black text color */
        }

        .save-button {
            background-color: #007bff;
            color: #fff;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s ease-in-out;
        }

        .save-button:hover {
            background-color: #45a049; /* Darker green on hover */
        }
    </style>
</head>

<body>
    <header>
        <h1>New Review</h1>
    </header>
    <div class="container">
        <form action="/add_review" method="POST" class="review-form">
            <label for="topic">Topic:</label>
            <select id="topic" name="topic" class="form-input" required>
            %for member in members:
                <option value= "{{member}}"> {{member}} </option>
            %end
            </select>

            <label for="content">Review Content:</label>
            <textarea id="content" name="content" class="form-input" required></textarea>
            <p>Rate the following on a scale from 1 to 10:</p>
            <input type="number" min="1" max="10" name="effort"> Effort expended on this topic.</input><br>
            <input type="number" min="1" max="10" name="communication"> Communication with team.</input><br>
            <input type="number" min="1" max="10" name="participation"> Participation in critical reviews.</input><br>
            <input type="number" min="1" max="10" name="attendance"> Attending team meetings.</input><br><br>
            <input type="submit" value="Save Review" class="save-button"><br><br>
        </form>
    </div>
</body>

</html>"""

    @staticmethod
    def get_homepage():
        """Returns HTML content for the homepage."""
        return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/static/styles.css"> 
    <title>Homepage</title>
    <link rel="stylesheet" href="/static/styles.css">

</head>
<body>
    <h1>Welcome to the Homepage</h1>
    <p>This is the homepage of the website.</p>
    <p><a href="/login">Login</a> or <a href="/register">Register</a></p>
</body>
</html>"""

    @staticmethod
    def change_password_page():
        """Returns HTML content for the change password page."""
        return """<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Change Password</title>
        <link rel="stylesheet" href="/static/styles.css">

    </head>
    <body>
        <h1>Change Password</h1>
        <form action="/change_password" method="post">
            <label for="old">Old Password:</label>
            <input type="password" id="old" name="old" required><br>
            <label for="new">New Password:</label>
            <input type="password" id="new" name="new" required><br>
            <button type="submit">Change Password</button>
        </form>
    </body>
    </html>
    """

    @staticmethod
    def createTeamPage():
        """Returns HTML document to create a new team."""
        return """<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Create a new Team</title>
            </head>
            <body>
        <h1>New Team</h1>
        <form action="/formteam" method="post">
            <label for="team">Team Name:</label>
            <input type="text" id="team" name="team" required><br>
            <button type="submit">Create Team</button>
        </form>
    </body>
    </html>
    """

    @staticmethod
    def schedule_list():
        """
        An HTML page for viewing all schedule reviews for the specified team.
        :return: An HTML Page.
        """
        return """<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Schedule</title>
            <link rel="stylesheet" href="/static/styles.css">
        </head>
        <body>
            <h1>Schedule</h1>
            <ul>    
                    <p>Current Date: {{ date }} </p>
                    <p>Scheduled:</p>
                    % for obj in reviews:
                    <li>
                        <strong>{{ obj[0] }}:</strong> {{ obj[1] }}
                    </li>
                    % end
                    
                    <p style="color:red;">Late:
                    % for obj in late_reviews:
                    <li>
                        <strong>{{ obj[0] }}:</strong> {{ obj[1] }}
                    </li>
                    % end
                    </p>
            </ul>
            <a href="/profile">Return</a>
            <a href="/logout">Logout</a>
            <a href="/scheduler">Go to Scheduler</a>
        </body>
        </html>
        """

    @staticmethod
    def comment(review):
        """Comment page to add comment for a review post."""
        return f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Comment</title>
    </head>
    <body>
        <h1>Comment</h1>
            <form action="/comment" method="post">
                <label for="comment">Topic:</label>
                <input type="hidden" name="review_author" value="{review.author}">
                <input type="hidden" name="review_index" value="{review.index}">
                <input type="hidden" name="review_topic" value="{review.topic}">
                <input type="hidden" name="review" value="{review}">
                <textarea id="comment" name="text" rows="4" cols="50" required></textarea><br>
            <input type="submit" value="Save Comment" class="save-button"><br><br>
            </form>
        <br>
        <a href="/forum">Go to Forum</a>
        <br>
        <a href="/logout">Logout</a>
    </body>
    </html>
    """

    @staticmethod
    def view_review():
        """Returns HTML content for the forum page."""
        return """<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Review and Comments</title>
    </head>
    <body>
        <h1>Review and Comments</h1>
        <ul>
                <li>
                    <strong>{{review.author }}:</strong>
                    <em>{{review.topic}}</em> - {{review.content}} <br>
                    &nbsp <strong>Effort:</strong> {{review.rating.effort}} 
                    &nbsp <strong>Communication:</strong> {{review.rating.communication}}
                    &nbsp <strong>Participation:</strong> {{review.rating.participation}}
                    &nbsp <strong>Attendance:</strong> {{review.rating.attendance}}
                    <p>&nbsp Average Rating: {{review.rating.average}} / 10</p>
                    
                    % for comment in comments:
                        <br>
                        <strong>{{comment.user}}:</strong>
                        <em>{{comment.text}}</em>
                        </br>
                    % end    
                </li>
    </body>
    </html>
    """

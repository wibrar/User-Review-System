"""Models a local server for hosting team-related performance reviews
using the Bottle Framework."""

from bottle import run, route, request, template, response, static_file

from account import Account, Team
from review import Review, ReviewRating, ReviewSchedule, ReviewComment
from HTMLTemplates import HTMLTemplates
import datetime

hostName = "localhost"
serverPort = 8080

try:
    user = Account("Admin", "admin")
except NameError:
    user = Account.log_in("Admin", "admin")


@route('/static/<filename:path>')
def static(filename):
    """
    Method for loading the CSS styling.
    :param filename: The name of the file where the stylings are stored.
    :return: The static file used for CSS.
    """
    return static_file(filename, root='./static')  # Adjust the root path accordingly


@route('/')
def home():
    """
    Displays the homepage of the website.

    :return: HTML page
    """
    return HTMLTemplates.get_homepage()


@route('/login')
def login():
    """
    Displays the login page of the website, for the user
    to log into a previously created Account.

    :return: HTML page
    """
    return HTMLTemplates.get_login()


@route('/login', method='POST')
def do_login():
    """
    Performs the log in action using the Account class.

    If an Account with the given information doesn't exist,
    returns a KeyError.

    :return: HTML page
    """
    global user
    username = request.forms.get('username')
    password = request.forms.get('password')
    try:
        user = Account.log_in(username, password)
        response.set_cookie("account", username, path="/")
        response.set_cookie("password", password, path="/")
    except KeyError:
        return "Incorrect username/password."
    profile = HTMLTemplates.get_profile()
    u = request.get_cookie("account")
    p = request.get_cookie("password")
    acc = Account.log_in(username, password)
    if not acc.hasTeam():
        teams = "No Team to Display"
    else:
        teams = acc.getTeamName()
    return template(profile, username=username, teams=teams)


@route('/change_password')
def change_user_password():
    """
    Return form to Change current logged-in user password.
    :return: HTML Template
    """
    return HTMLTemplates.change_password_page()


@route('/change_password', method='POST')
def do_change_password():
    """
    Changes current logged-in user password to the specified password.
    :return: HTML Template
    """
    # Note the HTML Page for Change Password has not been added in yet.
    old = request.forms.get('old')
    new = request.forms.get('new')
    acc = request.get_cookie('account')
    account = Account.log_in(acc, old)
    account.change_password(new)
    profile = HTMLTemplates.get_profile()
    acc = Account.log_in(request.get_cookie("account"), request.get_cookie("password"))
    if not acc.hasTeam():
        teams = "No Team to Display"
    else:
        teams = acc.getTeamName()
    return template(profile, username=request.get_cookie("account"), teams=teams)


@route('/logout')
def do_logout():
    """
    Logs out the current active Account

    :return: HTML page"""
    global user
    user.log_out()
    response.set_cookie("account", "none")
    response.set_cookie("password", "none")
    #   Admin account indicates that no user session is active
    user = Account.log_in("Admin", "admin")

    return HTMLTemplates.get_homepage()


@route('/register')
def register():
    """
    Displays the register page of the website, for the user
    to make a new Account.

    :returns: HTML page
    """
    return HTMLTemplates.get_register()


@route('/register', method='POST')
def do_register():
    """
    Performs the register action using the Account class.

    If an Account with the given username already exists,
    returns a NameError.

    :returns: HTML page
    """
    username = request.forms.get('username')
    password = request.forms.get('password')
    try:
        user = Account(username, password)
        response.set_cookie("account", username)
        response.set_cookie("password", password, path="/")
    except NameError:
        return "Username already taken."
    profile = HTMLTemplates.get_profile()
    acc = Account.log_in(username, password)
    if not acc.hasTeam():
        teams = "No Team to Display"
    else:
        teams = acc.getTeamName()
    return template(profile, username=username, teams=teams)


@route('/profile')
def profile():
    """
    Displays the profile page for the user.

    :returns: An HTML Page.
    """
    user = request.get_cookie("account")
    if user == None:
        return "You aren't logged in!"
    else:
        profile = HTMLTemplates.get_profile()
        acc = Account.log_in(request.get_cookie("account"), request.get_cookie("password"))
        if not acc.hasTeam():
            teams = "No Team to Display"
        else:
            teams = acc.getTeamName()
        return template(profile, username=request.get_cookie("account"), teams=teams)


@route('/forum')
def forum():
    """
    Displays the forum, which shows all published reviews.

    :return: An HTML page.
    """
    reviews = user.session.load('f')
    forum.html = HTMLTemplates.get_forum()
    return template(forum.html, reviews=reviews)


@route('/writereview')
def writereview():
    """
    Displays the HTML page for writing a review.

    :return: An HTML page.
    """

    account = Account.log_in(request.get_cookie("account"), request.get_cookie("password"))
    if account.hasTeam():
        team = account.getTeamName()
        teamData = Team.getTeamMembers(team)  # ["Jack","Jill","Scott"] # for testing
    else:
        teamData = ["You are not apart of a Team"]

    return template(HTMLTemplates.writereview(), members=teamData)


@route('/add_review', method='POST')
def add_review():
    """
    Publishes a review to the forum by saving it to the database.

    :return: An HTML page.
    """
    # author = user.username
    # Test if cookie works correctly
    author = request.get_cookie("account")
    author = request.get_cookie("account")
    topic = request.forms.get('topic')
    content = request.forms.get('content')

    effort = request.forms.get('effort')
    communication = request.forms.get('communication')
    participation = request.forms.get('participation')
    attendance = request.forms.get('attendance')

    rating = ReviewRating(effort, communication, participation, attendance)
    Review(author, topic, content, rating)
    forum.html = HTMLTemplates.get_forum()
    return template(forum.html, reviews=user.session.load('f'))


@route('/edit_review/<index>/<topic>')
def edit_review(index, topic):
    """
    Displays the HTML page for editing a review.

    :param index: The index of the review, used to find the specific review.
    :param topic: The topic for the review, used to find the specific review.
    :return: An HTML page, or an error if review doesn't exist.
    """
    author = user.username  # Assuming you want to edit reviews only for the logged-in user
    review = Review.get_review(author, topic, int(index))
    if review:
        return HTMLTemplates.edit_reviews(review, review.topic, review.content)
    else:
        return "Review not found"


@route('/update_review', method='POST')
def update_review():
    """
    The update method to update a review that is being edited.

    :return:  The forum HTML page, which will display the updated reviews.
    """
    # get username
    author = user.username

    # delete old review
    oldindex = request.forms.get('review_index')
    oldtopic = request.forms.get('review_topic')
    rev = Review.get_review(author, oldtopic, int(oldindex))
    rev.remove_review()

    # update new review
    effort = request.forms.get('effort')
    communication = request.forms.get('communication')
    participation = request.forms.get('participation')
    attendance = request.forms.get('attendance')
    rating = ReviewRating(effort, communication, participation, attendance)
    topic = request.forms.get('topic')
    content = request.forms.get('content')
    Review(author, topic, content, rating)

    # Redirect to the main page to display the reviews
    forum.html = HTMLTemplates.get_forum()
    return template(forum.html, reviews=user.session.load('f'))


@route('/search', method='POST')
def do_search():
    """Performs a search on published reviews, by either topic, author, or content.

    :return: The HTML page for the forum, with the reviews that match the search criteria shown."""
    query = request.forms.get('search')
    searchby = request.forms.get('searchchoice')
    reviews = user.session.load('f')
    found = []

    for obj in reviews:
        if searchby == "topic":
            if query.lower() in obj.topic.lower():
                found.append(obj)
        elif searchby == "author":
            if query.lower() in obj.author.lower():
                found.append(obj)
        elif searchby == "content":
            if query.lower() in obj.content.lower():
                found.append(obj)

    forum.html = HTMLTemplates.get_forum()
    return template(forum.html, pagename="Search", reviews=found)


@route('/sort')
def do_sort():
    """Sorts the published reviews based on their average rating score.


   :return: The HTML page for the forum, sorted by average rating score.
   """
    reviews = user.session.load('f')
    sortedreviews = sorted(reviews, key=lambda x: x.rating.average, reverse=True)

    forum.html = HTMLTemplates.get_forum()
    return template(forum.html, reviews=sortedreviews)


@route('/delete_post/<index>/<topic>', method='GET')
def delete_post(index, topic):
    """
    A method to delete posts from the saved database, removing them from the forum page and any searched.
    :param index: The index for the review, which helps to find the specific review.
    :param topic: The topic for the review, which helps to find the specific review.
    :returns: The HTML page for the forum, with the removed review gone.
    """
    author = user.username
    rev = Review.get_review(author, topic, int(index))
    rev.remove_review()
    forum.html = HTMLTemplates.get_forum()
    return template(forum.html, reviews=user.session.load('f'))


@route('/comment/<author>/<index>/<topic>')
def comment_post(author, index, topic):
    """
    The page for writing comments.

    :param author: The author of the review to comment on, which helps to get the specific review.
    :param index: The index of the review to comment on, which helps to get the specific review.
    :param topic: The topic for the review to comment on, which helps to get the specific review.
    :return: The HTML page for commenting, which saves the specific comment in the process.
    """

    review = Review.get_review(author, topic, int(index))
    return HTMLTemplates.comment(review)


@route("/comment", method='POST')
def add_comment():
    """
    The POST method that adds a comment to a review object, using methods from both Review and ReviewComment classes.

    :return: The forum method, which displays the forum HTML page.
    """
    author = request.forms.get("review_author")
    index = request.forms.get("review_index")
    topic = request.forms.get("review_topic")

    current_user = request.get_cookie("account")
    review = Review.get_review(author, topic, int(index))
    comment_content = request.forms.get("text")

    ReviewComment.add_comment(current_user, review, comment_content)

    return forum()


@route('/view_comments/<author>/<index>/<topic>')
def view_comments(author, index, topic):
    """
    Shows post, and all comments on the current post.
    Comments consist of the content (string) and the name of the user making the comment (string).

    :param author: The author of the review to look at.
    :param index: The index of the review to look at.
    :param topic: The topic of the review to look at.
    :return: An HTML page, which displays the review and all comments attached to that review.
    """
    review = Review.get_review(author, topic, int(index))
    comments = review.comments

    view_comments.html = HTMLTemplates.view_review()
    return template(view_comments.html, review=review, comments=comments)


@route('/teams')
def team_page():
    """A page to look at all created teams, and the members in each team.

    :return: An HTML page, displaying all teams.
    """
    teams = Team.getTeamNames()
    teamPage = HTMLTemplates.get_team_page()
    if len(teams) == 0:
        return "There are no created teams."
    return template(teamPage, username=request.get_cookie("account"), teams=teams)


@route('/formteam')
def get_form_team():
    """The method for forming a team.

    :return: An HTML page, where the team is created.
    """
    return HTMLTemplates.createTeamPage()


@route('/formteam', method='POST')
def do_form_team():
    """The method for creating a team. Once created, a team is displayed on the list of all teams and can be joined.


    :return: An HTML page of the profile, where it will now display the joined team.
    """

    try:
        team_name = request.forms.get("team")
        Team(team_name)
    except ValueError:
        return "Name already taken."
    profile = HTMLTemplates.get_profile()
    acc = Account.log_in(request.get_cookie("account"), request.get_cookie("password"))
    if not acc.hasTeam():
        teams = "No Team to Display"
    else:
        teams = acc.getTeamName()
    return template(profile, username=request.get_cookie("account"), teams=teams)


@route('/addmember/<team_name>/<member>')
def add_members(team_name, member):
    """
    A page for the current user to join a formed team.


    :return: An HTML page of the profile, which will now display the team you've joined.
    """

    acc = Account.log_in(request.get_cookie("account"), request.get_cookie("password"))
    if not acc.hasTeam():
        acc.joinTeam(team_name)
    else:
        return "You are already on a team."
    try:
        Team.addTeamMember(team_name, member)
    except ValueError:
        return ValueError
    profile = HTMLTemplates.get_profile()

    teams = acc.getTeamName()
    return template(profile, username=request.get_cookie("account"), teams=teams)


@route('/scheduler')
def scheduler_page():
    """A page that shows the scheduler for reviews.

    :returns: The HTML page of the scheduler.
    """
    return HTMLTemplates.scheduler_page()


@route('/schedule', method='POST')
def schedule():
    """A post method that schedules the reviews. Saves the date and the user, and uses them to create a
    ReviewSchedule objects.

    :return: An HTML page. (The Schedule page)
    """

    schedule_date = request.forms.get("date")
    schedule_user = request.forms.get("username")

    team_list = Team.getTeamNames()
    team_name = None
    for x in team_list:
        members_list = Team.getTeamMembers(x)
        if schedule_user in members_list:
            team_name = x
            ReviewSchedule(schedule_user, schedule_date)
            return schedule_list(team_name)

    if team_name is None:
        return "This person is not on your team."


@route('/schedule_list/<name>')
def schedule_list(name):
    """A method to look at all scheduled reviews for your team.

    :param name: The name of the team that you are looking at the scheduled review list of.

    :returns: An HTML page."""

    review_users = ReviewSchedule.getScheduledTeammates(Team.getTeamMembers(name))
    review_list = []
    for x in review_users:
        review_list.append((x, ReviewSchedule.getUserDate(x)))
    # Code for finding any reviews that are past due.

    late_users = []
    current_date = datetime.datetime.now()
    for user in review_users:
        schedule_date = datetime.datetime.strptime(ReviewSchedule.getUserDate(user), "%Y-%m-%d")
        if current_date > schedule_date:
            late_users.append(user)
            review_list.remove((user, ReviewSchedule.getUserDate(user)))

    late_reviews = []
    for x in late_users:
        late_reviews.append((x, ReviewSchedule.getUserDate(x)))

    schedule.html = HTMLTemplates.schedule_list()
    return template(schedule.html, date=current_date.strftime("%Y-%m-%d"), reviews=review_list,
                    late_reviews=late_reviews)


if __name__ == "__main__":
    run(host=hostName, port=serverPort, debug=True)

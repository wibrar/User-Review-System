# Deadline
* Our initial deadline for main project code was to be **Nov 30**. 
* However, since the professor moved the deadline of the project to Dec 10th, and then Dec 12th, we moved our final code deadline to be **Dec 4**.
* Documentation was okay to be submitted as  a pull request until the final deadline of **Dec 12**.
* Hypotheticals, as specified by Professor, were allowed up until **Dec 15**.(Update) **Hypotheticals are in a folder called Hypotheticals.**

# Where to Find
* The main project code is located in the main folder of the repository. This consists of:
  * **requirements.txt** - Located in the main project folder "term-project-teamA". Includes all the necessary packages to set up a virtual environment with the terminal command:  pip install -r requirements.txt
  * **HTMLTemplates.py** - A folder containing all of the templates for our HTML pages that Bottle uses.
  * **account.py** - The account module, which handles account management and creation. It contains the **Account** class and the  **Team** class.
  * **database.py** - The database module, which handles database management for the project. It contains the **Database** class.
  * **projectserver.py** - The main server module, which puts together all of the modules using the **Bottle Framework**.
  * **review.py** - The review module, which handles the creation and management of reviews. It contains the **Review** class, the **ReviewRating** class, the **ReviewSchedule** class, and the **ReviewComment** class.
* All documentation is in the **docs** folder of the project. This consists of:
  * **README.md** - The file that holds our README for project navigation and information.
  * **meetingNotes.md** - The file containing all of our meeting notes for all three sprints.
      * **NOTE**: For the meetingNotes, the history for this sprint can be seen in the commits of meetingNotes branch. They were only added to the master branch at the end of the sprint, but proof that they were updated throughout the sprint can be seen in the commits.
  * **performancereviews.md** - The file containing our performance reviews on the team and each other, conducted at the end of each sprint.
  * **processanalysismodel.pdf** - The file containing our process analysis model.
  * **ComponentArchitectureDocuments** - The folder containing all of our UML architecture documents.
    * The **microprocess architecture** document is also in this folder, called **Microprocess Architecture.md**
  * **Unit_Testing** - The folder containing all of our unit tests.
  * **TestFiles** - The folder containing any extra files needed for testing.
  * **SprintOneTwo_Archive** - The folder containing any archived files from sprint one and two, including user stories, older performance reviews and the old README file.
 
  * The group hypotheticals will be in a folder titled **Hypotheticals**.
 

  * **Code Reviews** Code reviews were performed in meetings; when this was done, it will be indicated in the meeting notes.
       * As well, code reviews were performed directly on pull requests as comments.
   
  * At the bottom of this README is a section called **User Reports**. If any team member felt that they wanted to explain more of their code and any difficulties they overcame while writing it, they will put it under here. This wasn't required of every group member. 

# How To Use
#### Virtual environment Setup instructions
* Once you have created and activated your virtual environment do the following:
* 1. In your command terminal type in the command:  pip install -r requirements.txt
* 2. After the package in the requirements text is installed with the above command, you can run the project from the terminal with the command: python projectserver.py
* The image below illustrates these steps.
#### Virtual environment Setup
![VenvSetup.png](ComponentArchitectureDocuments%2FUML_Diagrams%2FVenvSetup.png)

* After this last step you can follow the instructions below. 
* To open the server, run the projectserver.py file and go to http://localhost:8080/
* This will bring the user to the homepage of the site, where they can register, or log in.
* Press register, and input a username and password when prompted to create an account on the server. This will be saved in the Database.db file, so if you close the server and re-open it, the account will still exists. If the account already exists, you will be brought to a webpage with a “Username taken” message.
* If you already created an account, press log in and input your username and password if prompted. If the wrong credentials are put in, you will be taken to a page saying “Incorrect username/password.”
* Once you log in or register, you will be brought to the rough draft of the profile page. Here, you can “Go to Forum”, “Write a Review”, “Logout”, "Join a team" or "Create a Team".
  * **NEW** - Change Password - This brings you to a page where you can change your password.
  * **NEW** - This profile page will now also display the **team** you are on. To **create a team**, simply press the **Create a new team** button and input a team name. Then, back on the profile page, you can press **Join a team** and input the name of an existing team to join it.
* Starting with the simplest: Logout does exactly as it says, and logs you out of your account.
* Writing a Review brings you to a page with three things; a topic field, a content field, and several rating boxes. Here, you can write a review that will be automatically published to the forum once you hit save. Topic is for writing what the review is about; this can be a team member, a team, or something else. The content is where you write the review itself. The ratings are criteria you can rate the subject of the review about, from 1 to 10. Once you hit “Save Review”, this will bring you to the Forum page; this is also where the “Go to Forum” page brings you.
  * **NEW** - Now, once you are part of a team, you are limited to only writing reviews about your team members. This limits the field of topics, which makes it easier search for reviews about specific people.
  * If you are not part of a team, the topic field will display "You are not part of a Team", but still allow you to write a review with no topic.
* The forum is where published reviews live! Any written reviews will be published here for all users to see. They will be listed by the name of the username who wrote them, the topic, the content, and the rating. It will also automatically average the ratings given for each review to give an average rating out of 10 for each review.
  * **NEW** - A comment feature. On any written review, you can press **"Comment"** to be taken to a page where you can add a comment to a review.
  * **NEW** - You can view comments on reviews by pressing **"View Comments"** on a review on the forum page.
  * **NEW** - The **Edit** button allows you to edit a posted review. The **Delete** button allows you to delete a posted review.
* With the search review bar, you can choose to search reviews by: topic, author, or content. Each search supports partial match searching; i.e searching the content of each review for reviews that contain “pop” will return any review with content that contains “popcorn”.
* **NEW** A schedule feature. Pressing **"Go to scheduler"** on the Forum page will allow you to schedule a review for your teammates, using a built-int HTML calendar.
* **NEW** Scheduling a review will bring you to the **"Schedule"** page, where you can see the current date, any scheduled reviews, and any **late** reviews- scheduled reviews that are past due.
* Not yet in HTML, but possible through going to http://localhost:8080/sort is the sort feature. Going to this path will bring you to the forum page, but with the reviews sorted from the highest average score to the lowest average score.

# Features and Tasks
* This sprint, we decided on three new features to add:
  * A Team feature that would allow people to be put in teams. Team members would only be allowed to write reviews by each other, and be allowed to schedule reviews about each other.
  * A Comment feature, which would allow people to add comments to reviews.
  * A Schedule feature, which would allow you to schedule reviews that needed to be done in the future. You would only be able to schedule reviews for people on your team.
  * **NOTE**: In the meeting notes, an Anonymous feature was planned to be implemented, but this was later scrapped. 

* Early on in the sprint, as can be seen in the meeting notes for **Nov 16**, these features were split into tasks and assigned to each group member.
* These were also added to the KanBan board.
  * Jurez:
    * Create Schedule Class
    * Create Team Class
    * Refactor database and account classes to implement Teams and Schedule Class
    * Worked on HTML for Team pages
    * Implement Unit testing for Team class
    * Implement Unit testing for Schedule Class
  * Jenna:
    * Serverside (projectserver.py) Comments implementation
      * Involved creating three methods: scheduler_page, schedule, and schedule_list
    * Serverside (projectserver.py) Schedule implementation
      * Involved creating three methods: comment_post, add_comment, view_comments
    * Worked on HTML for the "Schedule" page and updated the "Comment" and "View Review" HTML to work with server
  * Pratik
    * Update project with CSS styling
    * HTML page to create scheduled reviews
    * Added buttons on Profile page to do various features, including changing password, and buttons on Forum page to edit and delete reviews
  * Wasif
    * Created Comment Class
    * Refactor Review class to implement comments
    * Created the HTML for "Comment" and "View Review" HTML.
  * **NOTE**: At first, we had assigned all HTML tasks to Pratik- however, near the middle of the sprint, we realised this was a lot to ask one person to do- so we all took over creating at least one HTML page for our implemented tasks.

# Unit Test
  * **Jenna's Unit Test** - projectserver.py
    * The Server Module unit test is done using POSTMAN API. The code given in the json file can be exported into a POSTMAN program, and then the GET and POST methods on the sidebar can be clicked so that the user can see how pages should look when the code is run correctly.

  * **Jurez's Unit Test** - testAccount.py, test_persis.py, testSchedules.py, TestTeams.py
      * Unit testing For Database 
        * Go the Unit_Testing folder, there is a file called test_persist.py. Simply click run. 
        
      * Unit testing for Account
        * In the same folder, there is a file called testAccount.py. Simply click run to execute.
      
      * Unit testing for Team
        * In the same folder, there is a file called testTeams.py. Simply click run to execute.
      
      * Unit testing for ReviewSchedule 
        * In the same folder, there is a file called testScheduler.py. Simply click run to execute.
        
    
  * Wasif's UNit Test - Review.py
    * Unit test for review class
      * Go to Unit testing file, open testreview.py. Click run button.
    * Unit test for Comment class
      * Go to Unit testing file, open testComment.py. Click run button.
       
          
 * pratik's unit test- htmlTemplates.py
    *location - folder unit testing , file name = final_unittesting _html.py
       * new method of html unit testing is using Selenium interface, the old has lot of limitation , this new code just specify and find a button or satement which is required for the page, i.e. it check what should be there for the page to pass the test.
   

 # USER REPORT

*task completed/user report :
 work done in branch 202060778-Pratik

 THE PROCESS:
 as we begin the sprint 3, each person was given their task and this time ,it was clear cut what a person need to do,
 so the communitcation between the team was getting better. i was given the task for CSS implementation , making a scheduler,
 unittesting for html , and some improvised task like making a dropdown menu, assigning reviews to teammates.

 as we discussed about this sprint task, the biggest problem i faced was communicating between the back end teammates , say i handle html part so i have to wait
 for them to finish their implement so i can add a front end html thing they desire. we came up with a solution that the person who want to implement in the html code ,
will provide a stub method and let me know so i can least be prepared.

but unfortunately, this solution was not the best , as my teammates have other deadline to follow too, including me as well , so i had a meeting the professor
about this issue, he told me some good idea to implement by code , how we can better our process and also helped implement the css code as it as a bottle framework so it require a static file to use and located, and then by the help of professor,

how we solved this issue

1) we decide to make some adjustment as for the css task, as it was done by me alone , so rather than making a chunky code with html and css in one file
it was better to just make a css file separate and just paste a link html which connect css and html, it made the code more sensible as if
a user want to add some button or anything in html template they can do it without implementing any css changes.

2)for the alternative solution we discussed the issue again and we came as we decided to held a meeting as soon as possible, where i present my html implement of making a-scheduler and guide jeena how i implement my code in person so he can work on its backend, and i will be 
on standby if she had something updated. then i help out jurez in making a dropdown menu. So to take the pressure from me we decide to each teammate will do at least one html of their own implementation. 

3)In the meeting with the prof , he also notice some limitation of html unit testing an provided me an alternate for the uni testing.
As the old way , if any of my teammate make some changes in html template it will result in uni testing failing , so with the help of prof , we decided to put a unit test which only check requirement item like the login page should have a login button and other page should have some test , I.e. the requirement of the page need to be checked rather than the whole page.

Where u can find my work;

1)CSS file = located in static folder

2)unit testing. = unit testing folder , file name = final_unittesting_html.py

3)Scheduler = u can find it in main htmltemplates.py , function called scheduler page

4)team drop down menu and assigning = find it in htmltemplates.py, function called write reviews.

OVERALL:

This sprint was a improvement on alll and little heavy on the task but we manage it by the deadline and worked our way through.
The css at the end make the project looked alive, as it make it looked more professional. we followed our process and make some adjustment while encountering some problem, thus we did fair bit off problem solving and learned more about this project and this course and how we work as. A team .

# "Hypotheticals- Submisions"
In this section if a group member felt it was necessary, they would have attached their
hypothetical submission to this section.

### Student Submission by Jurez:
Firstly I'm grateful towards Professor Brown and our T/A for making the neccesary ammendents
towards our grades. I think if our group had gotten sprint feed back submission sooner, we would
have invested significant more effort into making sure our sprint 3 activity was as visible as possible
in our sprint three submission. **I think the visibility of our Sprint2 activity was the biggest issue we encountered in our
feedback, but I understand why an issue like this can occur, as our evaluators have to process a large volume information from students and this
information is at times unorganize.**
Naturally, our documention of kanban board, meetings notes, and issue board
improved overtime as we progressed through the semester, however if we had realized this issue sooner
we would have made it our number one priority to make our activity as visible as possible through more organized 
documentation.
**Thus for clarity I decided it would be beneficial 
if I left a map for our evaluators to navigate through some of our sprint 3 activity.**

#### Pull request and Code review documentation
You will probably notice a few comments posted on specific pull request by me (Jurez) on the deadline night Dec 12, 2023.
These comment posts were my attempts to link each pull request to the original code review which was documented in
our meeting notes. The "Code Review" content was posted in its raw form and directly from the meeting notes, with no
changes, this was done to make navigating to our meeting notes more convenient **(by specifying the meeting note entry which documented the code review)**, and should not be intrepretted as a "last minute
code review" as this was not my intent. While in the process of doing this, I did realize that one of our code reviews were lacking,
in a case like this, I simply left an explanation, where necessary and made I no attempt "correct" these mistakes. I think this latter
point illustrate that my intent was not to "change/supplement" any code reviews, but to purely point our evaluators towards the
referencing meeting note entries. I ran out of time while doing this so the next subsection will hopefully clarify any visibility
issue related to our Sprint 3 activity. 

### Student Submission by Jenna:
For the most part, if given the Sprint 2 feedback, I would have focused more on improving our code reviews. I think for a lot of our Sprints, the code reviews were something we struggled with, and the feedback on our reviews from sprint 2 would have helped. I would have discussed with the team the things mentioned by the Professor, mainly applying more DRY and SOLID, and putting more effort into making sure everyone can attend code reviews. That way, we could all practice looking for examples- or lack of examples- of DRY and SOLID in the code, which would have helped us all get a greater understanding of these concepts.
As well, since we didn’t get any feedback for the Process Analysis Document due to error with the marking, I felt like I was unable to change or improve it. If I had the feedback from Sprint 2, I would have taken time with the team to go over this document so that we could add any improvements offered by the Professor.

## Sprint 3 Activity Map
I can't guarantee that this map is comprehensive, as I can only tell a story from my perspective, and I might not be aware
of all the issues my group members individually experienced, but the ones I am aware of I will document them here if they are
relevant to our evaluation scheme.
**All of our sprint 3 activity consists of PR#118 - #178, in terms of our code submissions and documentations.**
Changes after this point were related to our "Hypotheticals" document and were permitted by Professor Brown up to December 15th

##### Documentation relevant to Code Reviews and any issues arising from them and Raised Meeting Issues.
**This section is relevant to both the Team grading and Individual grading schemes**

PR #143- Meeting note entry: November 23rd

PR #146- Meeting note entry: November 27th

Meeting note entry: November 30th
Code review: PR #148
**(Team issue #1) - Code Review issue raised:** During Jenna code review we raised two issues, one was that team_page() method
had redunant code, and should be refactored (relevant to DRY). This was raised as issue #150 (kanban board) and later resolved in 
PR# 158  between code lines 373 -385 (These commits are somewhere between December 2nd to 4th). 

This code review also
raised **(Team issue #2)- code review**, a bug was spotted in the account module and tracked on kanban board as issue #153, this bug was later fixed in
PR # 159.

**(Team issue #3)- Meeting issue raised** : After our code review was conducted, I also raised the point that our HTML developer Pratik
needed assistance with implementing some of the HTML Pages. Reference to this discussion is documented in our Nov 30th 
entry. 
Issue resolution: Later on December 4th, Pr #158 and #159 sought to resolve this issue, Jenna and I assisted Pratik with these tasks, a 
code review was done directly on github. 

December 1st - This was a Friday, so we did our code reviews remotely and left comments on github.
Code Review: PR # 152 - Remote code review (there was no scheduled class), This code review was done directly
on github.

**(Team issue #4)- Code Review Issues raised**: We noted that Pratik's code submission (PR#152) likely violated the openness/closeness 
principle of the SOLID convention, and that we would have to make improvements later. 
Issue Resolution: This was documented on the kanban board as item #154 and then later fixed in Pull request # 159 and thus resolved this issue.

Pr # 156 - A code review was not applicable here, explanation given on git-hub. We simply verified that
project files were still functioning.

PR# 160 and PR#161 - These pull request were done directly on github. 
The pull requests after #161 were documentation related and are not relevant for code reviews.

Meeting note entry: December 10th **(Team issue #5)**
This issue was documented as issue #169 and our team resolved this issue by discussion on discord,
a summary of our discussion is seen on the Issue Board under item #169.
*

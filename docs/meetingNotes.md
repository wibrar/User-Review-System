# Meeting Notes

## Oct 3, 2023
**Recorded by:** Jenna 
**Notes submitted on:** Oct 12, 2023 
**SCRUM master:** Jurez
**Venue:** EN 2040
**Time:** 1:00pm to 1:50pm
**Attendance:** Jenna, Jurez

* Elected a note-taker and a SCRUM master for the future of the project
* Planned to use the routing mechanism for Bottle
* Made plans for keeping account info for site, and also for a "review" object

## Oct 4, 2023
**Recorded by:** Jenna
**Notes submitted on:**   
**SCRUM master:** Jurez
**Venue:** EN 2040
**Time:** 1:00pm to 1:50pm
**Attendance:** Jenna, Jurez, Wasif

* We planned out the preliminary things we will need to finish by Oct 20:
  * Three classes: Record Server, Account, Review/Post
  * Services we may need: Create Account, View Profile, Create Review, Modify Review, Publish
    * Also a "forum" which displays all published reviews (will later need a filter by topic)
  * Possible use "shelves" for persistence technology
* Responsibilities:
  * Jurez will work on the account class, and log in/log out service
  * Jenna will work on a "base" for the server and start the Review class
* Planned deadline: October 16 (monday before due date)
* Things to do:
  * plan out an idea of "code dependency" so that things don't become tangled or confusing later on
  * figure out unit testing for this project

## Oct 5, 2023
**Recorded by:** Jenna
**Notes submitted on:** Oct 12, 2023   
**SCRUM master:** Wasif
**Venue:** EN 2040
**Time:** 1:00pm to 1:50pm
**Attendance:** Jenna, Jurez, Wasif

* Agenda items from prof: setting up project issue tracker and KanBan board; set release cycle 1 schedule for final pull-requests, code reviews and performance reviews; draft the software process for the project, review the progress on defining service and module interfaces: the definitions should be stable soon.
* Team agenda items: Scrum-master adds project-and-team based agenda items; members suggest new agenda items
* Done:
  * Setting up KanBan Board

* Possible idea for setting up a database with a dictionary of account objects (password as key?) and an array of review objects.

* Notes from class:
Usual Service Pattern:
Server recognizes incoming HTTP request
Server checks user credentials (method call to the user package) (user module)
Server manipulates project structures via app logic module to process requests (some kind of an interface call to an app logic (like making calls to quiz.py) (app module)
(above in server module)
Server persists changes to project data structures (could be in app logic modules or through server module) ( separate persistent storage and object manipulation)
Compose an HTML page response based on what happened in 3,4 (interface for the module)
Put HTML response into a HTTP response and send it back to client. (really easy in Bottle)

2,3,4,5 involve interface call to other modules

## Oct 12, 2023
**Recorded by:** Jurez
**Notes submitted on:** Oct 12, 2023 
**SCRUM master:** Pratik
**Venue:** EN 2040
**Time:** 1:00pm to 1:50pm
**Attendance:** Jenna, Jurez, Pratik

* Team Agenda: Project Status

* Agenda items: Issues while developing assigned tasks, Kanboard refinement & Project Issues refinement,
* Reviewed Assignment Rubric.

* Meeting Notes:
We thoroughly reviewed the Assignment rubric released in class today.
We used this insight from the review to recalibrate the future progression of our project.
We discussed issues we encountered during development and recommended suggestions.
We proposed a date to meet up and work on our parts in a group session: October 16 after class.
The group decided that our kanboard and project issue needed to be updated.

* Done:
Kanboard reformatted and labels added.
Project Issues implemented in team repository. 

## Oct 17, 2023
**Recorded by:** Jenna 
**Notes submitted on:** Oct 17, 2023   
**SCRUM master:** Jenna
**Venue:** EN 2040
**Time:** 1:00pm to 1:45pm
**Attendance:** Jenna, Wasif, Pratik, Jurez

* Team Agenda: Project Status

* Agenda Items: Detailing progress;  what will be ready for first sprint and what won't be?

* There was difficulties implementing the "log out" method from the user module into the server module
  * Resolved for the most part- need to implement "persistence" for the current user during server runtime

* What is done:
  * The user (account) module
  * The database system
  * The HTML templates

* What is being worked on:
  * The app logic (review module)
  * Server module (still needs to add app logic functionality)

* To do:
* Mostly documentation:
  * README file 
  * Code reviews
  * User stories
  * Feature suggestions
  * Docstrings for server module
  * Performance Review file (?)
    * A txt file to contain the team's performance reviews so that it is easy for the marker to find them

* What won't be done for first sprint:
  * Unit testing

* What to do in the future:
  * Unit testing for each module (user, app logic and server) will need to be added for the second sprint.
  * Come up with more "checkpoints" so that the team does not end up behind on progress for future sprints
    * Multiple shorter deadlines instead of one large one

* Started the README file so that it could be ready for the submission date of Friday night.

* Set a deadline of WEDNESDAY, OCT 18 (MIDNIGHT) so that there can be a final discussion in class on Thursday.

## Oct 18, 2023
**Recorded by:** Jurez
**Notes submitted on:** Oct 19, 2023   
**SCRUM master:** Wasif
**Venue:** Library
**Time:** 12:45 to 1:45 pm
**Attendance:** Jenna, Jurez, Pratik, Wasif

* Next Sprint
  * Update server to implement HTML pages (using classes instead of templates)
  * Filter by topic feature
  * Unit test
  * Wrap server into a class (object oriented method?)
  * 
* Things we can still work on
  * Implementing HTML pages to server

* Things left to implement
  * Draft review
  * Publish review
  * Filter by topic

* Group decided unit test was unlikely to be done by end of sprint.

## Oct 19, 2023
**Recorded by:** Jenna
**Notes submitted on:** Oct 19, 2023   
**SCRUM master:** Jurez
**Venue:** EN 2040
**Time:** 1:00pm to 1:45pm
**Attendance:** Jenna, Jurez

* Meeting agenda: final clean-up, code and performance reviews, documentation for end of sprint.

* Performed Code Review on Account.py and Database.py
  * Jurez explained how the class works, including methods, initialization, parameters, etc.
  * Including STUB methods that depend on the Review Class.
  * Database code needs to be updated to "remember" accounts created in different sessions.(resolved)
* Performed Code Review on projectserver.py
  * Jenna explained how the server works, including methods, initialization, parameters, etc
  * Including STUB pages for classes that haven't been implemented yet

  * Logout service still not working- (resolved)
    * Possible option is to move to the object-oriented version of Bottle instead, for the purpose of using class variables.
    * In its current state the User variable in the server is a global variable, so the log-out service function
    * can't reassign a null value to the user variable due name shadowing. (this issue was resolved)
  
* Unit Testing push to next Sprint:
  * Unfortunately we were not able to implement unit testing. This is primarily because of 
  * none of our group members knew how to create one. Our collective prior experience for unit testing,
  * as a group was simply how to pass a unit test. A great instructional video  was released on 
  * how to do unit testing on October 16, however as with most new concepts there is a learning curve,
  * and we were not able to confidently synchronize learning this new concept across four team members
  * under this short time period. Further compounding our issue was that by the 16th each team member
  * were all preoccupied with midterm exams and other responsibilities for other courses. By October 16th
  * we informally realized that this technology would most likely not be implemented under these conditions and
  * we did not want to put ourselves in the position of trying to implement this technology at the last second
  * before the deadline, as rushing invites mistakes. So we realistically just pushed implementing this technology
  * in the next sprint.


## Oct 26, 2023
**Recorded by:** Jenna
**Notes submitted on:** Oct 26, 2023
**SCRUM master:** Jurez
**Venue:** EN 2040
**Time:** 1:00pm to 1:45pm
**Attendance:** Jenna, Jurez

* Meeting agenda items for consideration: identify team tasks for 2nd sprint; identify tasks still not completed from sprint 1; identify features for 2nd sprint; decompose features into coding tasks; try to identify possible interface revisions required for coding tasks 
* assign design and coding tasks for 2nd sprint and set deadlines for activities, especially pull request deadline for final sprint submissions.

* Since last meeting, Jurez has fixed bugs in database, and touched up the Review Class.
* Each team member will take responsibility for the unit test for their own module:
  * Jurez will do the Database unit test
  * Pratik will do the Account unit test
  * Wasif will do the Review unit test
  * Jenna will do the Server unit test/API test

* Goals for this sprint:
  * Implement object mapping for HTML pages 
  * Unit testing
  * Finish implementing Forum page and functionality
  * Session Management
  * Search Review function
    * New page/add to Forum page?
  * Review rating function
  * Profile page in Server Module
  * Edit Review / Delete Review in Review module
  * Change password in Account module

* Jurez Tasks:
  * Unit testing for database
  * Implement user story (changing password)
  * Debug the Review class (with Wasif)

* Jenna Tasks:
  * Unit testing/API testing for Server module
  * Implement editing a review
  * Review rating function

* Pratik Tasks:
  * Unit testing for Account module

* Wasif Tasks:
  * Finish Review class
  * Unit testing for Review module

* One option for session management is to refactor the Server module into an Object Oriented module; consider this for the future
* Clean up the master branch- it's very disorganized right now (with many unnecessary files)

* Mini deadline for Monday, Oct  30:
  * Finish everything from first sprint
    * Review class, Forum page (Search by topic), Unit Testing(if you can)
  * Debug together, do code reviews
  * Finish delegating tasks for second sprint

* Future Deadlines: November 6th
  * New features should be complete
  * Debug whole project, do code reviews, maybe performance reviews
  * Discuss features to add to backlog (User stories)

* Final deadline of November 8th
  * Plan meeting for this day (attendance REQUIRED!!!!) 
  * All debugging should be complete
  * Everything should be submitted (through pull requests)
  * All reviews done
  * Updated README

## October 30/10/2023
**Recorded by:** Jurez
**Notes submitted on:** Oct 30, 2023   
**SCRUM master:** Pratik
**Venue:** Library
**Time:** 12:45 to 1:45 pm
**Attendance:** Jenna, Jurez, Pratik, Wasif

* Agenda items: Unit testing, debugging sprint one features, update kanboard, removing file clutter


* Performed code review on  HTML Templates.py
  * All the previous html pages were combined into one python file, and duplicate pages were 
  * subsequently removed.

* We decided to push our unit testing deadline to November 2nd

* Discussed refactoring the update_review service to use the newly created review class,
  * we noted that the update_review method should decouple the review class logic from
  * the server and into the review class module.

* Kanboard board was updated to reflect the current state of the project.

* Done: 
  * Kanban board updated.
  * File cluttering resolved, and html pages added into one file.

## Nov 2, 2023
**Recorded by:** Jenna
**Notes submitted on:** Nov 2, 2023
**SCRUM master:** Wasif
**Venue:** EN 2040 (during class time)
**Time:** 1:00pm to 1:50pm
**Attendance:** Jenna, Jurez, Wasif, Pratik


* Professor’s suggestions for Agenda: review feedback from sprint 1; what changes are needed to process model and team activities?


* We seriously discussed the feedback from the last sprint, in order to improve our process for this next sprint.
 * As a note, most of this was done through online discussion directly after grades were released; but they're being noted here for clarity for the professor
   * Overall, the bad grade was hard but not entirely unexpected. We realized that major changes need to be made before the deadline for Sprint 2 to pave a better path for the project.
 * First: Meetings
   * It's clear that attendance to meetings needs to be improved. The plan for now is for all of us to share our schedules over the next few days, and then to plan our meetings around these so that everyone can be at every meeting.
     * Right now, attendance to meetings is unacceptable- only half the group is showing up to the class-time meetings. This will seriously harm the future of the project and needs to be fixed ASAP.
     * The possibility of having more, short online meetings was brought up- the idea is to have "check-ups" so that we can see where everyone is and make sure everyone is clear on what needs to be done.
       * I.E. a short, 30 minute online meeting is better than no meetings at all!
 * Second: Code Reviews and Performance Reviews
   * We were not clear on where our code reviews were located, and even then, it's evident that our code reviews were very lacking anyway.
     * This was discussed with professor in class time; see below for our new process involving code reviews.
   * Based on feedback, our performance reviews were extremely lacking and not transparent enough. Near the end of the sprint, everyone should take serious time to write a transparent review with their feelings about the project, and give an honest rating on how they feel we handled this project.
     * We decided that each of us would give every other team member a rating, 1-10, based on each of the criteria given in the assignment 2 notes. For clarity, these criteria are:
       * Effort expended on topic
       * Communication with team
       * Participation in critical reviews
       * Attending team meetings
     * As well, a short paragraph on the performance of the team overall should be expected from each member as well.
   * Third: User stories
     * Clearly, we all missed the expected way to write these. User stories for future sprints should be written in the format given by Professor, and should CLEARLY define a feature that could be added to the project
       * As well, once a user story is written, be sure to add this feature to the KanBan board under the backlog- and we will discuss implementing these features together in meetings!
   * Four: README
     * It's clear based on feedback that the README file needs a big revamp.
     * It should include basically every detail on the project, including who did that
     * As well, it should include CLEAR instructions on how to use code, as well as how to find and run unit tests
 



* Before, we assigned unit test tasks based on the notion that it was not needed to implement an HTML unit test;
 * Pratik was assigned the account unit test, Wasif was assigned the review unit test, Jurez was assigned the database unit test, and Jenna was assigned the POSTMAN API for server module
 * However, on re-reading the notes, we have realized that there is a proper HTML test that we have missed, and we will be implementing this as soon as possible. The plan for now is for Pratik to work on this with help from Jurez if needed.
 * We also decided that, once completed, unit tests will be stored in a "tests" folder.
   * Each person will be **responsible** for documenting WHERE to find and HOW to use the unit test they created; this should also be shared with other team members in CODE REVIEWS that will be documented in meeting notes.


* Discussed code reviews and process model analysis with professor
 * RE: Code reviews
   * Code reviews will be done in this manner: The person who wrote the code will explain it to the rest of the team, and then other members can ask any questions/clarifications they may have
   * These code reviews will be documented in team minutes.
   * As well, a part of these code reviews will be seeing if all of our code matches the SOLID model given by the Professor.
 * RE: Process Model Analysis
   * This should be a **clear** overview of how we handled this project, including:
     * who handled pull requests
     * deadlines
     * more info will be given by professor near end of next week


* In order to make sure that deadlines are met, Jenna made a hard deadline of Tuesday, November 7th.
 * After this day, **no major code-related pull requests** will be accepted into the master branch.
 * However, any small changes or clarifications to the documentation should be fine, since we still need to add meeting notes, user stories, reviews and the like.


* Planned the UML architecture for submission as a team, worked on it together by following the chart and deciding which parts of the project correlate to what on the given example of UML architecture.
* Discussed another method for indexing reviews to make them easier to find
* Jurez pointed out that a GET method may be needed for the edit review method in order to make it work, as it is still returning an error


* The professor also clarified that this course is about "Process over Product", and I think we should remember that going forward.
 * It's okay to have problems and not meet deadlines, as long as we DISCUSS and DOCUMENT all of this.

## Nov 3, 2023
**Recorded by:** Wasif
**Notes submitted on:** Nov 3, 2023
**SCRUM master:** Jenna
**Venue:** Library
**Time:** 11:00 - 11:55am
**Attendance:** Jenna, Jurez, Wasif
**Note:** Pratik had work, so he was not able to come today. He told us that he will be able to meet in the meeting tomorrow.

* Updating the Kanban Board to remove all the bugs to assign tasks
* Wasif will do Delete function
* Jenna will do search by Topic function
* We all looked into our individual feedback and diccussed where we lost marks
* Jenna and Jurez helped wasif with unit testing.

## Nov 4, 2023
**Recorded by:** Jenna
**Notes submitted on:** Nov 4, 2023
**SCRUM master:** Pratik
**Venue:** Library
**Time:** 11:00 - 11:55am
**Attendance:** Jenna, Wasif, Pratik
**Note:** Jurez was unable to attend due to work; this was noted when the meeting was planned.

* We caught Pratik up on the things that were discussed yesterday, and informed him of his assigned tasks on the KanBan board. 
* Once again, the deadline of Tuesday for any code-related pull requests was noted. 
  * The idea is to have all the code done by Monday, so we can spend the rest of the week before the deadline focusing on documentation.
  * We discussed moving marks from Sprint 1 to the Final Sprint, and everyone agreed with this.
* We decided that on Monday, the four of us would go over the marking rubric for Sprint 2 to make sure that we were meeting every criteria.
* A new pull request process was discussed after the meeting yesterday, and Jurez added this to the README file.
    * *When ever a group member is ready to make a pull request involving coding we will
    * adhere to the following pattern (as of November 3rd).
      1. Explain what task progress is being made towards
      2. Explain how the code works
      3. Allow time for Team members participate by conducting code reviews based on
          the SOLID and any other relevant design principles before the merge.
      4. If anyone spots an issue/ room for improvement we will to document
          this in the issues table/ kan ban board backlog. If a project-breaking
          issue is spotted, we will close the request.
      5. Finally, the pull request is merge.
      * Note: This protocol does not apply to pull request involving updating meeting notes or documentation notes.

* When looking over the rubric for the past assignment, we noticed that we hadn't been marking our task progress in the meeting notes.
  * This is important for marking. A new procedure should be followed: we should each take a few minutes at the beginning of every meeting
  * to update each other on where we are with the code.
    * As well, we can mention in our README that the pull requests were how we were monitoring task progress until this point.

* It was noted that the "Filter by Topic" task on the kanban board previously assigned to Jenna was more of an HTML task,
* so it was re-assigned to Pratik.

* We discussed unit testing and how to do it, and also reiterated that it was most important that the unit tests worked, and not that
* every test passed (for now)
  * Jenna also reminded everyone to write a "how-to" guide for their unit test to be added to the README, and perhaps to a text file in the testing folder.

* We went over the user stories again, and reviewed the proper format for them as given in the class notes.
  * Jenna also reminded everyone that, once their user story was done, the feature that is created by it should be added to the backlog of the kanban board.

* Found a new issue: the Database needs to be created everytime the server is started, which causes PyCharm to get a lot of errors.
  * This was noted and added to the Kanban Board.

* We noted that we should ask the Professor questions in class on monday, mostly related to the architecture diagram, the process analysis diagram, and code reviews.
* We all agreed to meet up again on Monday during the class time.

## Nov 6, 2023
**Recorded by:** pratik
**Notes submitted on:** Nov 6, 2023
**SCRUM master:** wasif
**Venue:** class
**Time:** 1-1:50 pm
**Attendance:** Jenna, Wasif, jenna

Jenna completed the feature rating and search review functionality. Wasif tackled the edit review task but faced issues with HTML parameters for content and topic. He successfully completed the delete functionality. Jurez focused on the UML architecture and also studied the material for the process analysis model. Pratik worked on the HTML aspects of the project.

During the code review session for the Search Review and Rating feature, it was noticed that the search function is currently case-sensitive, making it somewhat awkward to use. This issue was added to the kanban board for future attention.

Wasif proposed the idea of creating a "test pack" for the grader, containing pre-made reviews and accounts for easy use. This suggestion was also added to the Kanban board.

The team discussed the concept of making the "edit" and future "delete" buttons user-specific for reviews, meaning individuals would only see these options for the reviews they created. It was agreed to implement this change in the next sprint, and the task was added to the backlog.

Additionally, the team acknowledged the need for clear assignment of tasks to avoid confusion. They decided to clearly state who is responsible for each task to provide clarity for the Professor.

## Nov 7, 2023
**Recorded by:** Jurez
**Notes submitted on:** Nov 8, 2023
**SCRUM master:** Jenna
**Venue:** EN 2040 (during class time)
**Time:** 1:00pm to 1:50pm
**Attendance:** Jenna, Jurez

* Agenda Items : Code Reviews, Kanban Board Updates, Task Delegation Clarity, MVC Patterns

* Code Reviews and Pull Request Process:
* Previously (on Nov 3rd) the group adopted a Pull request model in which the person opening the pull request
* would explain what task progress is being made towards, and how their implementation works. This would allow for
* more efficient code reviews. 
  * Jenna's Pull Request: Status: Merged
    * We took note that adding ReviewRating class to review module was a good example
      * of cohesion - keeping related code in the appropriate modules.
    * We also noted that SRP principle was adhered to as the changes needed to implement
      * search review feature were distributed to their relevant modules, for example
      * the necessary code changes were made in the HTML module, review module, and server module 
      * as opposed to attempting implement all the code in one location.
    * Thus, in general we concluded that the added code did not break any of the SOLID conventions.
  * Pratik's Pull Request: Status: Pending (Will most likely be closed)
   * Note: Unfortunately we were not able to merge this pull request, because the branch
     * still had conflicting files from a previously closed request. We consulted with the professor
     * to see if we were allowed to create new branches to resolve this issue, and Professor Brown 
     * informed us that it was okay for us to create new branches, as long as we don't delete any preexisting ones.
   * Even though this pull request will be closed, we noted that there was a html page for the change password feature,
   * and unit-testing for the HTML pages. 
  * Jurez's Pull Request (Conducted after meeting):
    * The code review for this pull request was done after class remotely on discord, as we had ran out of class time.
    * The summary of our discussion was posted in a comment on the pull request. However, key points were:
      * The SOLID conventions were adhered to, Any changes needed to implement a feature were
        * distributed to their relevant modules, this is in keeping with SRP and cohesion principle. 
        * The Open/close principle was also adhered to. 
        * For full details the code review was conducting on the pull request.
* The Kanban Board and Issues listing was updated to relfect the current state of the project:
  * Kanban Board Changes related to today's Pull Request:
    * The Following were added to Done
      * Session Management task (labels :coding task, feature ), Assignee: Jurez
      * Sorting Reviews (coding task) Assignee: Jenna
  * Kanban Board Maintenance:
    * This relates to any missed items that were not updated from previous pull request.
    * The following were added to Done :
      * Retrieve and modify a draft review (coding task) Assignee: Jurez

* Task Delegation Clarity:
  * In our meeting notes on November 6, we noted an issue we were having over confusion
  * as to which group member should be implementing which task. We identified that a frequent
  * source of this confusion was through helping other group member implement their interface.
  * In the previous Sprint I, we encountered issues with task deadlines being met, so in response to
  * this issue, in this Sprint II we opted in for offering more assistance to group members who may
  * have struggled with implementing their interface. 
  * While there is nothing wrong with helping our group members with their tasks, we still 
  * acknowledge that this may cause a lack of transparency to our markers when they have to evaluate
  * our project. To alleviate this confusion, we will document the extent of any help offered to a group members
  * tasks.
  * We will further deliberate on the best approach to this issue at the beginning of our next
  * sprint.
* MVC patterns:
  * There was no time to discuss this in class, however we will discuss implementing the
  * relevant design patterns that may enhance our project in the next sprint. 

## Nov 9, 2023
**Recorded by:** Jenna
**Notes submitted on:** Nov 9, 2023
**SCRUM master:** Pratik
**Venue:** EN 2040 (during class time), Library
**Time:** 1:00pm to 3:00pm
**Attendance:** Jenna, Jurez, Pratik, Wasif

* Task Progress:
  * We fixed things that had been accidentally deleted or lost during pull requests.
  * Jurez worked on the UML architecture, and is planning to have it done by Friday afternoon
  * Jenna started on the updated README and discussed her plans for the process analysis model. She will have a rough draft by tonight, and then share it with the group for feedback.
    * for the README: we decided that each team member should be responsible for adding the tasks they did to the readme.
* The last meeting before the submission deadline. 
* We discussed task assignments, and went through the KanBan board to make sure that everything was correctly assigned to who did it
  * Or whoever was planning on doing it.
* We discussed the Filter by Topic feature, and decided that it was redundant because the way we would have implemented it was pretty much exactly the same as the Search Review feature.

* Discussed the issues with our pull request process, because things are getting deleted, or pull requests are having to be rejected because of too many conflicts.
  * Before a feature is worked on, your branch should be updated to match the newest version of the master branch to avoid any conflicts.

* Jurez helped Pratik with this process, so that there wouldn't be future issues with pull requests.
* We decided to have an extended meeting today, in order to finish any loose threads before the deadline. 

* We discussed what was left for Friday:
  * Our documentation, including performance reviews,
  * Professor said that user stories were not needed for this sprint
* We extended our meeting and went to the library to help Wasif with his code
* We discussed with the professor the format needed for the Process Analysis Model; he clarified that it should essentially be 3 models:
  * One for the past process, one for the current process, and one for the future process.

## Nov 14, 2023
**Recorded by:** Jenna
**Notes submitted on:** Nov 14, 2023
**SCRUM master:** Pratik
**Venue:** EN 2040 (during class time),
**Time:** 1:00pm to 1:50pm
**Attendance:** Jenna, Pratik

* Agenda Items suggested by prof: Discuss the assignment description for sprint 3. Discuss incomplete tasks left over from sprint 2. Beginning of sprint decisions: define tasks and features to be completed this sprint; set deadline for final pull re-quests; divide features into implementation tasks; preliminary assignment of tasks to team members.
* We looked over the assignment description for sprint 3.
* Since some team members weren't able to make it today, Jenna and Pratik discusses some features that could be implemented, with plans to narrow down the list and discuss with the others on Thursday:
  * Implementing the schedule
    * Pros: good feature that would involve a lot of code, Cons: could take a while, may not be possible to complete in two weeks time
  * CSS idea given by Wasif in previous meetings
  * A comment feature for commenting on reviews
  * Maybe implementing time/date into our reviews
  * Posting reviews anonymously 

## Nov 16, 2023
**Recorded by:** Jurez
**Notes submitted on:** Nov 14, 2023
**SCRUM master:** Jenna
**Venue:** EN 2040 (during class time),
**Time:** 1:00pm to 1:50pm
**Attendance:** Jenna, Pratik, Jurez

* Agenda Items : Debugging Task, Decompose New Sprint Features into Task,  Assign Task, Implement Deadlines
  * New Sprint Features and their Decompositions: 
    * Comment under a Performance Review
      * Requires Server Side service (design task) assignee:  Jenna
      * Review Class must be refactored to add a container 
         to store all comments (coding task) assignee: Wasif
      * Comment Class to be added to review module (design task) assignee: Wasif
      * HTML forum page be refactored to include "view comments" button (coding task) assignee: Pratik
    * Anonymous Post
      * Requires minimal changes, is simply a 
        string "anonymous" to be added to menu of available topics/users (coding task) assignee:
    * Schedule Class
      * Refactor Review to include instance variable to record date (coding tasks) assignee: Wasif
      * Create Schedule Class (design tasks) assignee: Jurez
        * That assigns a date for each user's performance review
        * Refactor database to save/load schedule object (coding tasks) assignee: Jurez
        * Server Side method to assign date to a particular user (design task) assignee: Jenna
          ----> Should create a "schedule" object. 
        * Html button to assign date to each user (coding task) assignee: Pratik
    * Team Class:
      * Account class should be refactored to include instance variable for team (coding task) assignee: Jurez
      * Team Class (design task) assignee: Jurez
        * Each user will be a part of a "team", user must be on same team to make a performance review
          on a specific person. 
        * Database load/save refactored to store new object (coding task) assignee: Jurez
        * Relevant server side services should be refactored to enforce commenting constraint (coding task) assignee: Jenna
  
    * KanbanBoard Updates: 
        * Kanban board was updated to include all the tasks mentioned above. 
  
    * Debugging:
      * There is a bug on the forum page that displays the topic and comment twice
      * The change Password button needs to be added back into our html pages

  * Deadlines:
    * All worked should be submitted by November 27th (soft deadline), 
    * Time will be allowed for debugging up to the November 30th, but all work must absolutely be
      * in by this date as we will have exams the next for our other courses  (hard deadline).

## Nov 21, 2023
**Recorded by:** Jenna
**Notes submitted on:** Nov 21, 2023
**SCRUM master:** Jurez
**Venue:** EN 2040 (during class time),
**Time:** 1:00pm to 1:50pm
**Attendance:** Jenna, Jurez, Wasif

  * Due to there not being a lot of time between the meeting today and the one yesterday, we didn't have much to update each other on in the meeting today
  * We re-iterated our plans to have some code to review with each other for our in-class meeting on Thursday.
  * We looked over the Kanban Board that Jurez updated the night before to make sure that we all agreed with the tasks assigned to us
  * Since we didn't have any code to review, we instead looked over the rubric to see if there was anything that there was missing

  * After the meeting yesterday, Jurez and Wasif had worked on code together to get it ready to be pulled into the main branch without conflicts
  * Wasif planned to make the pull request; since we were missing a team member, we opted to do the code reviews separately in the comments of the pull request, so that everyone could participate instead of leaving someone out.
    * There were some issues with implementing this code today- the "Change Password" feature we were trying to implement wasn't working correctly and needs to be debugged more

  * The Schedule Feature- Jurez found a way to implement this using HTML, and shared with the rest of the group in the chat.

  * Other than that, we used the class time to work on code together and to discuss ideas for how to implement things.

  * Future Plans: Jenna will review the video on micro-architectures that the professor gave us, and will try to have a rough draft of it ready for the next meeting. Then the team can look it over and she can explain it, so the entire team can see what it is and discuss any issues they have with it
  * Things to update: Unit tests, UML (since we are planning to add new classes)
    * Maybe process analysis model document - need to ask Professor
    * These were added to the Kanban Board
  * We discussed this with him - we agreed that if we got our marks back and had to fix things, we would modify the deadline as needed.
  * The Professor re-iterated that we have to follow the deadline- which we've set as Nov 30th
    * We also agreed that we should document anything that we can in order to make our process during this project very clear
  * As well, we plan to do a code review on Thursday with anyone who has code ready to present.
    * The plan is to review the code as a group using pull requests, and then merge the pull requests as long as everyone agrees that the code is good to go

## Nov 23, 2023
**Recorded by:** Jurez
**Notes submitted on:** Nov 21, 2023
**SCRUM master:** Jenna
**Venue:** EN 2040 (during class time),
**Time:** 1:00pm to 1:50pm
**Attendance:** Jenna, Prahtik, Wasif


### Agenda : Code Review for Wasif's Pull Request

* This  pull request included the features wasif implemented in sprint 2, initially we could not merge
* the work in because it had conflicts with the master branch, and the code submission had exceeded our
* previous internal deadline for sprint 2. The group work together to resolve the merge conflicts in the days 
* prior to Nov 23 and we used this meeting to conduct a code review.

# Feature's implemented in this code review:
* Unit Testing for Review Module: We simply noted that all the tests were passing as the SOLID Principles were not
  applicable to unit testing
* Edit_Review (Server Side): The group discussed whether this particular feature violated SRP of the SOLID convention, the initial
  concern raised was that it introduced to many lines of code on the project server. However, we eventually came to an
  agreement that the implementation of this function was appropriate and did not violate SRP, because we realized that
  the implementation of this feature used the minimum amount of lines possible to achieve the tasks, editing review object
  involved changes to a variety of instance fields, as it get the web application user the ability to change any aspect
  of their review post, so naturally this introduced multiple lines of code. Furthermore, we realized that there was
  no need to add an additional method to the review class, because pre-existing review method were utilized to implement
  this service. So in conclusion, we agreed that this feature did not break any of the SOLID conventions.
  * Delete Review (Server Side) and remove_Review(review module): We noted that this implementation  was good application of
  using the open/closed principle. The changes to implement this new feature was distributed across the relevant modules, as opposed
  to be implemented in one module. Additionally, this also sticks to the SRP convention as well, as no class is being forced to
  take on an additional responsibility.
  * Update Review (bug fix): We noted that a "get method" was added to complete this service.
  
  # Bug Fixes included in this Pull Request
  *   The change password button was added back into the relevant html page, update_review
  
  # Overall Functionality
  *  We noted that no new bugs were introduced with this pull request, and the project server was still functioning at the
    time of the submission of this project.
  
  # Kanban Board Updates:
    * All of Wasif's tasks from sprint 2 were added to the "complete" column
      * This includes: #54 unittest for app logic, #84 delete post/review, and #74 update_review
  
  After merging this pull request, all group members were reminded to update their master branch and to merge in the
  changes into their work branches. 

## Nov 27, 2023
**Recorded by:** Jenna
**Notes submitted on:** Nov 27, 2023
**SCRUM master:** Jurez
**Venue:** EN 2040 (during class time),
**Time:** 1:00pm to 1:50pm
**Attendance:** Jenna, Jurez, Wasif, Pratik

* Professor noted that the deadline for this project would be extended, likely to December 10th, and that we could extend our own deadlines if needed.
  * Jurez and Jenna discussed pushing the coding deadline ahead in light of this; possibly to Dec 4th.
    * The current plan is to have all our code pushed by Monday, and then have a meeting on Monday to debug/finalize the code.
  * Once Wasif and Pratik arrived, we discussed this with them and they agreed on moving it to the 4th.
    * Since the first deadlines we established were based on the original project deadline of Dec 4th, we decided that it made sense to push our deadline forward since the project deadline had also been moved forward.
  * It would be a good opportunity to have more time to work on the project and clean it up.

* Jurez presented his pull reqest, which added the Team Class and the Review Schedule Class. Jenna and Jurez looked it over and found no conflicts. The other two weren't present for the code review.
  * Ideally everyone would be present for the code review, but due to the deadline approaching we decided to push it so that Jenna could work on implementing it into the server module.
  * More in-depth comments on code will be in the pull requests as decided earlier in sprint.
  * Once Pratik and Wasif arrived, they were also informed of the pull request and did a review of the code.

* Jenna showed her base idea for the microservices architecture- but due to the professor having not uploaded his example diagram yet, progress on this was paused for now.
  * It's planned to be finished by the end of the week, as work for other classes will be done by then and there will be time to work on it.

* A reminder was given that if the group wanted their personal scores from Sprint 1 moves to Sprint 3, they have to email the Professor before the last day of classes.

* We realized the meeting notes that had been recorded for the last meeting were not present; this will be fixed as soon as possible.
  * Jurez has the notes written, and just needs to add them to the file.

* Jurez gave an explanation of how he envisioned the schedule being implemented in the HTML for Pratik.
  * There was some problems with understanding how to do this, but the group discussed it and figured out a plan that should work.

* We notified the others in the team to update their branches after every pull request in order to avoid merging conflicts in the future.
* Jenna proposed the idea of reformatting the README as a .md file in order to give it easier to read formatting, since the README for the last sprint was a giant block of text that might be hard to parse.

* Pratik told us that he wouldn't be able to make the planned Thursday meeting due to conflicting responsibilities.
* We planned a future meeting for Monday, Dec 4th. 



## Nov 30, 2023
**Recorded by:** Jurez
**Notes submitted on:** Nov 27, 2023
**SCRUM master:** Jenna
**Venue:** EN 2040 (during class time),
**Time:** 1:00pm to 1:50pm
**Attendance:** Jenna, Jurez

* Agenda Items: Code Review for Jenna and Pull Request, Discussed Requirements.txt, HTML Page Assistance

## Requirements.txt
  * We reviewed the course notes pertaining to creating a Requirements.txt and
    * designated an assignee for this task.
    
* Assignee: Jurez

## Jenna's Code Review
  * Applicable SOLID Principles:
    All the task's implemented by Jenna were confined to the project server module, and any changes
      to pre-existing services only extended the functionality of those services. This was an example of the
      SRP and Open/Closeness principles of SOLID, and these were the only design principles found applicable
      from the SOLID convention within the context of this code review. 
  * New Features:
    * Jenna explained the functionality of each of her new services, we noted that we would have to complete
      their corresponding HTML pages first before we can actually test their functionality. We also noted that
      the Team Page function can be refactored to use the list returned from the Team Class, this was added to the
      kanban board under #150 issue.
  * Other Changes: 
    * We noted in general we should refactor some of the old features from the first sprint that were no longer needed,
    * after sprint 2 we included functionality for sessions management, so we noticed that there were still a few places
    * where session management needed to be applied. 
    * Jenna noted that Account module printed an error message to console even though the exception is caught,
      * so this issue will also be fixed as was documented as #153.

## HTML Page Assistance
  * After our group discussion on Nov 27, we realized that there was issue fully visualizing what final product
    * would look like. To resolve this conflict we offered our HTML developer Pratik assistance with developing 
    * some of the HTML pages in our class session on Tuesday. We realized that the work load of Designing/Refactoring
    * HTML pages has a tendency to scale up quickly as it on the Frontend side of the application, so any new feature
    * that is created in a given sprint might introduce additional work in that module. In our previous sprint
    * we experienced major issues with too many developers working on the HTML pages and synchronizing the work of 
    * their collective pages, so we made it a sprint goal for each developer to work on their designated modules. But
    * due to the large work-load in the HTML module, we realized that it would be unfair to leave this work to one person, so
    * we will offer assistance in an organized fashion to resolve this issue, and to keep the project on track with
    * the final product's vision.

## Kanban Board updates:
  * Requirements.txt added as task to kanban board
  * Jenna Tasks on the kanboard were linked to her pull request, and these tasks were closed/ added to
    * "Done" section
  * During the code review process we noticed, that we had to refactor some old features from the 
  * project's first sprint and some other minor code changes, these were added to the kanban board as
    * issue #151 and #150, #153 one was added to the Todo Label, and the other under Code Review Suggestion.

## Dec 5, 2023
**Recorded by:** Jenna
**Notes submitted on:** Dec 11, 2023
**SCRUM master:** Jurez
**Venue:** Online (Discord)
**Time:** 1:00pm to 2:00pm
**Attendance:** Jenna, Jurez, Wasif, Pratik

* We had an online meeting to discuss the team feedback from sprint 2.
* After looking at the feedback, we realise that the mark was lower than any of us expected, and that there had been issues with finding some of our documents and viewing our KanBan board.

* Jenna and Jurez planned to have a discussion with the Professor the next day in order to get this sorted, since the documents missing accounted for 30% of our grade.
* We also briefly discussed what last documentation needed to be done for Sprint 3.
* In regards to updating the UML and the Process Analysis Model, based on the Professor's idea for doing "hypotheticals" on what we would have changed with earlier feedback, and the fact that we literally didn't get feedback for those two documents, we decided to leave them as they were and explain how we would change them in our hypotheticals.
* Other than that, we still needed to update the read me, finish the microprocess architecture, and do our performance reviews.
  * As well, with the new guidelines given by the Professor, we need to write our hypotheticals too.
  * Jurez also discussed an idea for our hypotheticals, where we each write our own and then put them together into one document. 

## Dec 10, 2023
**Recorded by:** Jenna
**Notes submitted on:** Dec 11, 2023
**SCRUM master:** Wasif
**Venue:** Online (Discord)
**Time:** 9:00am to 10:00am
**Attendance:** Jenna, Jurez, Wasif, Pratik

* This meeting wasn't planned, but arose from a disagreement we had regarding the unit testing.
* For some of us, the unit testing was considering "coding", and thus shouldn't be submitted since our coding deadline of Dec 4th had already passed.
* However, Pratik argued that since the unit test doesn't affect the main project code at all, then it shouldn't be constrained to the code deadline like the other code would be.
* We had a serious discussion on this, and decided that Pratik was right- since the unit test wouldn't have the issue of creating bugs in the main code, we decided that we would allow submitting it past the deadline of Dec 4th, so we accepted Pratik's pull request for his unit test.
  * In accordance with the software engineering process, this discussion is covered in a bit more detail in issue #169.

* Since this meeting wasn't planned, we didn't discuss much else- but we went over the missing things one more time, and decided that we'd try to have everything finished by the night of 11th, since that would leave everyone plenty of time to study for their remaining finals.
* Since most of us had a final on the 11th, we left the meeting there for now and agreed to meet again on the night of the 11th to finish everything and make sure we were happy with our final submission.

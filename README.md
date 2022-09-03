# Capstone - Tasks

Tasks is a to-do list creator application. It may be used to keep track of upcoming tasks or reminders.

## Installation

Tasks runs on Django servers

## Description

Tasks draws upon the lessons learnt in the previous weeks using Django, Python and Javascript.

There are 2 models used in the application. One the User model; drawing from the AbstractUser class and the other a Task model. The task model contains:
- "user" field as a Foreign Key
- "body" field for task title/content
- "timestamp" field for the time the task is created
- "task_date" field for the goal of completion (input by user)
- "completion_date" field to track the actual completion
- "complete" Boolean field to check status of completion

There are 8 templates in the application. One Javascript and one css file in static files. The following details each template:
1. layout.html contains the basic structure of the application
2. login.html contains a post form for logging in
3. register.html also contains a post form for registering new users
4. index.html displays all the tasks
5. create.html again has a form for users to create new tasks
6. edit.html is for editing incomplete tasks
7. task.html is for displaying each task and its details
8. search.html is for searching or displaying search results

On running the application, you will first be presented with an index page, prompting you to login.

Login, logout, register and authentication, is used alongside with Django's AbstractUser class in models.

While logging in you will be taken to a login page. On authentication, user will be redirected back to the index page prompting to create a new task. If authentication fails, an error message will appear in the window.

On registering a new user, the same occurs except this time a register template and view function will be rendered rather than login ones.

To create a new task you will be taken to a new url "create" which consists of a post form. This form asks for the name of the task and the date and time of completion. Once submitted you will see the task has appeared on the index page, along with the date it has been created.

Clicking on a task will take you to a page detailing that task. First, the name/content of the task. Underneath this, on the left side two icons appear which also appear on the index page; the first one for editing and the second for marking as done. On the right side appears a delete button. Beneath this, the goal for completion of the task (given by the user) appears. Lastly, a status appears indicating if the task has been completed (✔️) or is pending (❌).

Now, each task, as mentioned above has multiple features:

### Mark as Done

The mark as done icon appears both on the index page (right aligned) as well as when viewing a particular task. When this icon is hovered over, its title appears. When this icon is clicked, a "complete" function is called and when rendered again you will notice that the task has now been striked through, indicating that it is completed. Along with this the date and time when this icon is clicked has also been added to the database.

While viewing the task you will notice that instead of "pending", the actual completion date is displayed under the goal, along with a "completed" status.  
On hovering above this icon again, the title this time, Unmark as done, will appear. On clicking, the completion date will be removed and "pending" will reappear. In the case that the task is completed again, then the completion time will be updated.

### Edit

Same as the mark as done icon, this icon also appears both on the index page and on the task page. When hovering above this icon, its title "edit" appears. When this icon is clicked, you are directed to an edit page. This page is a post form, prefilled with the body of the task, the previous goal of the task and a datetime input. A logged in user can only edit their task if the task is not yet marked as done.

### Delete

Unlike the above meantioned features, the delete option is not present on the index page, rather you will find this button on the task page and edit page. On clicking this button, a view function "delete" is called and the task is removed from the database.  

Other than the above task-oriented features, the ability to search is also available:

### Search
The search bar is on the index page only when one or more task has been created. When searching for a task if the exact name of the task is inputted then the page is directed to that task page. If a portion of the task is inputted then relative search results are shown.

## Validation

Each form in the project; edit, search and create has been validated so that no user can enter a blank task entry and date. This has been implemented through Javascript. When edit and create are submitted, an alert appears if an error is found. If the form has been submitted successfully then also a successful alert appears.

## Security

Each url in the application is secured to make sure that no user or anonymous user can access any other user's information. They are presented with an error message or a message prompting them to login or create a task instead.

## Distinctiveness and Complexity
This project is distinctive because of the features that each task is provided with. The ability to edit, create and delete tasks reflected by distinctive front-end changes is unique.  
The project is different from general entry making applications as it also has completion statuses and the ability to change this status whenever you please.  
This app implements functionalities which are fairly distinct from the other projects that I have made during the previous weeks of this course.  
Of course, the styles of the application and task window is also unique, with a mobile responsive design and toggle navbar!
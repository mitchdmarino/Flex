# Flex: A workout companion

## Technologies

* Django
* Python
* Pytest
    * Pytest Factory Boy
* Python HTML Calendar
* Postgresql
* Bootstrap 

## Approach

Coming into this project with no Django or test driven development experience, I needed to spend a lot of time researching Django and Pytest/UnitTest before even getting started. 

I first built a small proof of concept app following along with the Django tutorial from the documentation. This helped me better understand Django, but there were still so many features that I was unfamiliar with. I continued to read through the documentation, but it was a lot of information to take in at once and i quickly found that I wasn't making much progress. Eventually, I had to stop researching and just jump in and start coding, even though I was still uncomfortable with the technology. I ran into a multitude of issues that I needed to research how to solve, but this helped me (in the long run) gain a better grasp of how Django works. 

One of my goals for the project was to learn Test Driven Development. I decided to use Pytest to accomplish this, and was successful in setting up some basic tests for my database. However, having little to no experience with Django, I was wasting a lot of time writing tests on features that I didn't even know how to implement yet. Eventually, I decided to focus my attention on learning Django and getting to Pytest later if I had time. However, I did gain valuable insight into how TDD works and will continue writing tests for this app. 

This project was a lot more difficult than I anticipated, mainly due to my lack of experience with Django. It is still a work in progress and I have plans to continue adding on to its features. I also may convert the frontend to React and keep Django on the backend only. 

## Installation Instructions

To install this project, first fork and clone this repository. Then, cd into the project directory and set up your virtual python environment. There are a few ways to do this, you can run the command 
```
python3 -m venv venv
```

To activate the virtual environment, run 
```
source .env/bin/activate
```

Next, install the pip packages by running 
```
pip install -r requirements
```

Also, create a .env file and generate a new Django Secret Key (which Django uses to hash passwords). Add the SECRET_KEY variable. 

To start the project, run ```python3 manage.py runserver```

## User Stories

1. A user will be able to create an account and perform full CRUD actions on Workouts.

1. A user can schedule workouts to be completed at a certain time, viewing past and future workouts on a calendar.

1. A user can complete workouts and add notes (e.g. time elapsed, weight, comment)

1. A user can make their workouts public and view/save other public workouts. (IN PROGRESS)

1. A user can see data showing their progress (weight, personal records, activity, etc) (IN PROGRESS)

## WireFrames
### Dashboard: User's personal Hub
![](./wireframes/Dashboard.png)
### Calendar: User's workout schedule in calendar format
![](./wireframes/Calendar.png)
### Workouts: User's personal workouts list
![](./wireframes/Workouts.png)
### Profile: User's profile info
![](./wireframes/Profile.png)
### Progress: User's Progress shown as visual data
![](./wireframes/Progress.png)
### Goals: User's Achievements + Custom Goals
![](./wireframes/Goals.png)

## Major Hurdles

* Learning both Django and TDD for Django was a bit much for me this project. I didn't finish implementing all of my planned features. 
* The calendar feature was difficult to implement and style
* Debugging in Django took some practice 
* Understanding how to design an API in Django 
* Test Driven Development for request/response cycles, client interaction 


## ERDs

![](./wireframes/ERD.png)

## RESTful routing chart

| VERB | URL pattern | Action \(CRUD\) | Description |
| :--- | :--- | :--- | :--- |
| GET | /routines | Read   | shows list of all workout routines |
| POST | /routines | Create  | creates a new workout routine |
| PUT | /routines/:id | Update | updates the data for a specific routine|
| DELETE | /routines/:id | Destroy | deletes the routine with the specified id|
| GET | /workouts | Read   | shows list of all workout workouts |
| GET | /workouts/:id | Read   | shows list of specific workout  |
| POST | /workouts | Create  | creates a new workout |
| PUT | /workouts/:id | Update | updates the data for a specific workout|
| DELETE | /workouts/:id | Destroy | deletes the workout with the specified id|
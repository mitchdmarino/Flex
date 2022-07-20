# Flex: A workout companion

## Technologies


## Approach

## Installation Instructions

## User Stories

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
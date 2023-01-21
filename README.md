# First-jobber

## Description

The application assists you who are the first jobber and newbie in insurance to choose your reasonable insurance. This app will ask you to fill in the form and recommend three suitable insurance.

## Installation

_only for user who want to install the application in your local_.

### `CREATE DATABASE first_jobber` 

create the database inside your local

### `python manage.py makemigrations`

let your local know the migrations

### `python manage.py migrate`

make migration

### `python manage.py runserver`

run the server

## Link

[Github Link](https://github.com/Panupong026/First-jobber)

## ERD

### Planning ERD

![Database ER diagram](https://user-images.githubusercontent.com/116058313/213878070-07e60092-30b1-44af-912f-7ab96f4151a2.jpeg)

### Actual ERD



## Teachnology used

I use django for backend application and psql for database

## User stories
### MVP Goal:

- [x] As a developer, I want to have a database that collects the detail of the insurance
- [x] As a user, I want the application to have a user database. So that, I can collect the user’s data.

### Strech Goal:

- [ ] As a user, I want the application to compare the three recommended insurance as a table. So, the user can compare the difference clearly.
- [ ] As a user, I want to collect the latest answer from the user. So, the next time the user comes back, the application can show the latest status.
- [ ] As a user, I want the application can export the recommended insurance detail. So, the user can download and keep it.
- [x] As an admin, I want to have an admin feature that can CRUD the insurance table.

## Approch

### Frontend application

I can create a questionnaire application which is able to collect the user driving behavior and provide the suit insurance for them. Moreover the application lead them to the actual site for more information and make a purchase. 

### Backend application

I can create the backend application which the admin can CRUD the insurance, user and coverage and export as a JSON file for the frontend application.

## What left?

### Frontend application

I want the application have a better UX/UI and implement the logic. Moreover, I want the app to collect the user profile and collect it in the database

### Backend application.

I want to have a UserInsurance table to collect the latest user's answer for the next time they come back, the application can still show the questionnaire history.

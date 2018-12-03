# Project: iReporter  
[![Build Status](https://travis-ci.org/karisaJohn/Reporter.svg?branch=ft-user-DeleteSpecificRedFlag-162338345)](https://travis-ci.org/karisaJohn/Reporter)

iReporter is an application that enables any citizen to bring any form of corruption to the notice of appropriate authorities. Citizens can also report on things that need government intervention.


# Technology Used:
* **Python3**
* **Flask**
* **Flask-RESTful**

# [Pivotal Tracker](https://www.pivotaltracker.com/n/projects/2228491)

## Current Endpoints.

| Method | Route | Endpoint Function |
| :--- | :--- | :--- |
| Post | api/v1/redflags | Creates a RedFlag |
| Get | api/v1/redflags | Gets all RedFlags |
| Get | api/v1/redflags/id | Gets a specific RedFlag |
| Patch | api/v1/redflags/id | Edit a specific RedFlag |
| Delete | api/v1/redflags/id | Delete a specific RedFlag |

## Installastion Guide.
#### Clone the repo.
```
$ git clone https://github.com/karisaJohn/Reporter/tree/ft-user-DeleteSpecificRedFlag-162338345

```
#### Create a Virtual Environment and Activate.
```
$ python3 -m venv venv
$ source venv/bin/activate
```
#### Install Dependencies.
```
(venv) $ pip install -r requirements.txt
```
#### Run the app
```
(venv) $ FLASK_APP=run.py
(venv) $ flask run
```
#### Run the Tests
```
(venv) $ pytest --cov=app
```
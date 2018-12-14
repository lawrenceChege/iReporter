# iReporter
A platform where citizens can report corruption cases or government interventions

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/d0bcde400dc8421aa972e9954b90bb11)](https://app.codacy.com/app/lawrenceChege/iReporter?utm_source=github.com&utm_medium=referral&utm_content=lawrenceChege/iReporter&utm_campaign=Badge_Grade_Settings)
[![Coverage Status](https://coveralls.io/repos/github/lawrenceChege/iReporter/badge.svg)](https://coveralls.io/github/lawrenceChege/iReporter)
[![Build Status](https://travis-ci.org/lawrenceChege/iReporter.svg?branch=develop)](https://travis-ci.org/lawrenceChege/iReporter)
[![Maintainability](https://api.codeclimate.com/v1/badges/b99e2ea3d09bbd651354/maintainability)](https://codeclimate.com/github/lawrenceChege/iReporter/maintainability)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/d0bcde400dc8421aa972e9954b90bb11)](https://app.codacy.com/app/lawrenceChege/iReporter?utm_source=github.com&utm_medium=referral&utm_content=lawrenceChege/iReporter&utm_campaign=Badge_Grade_Dashboard)
[![codecov](https://codecov.io/gh/lawrenceChege/iReporter/branch/challenge-3/graph/badge.svg)](https://codecov.io/gh/lawrenceChege/iReporter)

## what it does

It provides a platform where users can report corruption issues to the authorities or report interventions to public projects

## Usage

> As a User, you can:

  * Create an account
  * Log in into the account
  * Create a red-flag or intervention
  * View all his or her interventions/ red-flags
  * View a specific red-flag or intervention
  * View the status of a red-flag or intervention
  * delete a red-flag or intervention
  * modify an inervention or red-flag
  * Add an image to an intervention or red-flag
  * Add a video to an intervention or a red-flag
  * Add a location or a google mapmarker to a red-flag or an intervention

> As an admin, you can

  * view all users red-flags and interventions
  * change the status of all red-flags and interventions

## Prerequisites

  * API
  * python
  * flask

## Installation

**Download option**

  * Go to [iReporter](https://github.com/lawrenceChege/iReporter) on github
  * Download the zip file and extract it
  * Right click on the folder and open with terminal on linux or bash

> we will continue from there :-)

**Cloning option**

  * On your favorite terminal
  * cd to where you want the repo to go
  * Run the following command:

```git clone https://github.com/lawrenceChege/iReporter.git```

  * Then:

`cd iReporter`

**Create virtual environment**

``` python3 -m venv env  ```

  * or alternatively

` virtualenv env`

**Activate virtualenv**
> on linux systems

` source env/bin/activate `
> on windows machines

` env\Scripts\activate `

**Install dependencies**
> using pipenv 
* install pipenv using pip

` pip install pipenv `

* install dependencies

` pipenv install `

> using requirements.txt

` pip install -r requirements.txt `

**Run the App**
> to run the app do 

` flask run`
> to run tests do 

`pytest -v `

Test                               | API-endpoint                                 |HTTP-Verb |
-----------------------------------| -------------------------------------------- | ------ --|
Users can create new incident      |/api/v2/incidents/                            | POST     |
users can view all their incidents | /api/v2/incidents/                           | GET      |
users can view a incident          | /api/v2/incidents/<int:incident_id>/         | GET      |
users can modify their incident    | /api/v2/incidents/<int:incident_id>/         | PUT      |
users can delete a incident        | /api/v2/incidents/<int:incident_id>/         | DELETE   |
Users can modify a new location    |/api/v2/incidents/<int:incident_id>/location  | PATCH    |
users can modify a comment         | /api/v2/incidents/<int:incident_id>/comment  | GET      |
admin can modify the status        | /api/v2/answers/<int:incident_id>/status     | PUT      |

### Author

*Lawrence Chege*

### Acknowledgement

*Andela Kenya*

*Bootcamp-cohort35-comrades*

*Tribeles-Team*

### Support or Contact

[Github Pages](https://lawrencechege.github.io/iReporter/)

[Heroku app](https://ireporti.herokuapp.com/)

*"A beautiful shell of a woman is all that is left of her"*

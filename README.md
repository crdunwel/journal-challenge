# Private Journal Website

Quick implementation of a basic Django web app that allows users to view, create, and delete journal entries.

## Getting Started

Tested in **Python 3.7.6** using CPython interpreter. If one uses pyenv then the included `.python-version` file should choose the correct version.

Django 3.03 is the only requirement as listed in `requirements.txt`

## Installation / How to Run

This is not a fully flushed out project and as such is only intended to be run locally using the Django development server.

After activating virtualenv and installing dependencies, one should first set up the sqlite database by running `python manage.py migrate`.

After setting up the database, one can run `python manage.py runserver`. Navigate to `http://localhost:8000/` will reveal the login page.

There is no registration mechanic currently implemented, but users can be created via the Django admin portal. To do this
one should first create a super user with `python manage.py createsuperuser` then navigate and login at `http://localhost:8000/admin/`.

## Biggest Issue(s)

Deciding how to limit scope to meet the time requirements is not always an easy task. Two hours isn't a lot of time 
to implement a web app with many bells and whistle. In this case, I decided to focus on reaching a good starting point
such that the core requirements of the project were met and a nice structure was in place to expand upon later. Some things
that fell short include:

- Design suffered / nonexistent.
- Only a stencil was created for tests.
- No frontend JavaScript was implemented to make for a smoother user experience.

Accepting not being able to turn in a polished product can be difficult and would say was the biggest issue.

## What I learned

It's been a while since I've started a Django project from scratch and forgot how much time goes into just setting up the
boilerplate. More accustomed day-to-day dealing with better flushed out abstractions and convenience methods so 
writing from scratch proved more time consuming than anticipated.

## What you would have done differently

With limited time there's always trade-offs. If I knew, for instance, that more time would be dedicated to the
project later then I would have spent more time doing the following:
 
- Designing a proper REST API for interacting with journal entries.
- Setting up base components with a frontend framework like Angular or React.
- Putting more thought into structuring the CSS as SCSS.
- Perhaps first looking at open source journaling projects that already exist and how they could be adapted for the needs of this project.
 
Overall, however, I don't think I would do anything much differently given the 
time constraint and the open-endedness of the project. In the end, MVP matters a lot so focused primarily on that.

## License

This code is licensed under the [MIT License](https://opensource.org/licenses/MIT).

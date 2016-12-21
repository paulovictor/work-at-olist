# Work at Olist

Olist is a company that offers an integration platform for sellers and
marketplaces allowing them to sell their products across multiple channels.

The Olist development team consists of developers who love what they do. Our
agile development processes and our search for the best development practices
provide the perfect environment for professionals who like to create quality
software.

We are always looking for good programmers who love to improve their work and
we give preference to small teams with qualified professionals to large teams
with average professionals.

This repository contains a small test used to evaluate if the candidate has the
basic skills to work with us.

You should implement a Django application that provides an API for handling a
tree of products' categories.


## How to participate

1. Make a fork of this repository on Github
2. Follow the instructions of `README.md`.
3. Deploy you project on Heroku
4. Apply for the position at our [career page](https://olist.recruiterbox.com/) and send:
  - Link to the fork on Github.
  - Link to the project in Heroku.
  - Brief description of the work environment used to run this project
    (Computer/operating system, text editor/IDE, libraries, etc.).
  - Curriculum Vitae attached to the email (avoid .doc files) or link to Linkedin profile.


## Specification

As we already said, Olist is a company that provides a platform to integrate
Sellers and Channels (eg. marketplaces).

One of our services allows Sellers to publish their products in channels. All
published products need to be categorized in one of channels' categories.


All channels group the products published in categories that are arranged as a
tree of *varying depths* (from 1 to infinite levels of hierarchy). See version
an small example below:

- Books
  - National Literature
    - Science fiction
    - Fantastic Fiction
  - Foreign literature
  - Computers
    - Applications
    - Database
    - Programming
- Games
  - XBOX 360
    - Console
    - Games
    - Accessories
  - XBOX One
    - Console
    - Games
    - Accessories
  - Playstation 4
- Computing
  - Notebooks
  - Tablets
  - Desktop
- :

Each channel sends us a CSV file where one of the columns (`Category`) is
contains the full category's path:

```
Category
Books
Books / National Literature
Books / National Literature / Science Fiction
Books / National Literature / Fiction Fantastic
Books / Foreign Literature
Books / Computers
Books / Computers / Applications
Books / Computers / Database
Books / Computers / Programming
Games
Games / XBOX 360
Games / XBOX 360 / Console
Games / XBOX 360 / Games
Games / XBOX 360 / Accessories
Games / XBOX One
Games / XBOX One / Console
Games / XBOX One / Games
Games / XBOX One / Accessories
Games / Playstation 4
Computers
Computers / Notebooks
Computers / Tablets
Computers / Desktop
:
```


## Project Requirements

The project must implement the following features:

- Python >= 3.5 and Django >= 1.9.
- Use PEP-8 for code style.
- The data should be stored in a relational database.
- A *Django Management Command* to import the channels' categories from a CSV.
  - Import command should operate in "full update" mode, ie it must overwrite
    all categories of a channel with the categories in CSV.
  - The command should receive 2 arguments: channel name (create the channel if
    it doesn't exists in database) and the name of `.csv` file:

```
$ python manage.py importcategories walmart categories.csv
```

- Each channel has its own set of categories.
- Each channel must have a unique identifier and a field with the channel's
  name.
- Each category must have a unique identifier and a field with the category's
  name.
- Creating a HTTP REST API that provides the following functionalities:
  - List existing channels.
  - List all categories and subcategories of a channel.
  - Return a single category with their parent categories and subcategories.

> Tip #1:
> Optimize for category tree read performance!

- English documentation of API.
- Variables, code and strings must be all in English.

> Tip #2:
> Django project boilerplate in this repository has several points for
> improvement. Find them and implement these improvements.


## Recommendations

- Write tests.
- Avoid exposing database implementation details in the API (eg. do not expose model ID at URLs)
- Practice the [12 Factor-App] (http://12factor.net) concepts.
- Make small and atomic commits, with clear messages (written in English).
- Use good programming practices.



## Installation on macOSX

- Create the virtualenv
```
virtualenv --no-site-packages --python=python3 work-at-olist
```

- Move to the virtualenv folder
```
cd work-at-olist
```
- Active the virtualenv
```
source bin/activate
```
- Clone the git repository

```
git clone https://github.com/paulovictor/work-at-olist.git
```
- Move to the project folder
```
cd work-at-olist/
```
- Install the requirements
```
pip install -r requirements.txt
```
- Configure your local database on workatolist/settings.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'olist',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```


- at folder /work/work-at-olist/work-at-olist execute this commands
```
make migrate
make run
```

- Now, access the http://127.0.0.1:8000/

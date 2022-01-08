# gobal-cms-django Base app

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Developer-DewPool/gobal-cms-django.git
$ cd gobal-cms-django
```

if virtualenv not install then first install virtualenv:

```sh
/gobal-cms-django$ pip3 install virtualenv
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)/gobal-cms-django$ pip3 install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip3` has finished downloading the dependencies:
```sh
(env)/gobal-cms-django$ ./manage.py runserver
```
And navigate to `http://127.0.0.1:8000/admin/` or `http://127.0.0.1:8000/`.

for `http://127.0.0.1:8000/admin/` create credential:

```sh
(env)/gobal-cms-django$ ./manage.py createsuperuser
```

then complete as it follow.
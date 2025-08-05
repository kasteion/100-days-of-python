1. Add gunicorn to the requirements.txt

```
gunicorn==21.2.0
```

The format for all packages in requirements.txt is

```
gunicorn==<version number>

```

2. Create a Profile (This has to do with heroku)

```
web: gunicorn main:app
```

| If your app is not inside a file called main.py then you should change main to your file name

3. Push to your remote on Github

4. Sign up to a hosting provider and create your web service

There are many different hosting providers

There are many different hosting providers to choose from when it comes to making your app go live on the internet. Features and pricing vary between them and their pricing plans can change. It's up to you who you want to choose. For this tutorial, I will show you how to host on render.com

| Provider       | ~Cost / Month | Name of Plan |
| -------------- | ------------- | ------------ |
| Heroku         | $5            | Eco & Basic  |
| render         | $0            | Individual   |
| Cyclic         | $0            | Free Forever |
| Glitch         | $0            | Starter      |
| Vercel         | $0            | Hobby        |
| PythonAnywhere | $0            | Beginner     |

The nice thing about most of these providers is that they can easily deploy your app straight from a GitHub repo. We've done most of the difficult bits already. There are just a few steps left:

Create an account with the hosting provider: Create an account on render.com by signing up via Github

6. Link our GitHub repo with the host: Create a New Web Service and choose your app uploaded to GitHub anc connect your repo.

7. Store the key-value pairs for our environment variables with our host.

- Edit the Start Command to `gunicorn main:app`
- Add the environment variables for your Flask app (Should be an "Advanced" option to do this)

8. Upgrade SQLite Database to PostgreSQL

Luckily, because we used SQLAlchemy to create our Flask app, there's nothing we need to change in terms of code. We just need to set up the PostgreSQL database.

- Create a new Postgres database from the website menu.
- Next, you will see a form. All you need to do is pick a name for the database and create it.
- Once you've created your database, go and find the Internal Database URL in the Info section. You might have to wait a little while until your database is created.
- Afterwards, simply copy this URL. You will shortly use this as an environment variable.
- Set your `SQLALCHEMY_DATABASE_URI` environment variable the valus of the URI shoud be something like `postgres://example_ig2c_user:u0E_lots_of_Symbols_here@dpg-c_more_symbols3bj85d0-a/example_ig2c`

How does all this work? SQLite is pre-installed for all Python projects, but here we are using Postgres. The reason we can seamlessly switch from SQLite to Postgres is because we are using the [psycopg](https://pypi.org/project/psycopg2-binary/) package in combination with SQLAlchemy. The psycopg module is an incredibly popular PostgreSQL database adapter for Python. (You can see the psycopg package listed in the requirements.txt.)

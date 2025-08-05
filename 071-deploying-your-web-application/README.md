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

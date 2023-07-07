import datetime as dt
import random
import smtplib
import os

WEEKDAY = 4
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")
DEST_EMAIL = os.environ.get("DEST_EMAIL")

quotes = None

with open("quotes.txt") as q:
    quotes = q.readlines()

weekday = dt.datetime.now().weekday()

if weekday == WEEKDAY:
    q = random.choice(quotes)
    with smtplib.SMTP("smtp.gmail.com", port=587) as conn:
        conn.starttls()
        conn.login(user=EMAIL, password=PASSWORD)
        conn.sendmail(
            from_addr=EMAIL,
            to_addrs=DEST_EMAIL,
            msg=f"Subject:Motivation\n\n{q}")


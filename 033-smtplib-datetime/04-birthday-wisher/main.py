import pandas as pd
import datetime as dt
import random
import smtplib
import os

EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

letter_templates = []
with open("letter_templates/letter_1.txt") as l1, open("letter_templates/letter_2.txt") as l2, \
        open("letter_templates/letter_3.txt") as l3:
    letter_templates.append("".join(l1.readlines()))
    letter_templates.append("".join(l2.readlines()))
    letter_templates.append("".join(l3.readlines()))

# 1. Update the birthdays.csv
birthdays = pd.read_csv("birthdays.csv")

# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()
today_birthdays = birthdays[(birthdays.month == today.month) & (birthdays.day == today.day)]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name
# from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.
for _, contact in today_birthdays.iterrows():
    letter = random.choice(letter_templates).replace("[NAME]", contact["name"])
    with smtplib.SMTP("smtp.gmail.com", port=587) as conn:
        conn.starttls()
        conn.login(user=EMAIL, password=PASSWORD)
        conn.sendmail(
            from_addr=EMAIL,
            to_addrs=contact["email"],
            msg=f"Subject:Happy Birthday!\n{letter}")


# python anywhere

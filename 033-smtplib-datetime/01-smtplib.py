import smtplib
import os

EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")
DEST_EMAIL = os.environ.get("DEST_EMAIL")

# Google: smtp.gmail.com
# Hotmail: smtp.live.com
# Yahoo: smtp.mail.yahoo.com


# connection = smtplib.SMTP("smtp.gmail.com", port=587)

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=EMAIL, password=PASSWORD)
    connection.sendmail(
        from_addr=EMAIL,
        to_addrs=DEST_EMAIL,
        msg="Subject:Hello\n\nThis is the body of my email.")

# connection.close()

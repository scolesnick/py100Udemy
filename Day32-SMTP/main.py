import sys
import smtplib
import random

app_email = sys.argv[1]
app_psw = sys.argv[2]
target_email = sys.argv[3]

# from cmd run - py main.py '<email>' '<password>' '<target email>'
# print(f'email: {app_email}\npassword: {app_psw}\ntarget email: {target_email}')

def send_quote(message):
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=app_email, password=app_psw)
        connection.sendmail(
            from_addr=app_email,
            to_addrs=target_email,
            msg=f'Subject:Inspirational Quote Day\n\n{message}'
        )

import datetime as dt
now = dt.datetime.now()

year=now.year
month=now.month
day=now.weekday()

# Challenge - send a motivational quote via email on the current weekday
quote_day = 5

with open(file='quotes.txt',mode='r') as file:
    lines = file.readlines()
quote = random.choice(lines)

if day == quote_day:
    send_quote(quote)
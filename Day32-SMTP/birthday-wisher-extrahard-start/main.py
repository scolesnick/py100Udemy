##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas
import random
import os
import sys
import smtplib
app_email = sys.argv[1]
app_psw = sys.argv[2]
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
month = now.month
day = now.day

df = pandas.read_csv('birthdays.csv')
bday_records = df.to_dict(orient='records')
match_bdays = []

for rec in bday_records:
    b_m = int(rec['month'])
    b_d = int(rec['day'])

    if b_m == month and b_d == day:
        match_bdays.append(rec)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
bday_today = len(match_bdays) > 0

if bday_today:
    for bday in match_bdays:
        letter_dir = 'letter_templates'
        letters = [os.path.join(letter_dir, f) for f in os.listdir(letter_dir) if os.path.isfile(os.path.join(letter_dir, f))]
        letter_path = random.choice(letters)

        with open(letter_path, mode='r') as file:
            lines = file.readlines()
        lines[0] = lines[0].replace('[NAME]',bday['name'])
        bday['letter'] = ''.join((lines))

# 4. Send the letter generated in step 3 to that person's email address.
def send_quote(message, target_email):
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=app_email, password=app_psw)
        connection.sendmail(
            from_addr=app_email,
            to_addrs=target_email,
            msg=f'Subject:Happy Birthday!\n\n{message}'
        )

for bday in match_bdays:
    send_quote(bday['letter'],bday['email'])
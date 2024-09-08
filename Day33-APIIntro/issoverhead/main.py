import requests
from datetime import datetime, timezone
import sys
import smtplib

app_email = sys.argv[1]
app_psw = sys.argv[2]
target_email = sys.argv[3]

MY_LAT = 35.075500 # Your latitude
MY_LONG = -91.881752 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
def is_within():
    lat_max = iss_latitude + 5
    lat_min = iss_latitude - 5
    long_max = iss_longitude + 5
    long_min = iss_longitude - 5
    if lat_min <= MY_LAT <= lat_max and long_min <= MY_LONG <= long_max:
        return True
    else:
        return False

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now(tz=timezone.utc)

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

def is_dark():
    if sunset <= time_now.hour < sunrise:
        return True
    else:
        return False

def send_alert():
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=app_email, password=app_psw)
        connection.sendmail(
            from_addr=app_email,
            to_addrs=target_email,
            msg='Subject:ISS Alert\n\nTheISS is above right now, look up!'
        )

if is_dark() and is_within():
    send_alert()
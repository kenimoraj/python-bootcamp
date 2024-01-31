import requests
from datetime import datetime
from math import fabs
import smtplib, time

MY_LAT = 52.229675 # Your latitude
MY_LONG = 21.012230 # Your longitude
LOGIN = "michal@jarominek.com"
PASSWORD = "ojweujjjmayvakak"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


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

time_now = datetime.now()

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.


while True:
    time.sleep(60)
    iss_is_close = fabs(iss_latitude - MY_LAT) < 5 and fabs(iss_longitude - MY_LONG) < 5
    curr_hour = time_now.hour
    is_dark = curr_hour > sunset or curr_hour < sunrise


    if iss_is_close and is_dark:
        with smtplib.SMTP("smtp.gmail.com") as conn:
            conn.starttls()
            conn.login(user=LOGIN, password=PASSWORD)
            conn.sendmail(to_addrs=LOGIN, msg=f"Subject:Might wanna look up for ISS\n\nISS is currently at ({iss_latitude},{iss_longitude})")

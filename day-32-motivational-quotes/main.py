import datetime as dt
import random
import smtplib
DAYS_OF_WEEK = ["Monday",
                "Tuesday",
                "Wednesday",
                "Thursday"
                "Friday",
                "Saturday",
                "Sunday"]

quotes = []

now = dt.datetime.now()

day_of_week = now.weekday()

# print(f"Today is {DAYS_OF_WEEK[day_of_week]}")

with open("quotes.txt", mode="r", encoding="utf-8") as file:
    quotes = file.readlines()

quote_to_send = random.choice(quotes)
print(quote_to_send)

# SENDING MAIL
mail_content = f"Subject:Motivational Quote for {DAYS_OF_WEEK[day_of_week]}\n\n{quote_to_send}".encode(encoding="utf-8")

email = "michal@jarominek.com"
passwd = "ojweujjjmayvakak"

with smtplib.SMTP("smtp.gmail.com") as connection:
    print("Connected")
    connection.starttls()
    print("TLS Established")
    connection.login(user=email, password=passwd)
    print("Logged")
    connection.sendmail(to_addrs=email, from_addr="aaa"+email, msg=mail_content)
    print("Mail sent")

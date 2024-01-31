##################### Extra Hard Starting Project ######################
import datetime as dt
import random
import pandas
import smtplib

LOGIN = "michal@jarominek.com"
PASSWORD = "ojweujjjmayvakak"
SMTP_SERVER = "smtp.gmail.com"

# 1. Update the birthdays.csv
#DONE
# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
c_month = now.month
c_day = now.day

df = pandas.read_csv("./birthdays.csv")
birthdays = [{"Name": row["name"], "Email": row["email"], "DoB": dt.datetime(year=row["year"],
                                                                              month=row["month"],
                                                                              day=row["day"])}
             for (index, row) in df.iterrows()]

people = []
for b in birthdays:
    if b["DoB"].month == c_month and b["DoB"].day == c_day:
        people.append(b)


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
templates = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

for p in people:
    chosen_template = random.choice(templates)
    with open("./letter_templates/"+chosen_template) as file:
        letter = file.read()
    letter = letter.replace("[NAME]", p["Name"])

    subject = f"Subject:This would go to {p['Email']}"


# 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP(SMTP_SERVER) as conn:
        conn.starttls()
        conn.login(user=LOGIN, password=PASSWORD)
        conn.sendmail(from_addr="fakju@onet.pl", to_addrs=LOGIN, msg=subject+"\n\n"+letter)
        print(f"Mail sent to {p['Name']}")




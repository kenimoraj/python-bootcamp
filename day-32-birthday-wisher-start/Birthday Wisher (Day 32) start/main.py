import os
import smtplib

my_email = os.environ["MY_EMAIL"]
passwd = os.environ["PASSWD"]


with smtplib.SMTP("smtp.gmail.com") as connection:
    print("connected")
    connection.starttls()
    print("tls")
    connection.login(user=my_email, password=passwd)
    print("logged")
    connection.sendmail(
        from_addr="adam.mickiewicz@poczta",
        to_addrs=my_email,
        msg="Subject:Atak!\n\nCiekawe czy zadziala"
    )
    print("sent")

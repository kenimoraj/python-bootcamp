import os
import smtplib

import requests
import datetime as dt
from math import fabs

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHAVANTAGE_API_KEY = os.environ['ALPHADVANTAGE_API_KEY']
NEWSAPI_KEY = os.environ['NEWSAPI_KEY']
LOGIN = os.environ['LOGIN']
PASSWD = os.environ['PASSWD']


ALPHAVANTAGE_PARAMS={
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHAVANTAGE_API_KEY
}

NEWSAPI_PARAMS = {
    "q": COMPANY_NAME,
    "sortBy": "publishedAt",
    "apiKey": NEWSAPI_KEY,
    "language": "en"
}

def get_last_two_dates_str() -> tuple:
    now = dt.datetime.now()
    format_str = "{year:d}-{month:02d}-{day:02d}"
    last_date = now - dt.timedelta(1)
    last = format_str.format(year=last_date.year, month=last_date.month, day=last_date.day)
    before_last_date = now - dt.timedelta(2)

    before_last = format_str.format(year=before_last_date.year, month=before_last_date.month, day=before_last_date.day)

    return last, before_last

def percent_change(x1: float, x2: float) -> float:
    delta = x2 - x1
    return round(delta / x1, 2)

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get("https://www.alphavantage.co/query", params=ALPHAVANTAGE_PARAMS)
response.raise_for_status()
stock_data = response.json()




(last, before_last) = get_last_two_dates_str()

stock_closed_before_last_value = float(stock_data["Time Series (Daily)"][before_last]["4. close"])
stock_close_last_value = float(stock_data["Time Series (Daily)"][last]["4. close"])

perc_delta = percent_change(stock_closed_before_last_value, stock_close_last_value)

get_news = fabs(perc_delta) > 5
print(f"Percentage change was {perc_delta}")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
response = requests.get("https://newsapi.org/v2/everything", params=NEWSAPI_PARAMS)
response.raise_for_status()
news_data = response.json()
articles = news_data["articles"][:3]

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

for a in articles:
    plusminus: str
    if perc_delta > 0:
        plusminus = "+"
    else:
        plusminus = "-"
    mail_title = f"[{STOCK} {plusminus} {fabs(perc_delta)}] - {a['title']}".encode("ascii", "ignore")
    mail_content = (a['description'] + f"\n{a['url']}").encode("ascii", "ignore")


    with smtplib.SMTP("smtp.gmail.com") as conn:
        conn.starttls()
        conn.login(user=LOGIN, password=PASSWD)
        conn.sendmail(to_addrs=LOGIN, from_addr=LOGIN, msg=f"Subject:{mail_title}\n\n{mail_content}")



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


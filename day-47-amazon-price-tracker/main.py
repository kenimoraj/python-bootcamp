import requests
from bs4 import BeautifulSoup

headers = {
    # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
'Accept-Language': 'en-US, en;q=0.5'
}
url = "https://www.amazon.com/Instant-Pot-Plus-Programmable-Sterilizer/dp/B075CWJ3T8/ref=sr_1_1?crid=1LVB99WKVCKJH&keywords=instant%2Bpot%2Bduo%2Bplus&qid=1706139995&sprefix=instant%2Bpot%2Bduo%2Bplu%2Caps%2C194&sr=8-1&th=1"

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
print(response.status_code)
# print(soup.prettify())
whole = soup.find("span", class_="a-price-whole").getText()[:-1]
fraction = soup.find("span", class_="a-price-fraction").getText()

price = float(f"{whole}.{fraction}")

print(price)

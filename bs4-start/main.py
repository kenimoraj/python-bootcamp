from bs4 import BeautifulSoup
import requests

yc_web_page = requests.get("https://news.ycombinator.com/")

soup = BeautifulSoup(yc_web_page.text, "html.parser")

print(soup.prettify())

tags = soup.find_all("span", class_="titleline")

texts = []
links = []

for tag in tags:
    text = tag.find("a").getText()
    texts.append(text)
    link = tag.find("a").get("href")
    links.append(link)


upvotes = [int(score.getText().split()[0]) for score in soup.find_all("span", class_="score")]

print(texts)
print(links)
print(upvotes)

max_score = upvotes[0]
max_index = 0

for i in range(1, len(upvotes)):
    if upvotes[i] > max_score:
        max_score = upvotes[i]
        max_index = i


print("=================\nMost upvotes:")
print(texts[max_index])
print(links[max_index])
print(upvotes[max_index])
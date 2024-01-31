from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
source = response.text
soup = BeautifulSoup(source, "html.parser")

items = [tag.getText() for tag in soup.select(".article-title-description__text .title")]

with open("./movies.txt", "w", encoding="utf-8") as file:
    for item in items[::-1]:
        print(item)
        file.write(item)
        file.write('\n')


import requests
from bs4 import BeautifulSoup

# https://news.ycombinator.com/robots.txt
response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

texts = [title.find(name="a").text for title in soup.find_all(name="span", class_="titleline")]
links = [title.find(name="a").get("href") for title in soup.find_all(name="span", class_="titleline")]
scores = [int(score.text.split(" ")[0]) for score in soup.find_all(name="span", class_="score")]

print(texts)
print(links)
print(scores)

most_voted = max(scores)
most_voted_index = scores.index(most_voted)

print(texts[most_voted_index])
print(links[most_voted_index])





from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

# import lxml
# soup = BeautifulSoup(contests, lxml)

# get the title tag
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup)
print(soup.prettify())
# The fist anchor tag
print(soup.a)

all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

all_paragraph_tags = soup.find_all(name="p")
print(all_paragraph_tags)

for a in all_anchor_tags:
    print(a.getText())
    print(a.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

company_url = soup.select_one(selector="p a")
print(company_url)

headings = soup.select(selector=".heading")
print(headings)

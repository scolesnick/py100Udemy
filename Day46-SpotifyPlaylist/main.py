from bs4 import BeautifulSoup
import requests
from numpy.lib.function_base import place

BASE_URL = "https://www.billboard.com/charts/hot-100/"


header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

# year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")

url = BASE_URL + "2000-08-12/"

#  scrape the top 100 song titles on that date into a Python List
response = requests.get(url=url)
soup = BeautifulSoup(response.text, "html.parser")

row_tags = soup.find_all("div",class_="o-chart-results-list-row-container")
# print(row_tag)

top100 = {}
for t in row_tags:
    placement = t.find("span").get_text().strip()
    title_tag = t.find("h3",id="title-of-a-story")
    art_tag = t.find("h3",id="title-of-a-story").findNext('span')
    title = title_tag.get_text().strip()
    artist = art_tag.get_text().strip()
    top100[placement] = [title, artist]

print(top100)
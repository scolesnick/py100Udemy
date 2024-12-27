from statistics import mode

import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
page = response.text

soup = BeautifulSoup(page, "html.parser")

movies = soup.find_all("h3", class_="title")

movies = movies[::-1]

# print(movies)
#
# for m in movies:
#     print(m.get_text())

with open("movies.txt",mode="w") as f:
    for m in movies:
        try:
            f.write(str(m.get_text())+'\n')
        except UnicodeEncodeError:
            f.write(str(m.get_text().encode("ascii", "replace").decode())+'\n')
from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_webpage = response.text

# For article with highest upvotes on the page
#  Get Article Title
#  Get Link of Article

soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.find_all("a", class_="storylink")
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.get_text()
    link = article_tag.get("href")
    article_texts.append(text)
    article_links.append(link)

article_upvotes = [score.getText()  for score in soup.find_all("span", class_="score")]
upvote_points = [int(score.split()[0]) for score in article_upvotes]

# print(article_texts)
# print(article_links)
# print(article_upvotes)
# print(upvote_points)

max_points = max(upvote_points)
max_title = article_texts[upvote_points.index(max_points)]
max_link = article_links[upvote_points.index(max_points)]

print(max_title)
print(max_points)
print(max_link)

# with open(file='website.html') as f:
#     contents = f.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
#
# print(soup)
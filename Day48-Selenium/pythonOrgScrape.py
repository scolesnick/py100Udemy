from selenium import webdriver
from selenium.webdriver.common.by import By
import pprint as pp


# Scrape all upcoming event dates and event names from python.org
# Store them in a nested dictionary and print to the console
url = "https://www.python.org/"
e_dict = {}


#Keep browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)



dates = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li/time')
events = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li/a')

for i in range(len(dates)):
    e_dict[dates[i].text] = events[i].text

pp.pprint(e_dict)

driver.quit()
from bs4 import BeautifulSoup
import requests
from pandas import Series,DataFrame
import pandas as pd


response = requests.get("https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos")
yc = response.text
soup = BeautifulSoup(yc,'html.parser')
article = soup.find_all('td')

for art in article:
    print(art.getText())







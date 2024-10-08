url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
from fake_useragent import UserAgent
import requests
ua = UserAgent()
headers = {'User-Agent': ua.random}
response = requests.get(url, headers=headers)
# print(response)
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
# from splinter import Browser
import numpy as np

pd.set_option('max_colwidth', 800)
html = response.content
soup = bs(html, 'html.parser')

dict_peliculas = {"Titulos"  : [],
                "Rating" : [],
                "Año" : [],
                "Duración" : []}

for enlace in soup.find_all("h3", class_ = "ipc-title__text")[1:26]:
    dict_peliculas["Titulos"].append(enlace.get_text())
    # print(enlace.get_text())

for enlace in soup.find_all("span", class_ = "ipc-rating-star--rating")[:25]:
    dict_peliculas["Rating"].append(enlace.get_text())
    # print(enlace.get_text())

for enlace in soup.find_all("span", class_ ="sc-ab348ad5-8 cSWcJI cli-title-metadata-item")[:75:3]:
    dict_peliculas["Año"].append(enlace.get_text())
    # print(enlace.get_text())

for enlace in soup.find_all("span", class_ ="sc-ab348ad5-8 cSWcJI cli-title-metadata-item")[1:75:3]:
    dict_peliculas["Duración"].append(enlace.get_text())

df = pd.DataFrame(dict_peliculas)
df.index = range(1, len(df) +1)

df = df.rename_axis('Posición', axis='index')

df.to_csv("imdb_scrap.csv")

print("Importando librerías...")
###Librerías:
import numpy as np
import pandas as pd
from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup as bs

print("Accediendo a la web...")
###Acceso a la web, descarga de información y creación de diccionario
ua = UserAgent()
headers = {'User-Agent': ua.random}
response = requests.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250", headers=headers)
html = response.content
soup = bs(html, 'html.parser')
movie_dict = {"Title":[],"Year":[],"Length":[],"Pos":[],"Rating":[]}

print("Extrayendo información...")
###Saca título y posición
titles = soup.find_all("h3")
for t in titles[1:26]:
    movie_dict["Pos"].append(t.get_text()[:t.get_text().find(".")]) ### El título ya nos da la posición
    movie_dict["Title"].append(t.get_text()[t.get_text().find(".")+2:]) ### Dos caracteres extra ". "

###Saca años y duración
movie_attrs = soup.find_all("span", attrs= "sc-ab348ad5-8 cSWcJI cli-title-metadata-item")
#Años
for y in movie_attrs[::3]:
    movie_dict["Year"].append(int(y.get_text()))
#Duración
for l in movie_attrs[1::3]:
    movie_dict["Length"].append(l.get_text())

###Saca rating
movie_ratings=soup.find_all("span", attrs="ipc-rating-star--rating")
for mr in movie_ratings:
    movie_dict["Rating"].append(float(mr.get_text()))

print("Exportando a csv...")
###Genera df y guarda en csv
df_movies = pd.DataFrame(movie_dict)
df_movies.to_csv(input("Introduce el nombre del archivo: ")+".csv",index=False)
print("¡Terminado! Creado archivo con",len(df_movies),"elementos")
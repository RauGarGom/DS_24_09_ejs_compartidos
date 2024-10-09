import hashlib
import requests
from datetime import datetime
import pandas as pd




def hash_params(timestamp, priv_key, pub_key):
    """ Marvel API requires server side API calls to include
    md5 hash of timestamp + public key + private key 
    """
    hash_md5 = hashlib.md5()
    hash_md5.update(f'{timestamp}{priv_key}{pub_key}'.encode('utf-8'))
    hashed_params = hash_md5.hexdigest()
    return hashed_params





timestamp = datetime.now().strftime('%Y-%m-%d%H:%M:%S')

pub_key = 'ab9047ea60c418f3410a8a0efa1e680a'
priv_key = '38ce0a196dad9c6a9c5c0bafff9d63e04879995b'

params = {
    'ts': timestamp, 
    'apikey': pub_key, 
    'hash': hash_params(timestamp, priv_key, pub_key),
    'nameStartsWith': "J",
    'offset': 0,
    'limit': 45 
}

url = 'http://gateway.marvel.com/v1/public/characters'

res = requests.get(url, params=params)





data = res.json()
characters = data['data']['results']

for character in characters:
    thumbnail = character['thumbnail']
    character['picture_url'] = thumbnail['path'] + '.' + thumbnail['extension']
        
df_characters = pd.DataFrame(characters)
df_characters = df_characters[['id', 'name', 'picture_url']]






now = str(datetime.now()).replace(" ", "_").replace(":", "_")[:16]
nombre = "marvel_characters_Javier_" + now[5:] + ".csv"  
        
df_characters.to_csv(nombre, index=False) 
print(f"Archivo .csv guardado")


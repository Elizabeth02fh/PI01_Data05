import pandas as pd 
import numpy as np 

data = pd.read_csv("data_general.csv", index_col= False, sep= ",", header= 0)

### QUERY 1:
def get_max_duration(anio: int, plataforma: str, dtype: str):
    """
    Esta función devuelve la película con mayor duración según año, plataforma y tipo de duración.
    """
    q1 = data[(data['release_year'] == anio) & (data['plataforma'] == plataforma) & (data['duration_type'] == dtype)].sort_values("duration_int", ascending= False).head(1)

    result = q1["title"].to_list()
    
    return f"La pelicula: {result}"

#print(get_max_duration(2014,"amazon", "min"))

### QUERY 2:
def get_score_count(plataforma: str, scored: float, anio: int):
    """
    Esta función devuelve la cantidad de películas por plataforma con un puntaje mayor a XX en determinado año.
    """
    q2 = data[(data["plataforma"] == plataforma) & (data["score"] > scored) & (data["release_year"] == anio)].shape[0]

    return {"plataforma" : plataforma,
            "cantidad:" : q2,
            "anio" : anio,
            "score" : scored}
#print(get_score_count("netflix", 3.5, 2015))

### QUERY 3:
def get_count_platform(plataforma: str):
    """
    Esta función devuelve la cantidad de películas según el tipo de plataforma.
    """
    q3 = data[(data["plataforma"] == plataforma) & (data["type"] == "movie") ].shape[0]

    return {"plataforma": plataforma, "películas": q3}
#print(get_count_platform("hulu"))

### QUERY 4:
def get_actor(plataforma: str, anio: int):
    """
    Esta función devuelve aquel Actor que más se repite según plataforma y año.
    """
    q4 = data[(data["plataforma"] == plataforma) & (data["release_year"] == anio)]
    q4 = q4.assign(actor= q4.cast.str.split(",")).explode("cast")
    q4 = q4.cast.value_counts()
    
    actor = q4.index[0]
    cantidad = int(q4.iloc[0])

    return {"plataforma" : plataforma,
            "anio:" : anio,
            "actor" : actor,
            "apariciones" : cantidad}
#print(get_actor("amazon", 2020))

### QUERY 5:
def prod_per_county(tipo: str, pais: str, anio: int):
    """
    Esta función devuelve la cantidad de contenidos/productos que se publicó por país y año.
    """
    q5 = data[(data["type"] == tipo) & (data["country"] == pais) & (data["release_year"] == anio) ].shape[0]

    return {"Pais" : pais,
            "anio:" : anio,
            "peliculas" : q5}
#print(prod_per_county("movie", "canada", 2018))

### QUERY 6:
def get_contents(rating: str):
    """
    Esta función devuelve la cantidad de contenidos/productos según el rating de audiencia dado.
    """
    q6 = data[(data["rating"] == rating) & (data["type"] == "movie")].shape[0]

    return {"rating" : rating, "contenido" : q6}
#print(get_contents("13+"))
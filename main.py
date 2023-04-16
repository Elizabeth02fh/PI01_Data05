from fastapi import FastAPI
import queries
import pandas as pd 
import numpy as np 

app = FastAPI()

# Query 1: 
@app.get("/get_max_duration/{anio}/{plataforma}/{dtype}")
async def get_max_duration(anio: int, plataforma: str, dtype: str):
    """
    Esta función devuelve la película con mayor duración según año, plataforma y tipo de duración.
    """
    q1 = queries.get_max_duration( anio, plataforma, dtype)

    return f"La pelicula: {q1}"


# Query 2:
@app.get("/get_score_count/{plataforma}/{scored}/{anio}")
async def get_score_count(plataforma: str, scored: float, anio: int):
    """
    Esta función devuelve la cantidad de películas por plataforma con un puntaje mayor a XX en determinado año.
    """
    q2 = queries.get_score_count(plataforma, scored, anio)

    return {"plataforma" : plataforma,
            "cantidad:" : q2,
            "anio" : anio,
            "score" : scored}

# Query 3:
@app.get("/get_count_platform/{plataforma}")
async def get_count_platform(plataforma: str):
    """
    Esta función devuelve la cantidad de películas según el tipo de plataforma.
    """
    q3 = queries.get_count_platform(plataforma)

    return {"plataforma": plataforma, "películas": q3}


# Query 4:
@app.get("/get_actor/{plataforma}/{anio}")
async def get_actor(plataforma: str, anio: int):
    """
    Esta función devuelve aquel Actor que más se repite según plataforma y año.
    """
    data = pd.read_csv("data_general.csv", index_col= False, sep= ",", header= 0)
    q4 = data[(data["plataforma"] == plataforma) & (data["release_year"] == anio)]
    q4 = q4.assign(actor= q4.cast.str.split(",")).explode("cast")
    q4 = q4.cast.value_counts()
    
    actor = q4.index[0]
    cantidad = int(q4.iloc[0])

    return {"plataforma" : plataforma,
            "anio:" : anio,
            "actor" : actor,
            "apariciones" : cantidad}

# Query 5:
@app.get("/prod_per_county/{tipo}/{pais}/{anio}")
async def prod_per_county(tipo: str, pais: str, anio: int):
    """
    Esta función devuelve la cantidad de contenidos/productos que se publicó por país y año.
    """
    q5 = queries.prod_per_county(tipo, pais, anio)

    return {"Pais" : pais,
            "anio:" : anio,
            "peliculas" : q5}

# Query 6:
@app.get("/get_contents/{rating}")
async def get_contents(rating: str):
    """
    Esta función devuelve la cantidad de contenidos/productos según el rating de audiencia dado.
    """
    q6 = queries.get_contents(rating)

    return {"rating" : rating, "contenido" : q6}
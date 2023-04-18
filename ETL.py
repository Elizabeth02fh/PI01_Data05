# importando las librería a utilizar
import pandas as pd 
import numpy as np 

# Cargando todos los datasets incluyendo la carpeta "ratings".
Amazon = pd.read_csv("Data/amazon_prime_titles.csv", index_col= False, sep= ",", header= 0)
    # Agregando un nombre al dataset Amazon.
Amazon.name = "Amazon"

Disney = pd.read_csv("Data/disney_plus_titles.csv", index_col= False, sep=",", header= 0)
    # Agregando un nombre al dataset Disney.
Disney.name = "Disney"

Hulu = pd.read_csv("Data/hulu_titles.csv", index_col= False, sep=",", header= 0)
    # Agregando un nombre al dataset Hulu.
Hulu.name = "Hulu"

Netflix = pd.read_csv("Data/netflix_titles.csv", index_col= False, sep=",", header= 0)
    # Agregando un nombre al dataset Netflix.
Netflix.name = "Netflix"

ratings_uno = pd.read_csv("Data/ratings/1.csv", index_col= False, sep= ",", header= 0)
ratings_dos = pd.read_csv("Data/ratings/2.csv",index_col= False, sep= ",", header= 0)
ratings_tres = pd.read_csv("Data/ratings/3.csv",index_col= False, sep= ",", header= 0)
ratings_cuatro = pd.read_csv("Data/ratings/4.csv",index_col= False, sep= ",", header= 0)
ratings_cinco = pd.read_csv("Data/ratings/5.csv",index_col= False, sep= ",", header= 0)
ratings_seis = pd.read_csv("Data/ratings/6.csv",index_col= False, sep= ",", header= 0)
ratings_siete = pd.read_csv("Data/ratings/7.csv",index_col= False, sep= ",", header= 0)
ratings_ocho = pd.read_csv("Data/ratings/8.csv",index_col= False, sep= ",", header= 0)
# Generando un dataset "rating total" concatenando los 8 datasets.
ratings_total = pd.concat([ratings_uno, ratings_dos, ratings_tres, ratings_cuatro, ratings_cinco, ratings_seis, ratings_siete, ratings_ocho], axis= 0)
ratings_total.name = "rating"

# Creando las funciones para responder las consultas sugeridas.

# Consulta 1:
def generar_id(df= pd.DataFrame()):
    """
    Esta función crea la nueva columna "id" en el dataframe.
    """
    if df.name == "Amazon":
        df["id"] =  "a" + df["show_id"]
        df["plataforma"] = "amazon"
    elif df.name == "Disney":
        df["id"] =  "d" + df["show_id"]
        df["plataforma"] = "disney"
    elif df.name == "Hulu":
        df["id"] =  "h" + df["show_id"]
        df["plataforma"] = "hulu"
    elif df.name == "Netflix":
        df["id"] =  "n" + df["show_id"]
        df["plataforma"] = "netflix"

# Consulta 2:
def reemplazar_nulos(df= pd.DataFrame()):
    """
    Esta función reemplaza los valores nulos del campo rating por la letra "G" en el dataframe.
    """
    df["rating"] = df["rating"].replace(np.nan,"G") 

# Consulta 3
# Consulta 3.1:
def formato_fecha1(df= pd.DataFrame(),campo= str()):
    """
    Esta función normalizará en el formato fecha: "AAAA-mm-dd", del campo solicitado en el dataframe.
    """
    if (df.name == "rating") & (campo == "timestamp"):
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit='s').dt.strftime('%Y-%m-%d')
        df["timestamp"] = pd.to_datetime(df["timestamp"])
    
# Consulta 3.2:
def formato_fecha2(df= pd.DataFrame(),campo= str()):
    """
    Esta función normalizará en el formato fecha: "AAAA-mm-dd", del campo solicitado en el dataframe.
    """
    df[campo] = pd.to_datetime(df[campo]).dt.strftime('%Y- %m- %d')

# Consulta 4:
def minuscula(df= pd.DataFrame()):
    """
    Esta función modificará sin excepción alguna todos los campos de texto en minúscula en el dataframe.
    """
    for campo in df.columns.values.tolist():
        df[campo] = df[campo].apply(str).str.lower()

# Consulta 5:
def separar_duration(df= pd.DataFrame()):
    """
    Esta función separa el campo "duration" en dos campos: "duration_int" y "duration_type" en el dataframe.
    """
    separar = df["duration"].str.split(' ', n=1, expand= True)
    df["duration_int"] = separar[0]
    df["duration_type"] = separar[1] 
    df["duration_type"] = df["duration_type"].str.replace("seasons", "season")


# Normalizando con las funciones el dataset "ratings_total"
formato_fecha1(ratings_total,"timestamp")  
ratings_total = ratings_total.groupby("movieId").agg(np.mean).rating.round(decimals=1).to_dict()

# Normalizando con las funciones los dataset de las plataformas.
generar_id(Amazon)
generar_id(Disney)
generar_id(Hulu)
generar_id(Netflix)

# Concatenamos los datasets de las plataformas en un dataset general y aplicamos las funciones.
plataforma_streaming = pd.concat([Amazon, Disney, Hulu, Netflix], axis= 0)
plataforma_streaming.drop("show_id", axis= 1, inplace= True)

reemplazar_nulos(plataforma_streaming)
formato_fecha2(plataforma_streaming,"date_added") 
minuscula(plataforma_streaming)
separar_duration(plataforma_streaming)
plataforma_streaming.drop("duration", axis= 1, inplace= True)

# Finalmente creamos el campo score.
plataforma_streaming["score"] = plataforma_streaming["id"].map(ratings_total) 

# Exportamos a un dataset final de nombre "data_general"
plataforma_streaming.to_csv("data_general.csv", index= False)

print("ACABAMOS EL ETL")

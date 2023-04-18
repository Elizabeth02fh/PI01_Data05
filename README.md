# PI_Henry

## Proyecto Individual - MLOPS

Alumno: José Luis Martínez Chávez


> En este README encontrarán toda la documentación, e instrucciones necesarias, para poder utilizar la API y el Sistema de Recomendación que se  solicitó desarrollar.


**MENU:** 
 _dataset de las 4 plataformas y los 8 rating._ en _"https://drive.google.com/drive/folders/1b49OVFJpjPPA1noRBBi1hSmMThXmNzxn"_
* **ETL.ipynb** - _notebook con las transformaciones pedidas._
* **EDA_1.ipynb** - _notebook con las transformaciones pedidas._
* **main.py** - _contiene el llamado de la APi._
* **README** - _Instrucciones de uso._
* **queries.py** - _contiene las funciones de las queries pedidas y el sistema de recomendación._
* **requirements.txt** - _dependencias necesarias para que funcione._
* **data_general.csv** - _data limpia que usamos para las consultas y para el sistema de recomedación._

**Las funciones que componen la API  y sus respectivas consutas deployadas en render**

-  Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN. <br>
https://pi-henry-t1tx.onrender.com/get_max_duration/2020/netflix/min
-  Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año. <br>
https://pi-henry-t1tx.onrender.com/get_score_count/amazon/3.4/2019.
-  Cantidad de películas por plataforma con filtro de PLATAFORMA. <br>
https://pi-henry-t1tx.onrender.com/get_count_platform/hulu
- Actor que más se repite según plataforma y año. <br>
https://pi-henry-t1tx.onrender.com/get_actor/disney/2020
- Cantidad de contenidos/productos que se publicó por país y año. <br>
https://pi-henry-t1tx.onrender.com/prod_per_county/movie/india/2018
-  Cantidad de contenidos/productos según el rating de audiencia dado. <br>
https://pi-henry-t1tx.onrender.com/get_contents/18%2B


**Machine Learning**


Ya los datos están limpios, investigamos las relaciones que hay entre las variables de los datasets, ver si hay outliers o anomalías , y ver si hay algún patrón interesante que valga la pena explorar en un análisis posterior, para ello realizamos un Análisis Exploratorio de Datos-EDA.

Por terminar desarrollamos nuestro Sistema de Recomendación. En este caso nos basamos en las librerías TfidfVectorizer  y linear_kernel


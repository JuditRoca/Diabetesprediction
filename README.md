# Predicción Salarios Data Science

![portada](Data/Portada2.jpg)

<p align="center">
  <a href="#Introducción">Introducción</a> •
  <a href="#Estructura-repositorio.">Estructura repositorio.</a> •
  <a href="#Variables.">Variables.</a> •
</p>  



<h2 id="Introducción"> :pencil: Introducción</h2>

En este repositorio buscaremos patrones y tendencias para comprender mejor la estructura salarial en este campo y crear un modelo que nos permita predecir los salarios. Los resultados podrían beneficiar tanto a los empleadores, ajustando sus políticas salariales, como a los profesionales que buscan oportunidades laborales. A través de visualizaciones y análisis estadísticos, revelaremos conocimientos clave sobre los salarios de los analistas de datos. Esto servirá como punto de partida para decisiones relacionadas con la compensación salarial.



<h2 id="Estructura-repositorio."> :floppy_disk: Estructura repositorio.</h2>

En la estructura de carpetas, se han incluido las siguientes secciones:

Carpeta "data": Contiene los archivos relacionados con los datos. La subcarpeta "raw" almacena el archivo original del dataframe. El archivo "processed_df.csv" contiene el dataframe procesado y listo para su uso. Los archivos "train.csv" y "test.csv" contienen los conjuntos de datos de entrenamiento y prueba respectivamente.

Carpeta "models": Contiene el modelo entrenado en formato pickle.

Carpeta "notebooks": Contiene los cuadernos Jupyter utilizados durante el desarrollo del proyecto. El cuaderno "01_EDA.ipynb" se utiliza para realizar el análisis exploratorio de los datos. El cuaderno "02_data_processing.ipynb" se utiliza para el procesamiento de los datos. El cuaderno "03_entrenamiento_modelo.ipynb" se utiliza para la creación y entrenamiento de diferentes modelos. El cuaderno "04_evaluacion_modelo.ipynb" se utiliza para evaluar los modelos y realizar comparaciones.

Carpeta "src": Contiene los archivos Python que contienen el código fuente para el procesamiento de datos, la creación del modelo y la evaluación. El archivo "data_processing.py" contiene el código para procesar los datos y generar el archivo "processed_df.csv". El archivo "model.py" contiene el código para crear, entrenar y guardar el modelo en la carpeta "models". El archivo "evaluation.py" contiene el código para evaluar el modelo entrenado utilizando el archivo "test.csv".

Carpeta "docs": Contiene los materiales para presentación de proyecto tanto al equipo técnico como a la empresa.

Archivo "README.md": Este es el archivo principal que proporciona información general sobre el proyecto, incluyendo la descripción de la estructura de carpetas y otras instrucciones o notas relevantes.


<h2 id="Variables."> :book: Variables.</h2>

En este proyecto hemos trabajado conlas siguientes variables:

work_year: El año en que se pagó el salario.

experience_level: El nivel de experiencia en el trabajo durante el año.

EN se refiere a nivel de entrada/junior.
MI se refiere a nivel intermedio.
SE se refiere a nivel senior/experto.
EX se refiere a nivel ejecutivo/director.

employment_type: El tipo de empleo para el puesto.

PT se refiere a medio tiempo.
FT se refiere a tiempo completo.
CT se refiere a contrato.
FL se refiere a trabajo independiente.

job_title: El puesto en el que se trabajó durante el año.

salary: El monto total del salario bruto pagado.

salary_currency: La moneda del salario pagado, en formato de código de moneda ISO 4217.

salaryinusd: El salario en USD.

employee_residence: El país de residencia principal del empleado durante el año de trabajo, en formato de código de país ISO 3166.

remote_ratio: La cantidad general de trabajo realizado de forma remota.

company_location: El país de la oficina principal del empleador o sucursal contratante.

company_size: El número medio de personas que trabajaron para la empresa durante el año.


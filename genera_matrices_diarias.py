#Este es un codigo al que al entregarle un archivo .dat.gz de tipo binario
#realiza un recorte de la region de sudamerica y genera un archivo .npz que 
#contiene informacion.

#Un array con:
############# #Un array bidimensional con la precipitacion
############# #Un array con los valores de latitudes
############# #Un array con los valores de longitudes

#Librerias
import gsmap_tool as gsmap 
import os
from datetime import datetime
import numpy as np


#-------------Cargar archivo--------------------------------------

#Archivo .grib que deseamos leer
file = "gsmap_gauge.20230727.0.1d.daily.00Z-23Z.v8.0000.0.dat.gz"

#Carpeta donde se encuentra el archivo
folder = '/home/fernando.huaranca/datos/Datos_GSMAP/daily_G_v8'

#Ruta del archivo
path = os.path.join(folder,file)

#----------Limites--para-el-subset--------------------------------

#Region de sudamerica

ini_lon=260.0
end_lon=330.0
ini_lat=-65.0
end_lat=15.0    

#------------Subset-del-archivo----------------------------------

#Utilizamos la funcion para realizar un subset
var = gsmap.read_gsmap_subset(path , ini_lon , end_lon , ini_lat , end_lat )



#----------Extraemos-variables-de-interes--------------------

#Matriz bidimensional de precipitaciones diarias
pp = var[0]

#Array con longitudes
lon = var[1]

#Array con latitudes
lat = var[2]

#Extraer la fecha del file

fecha_str = file.split('.')[1]
fecha_datetime = datetime.strptime(fecha_str, '%Y%m%d')

# Formatear la fecha como DD-MM-YYYY
name_file = fecha_datetime.strftime('%d-%m-%Y')

#-----------Output--------------------------

# Ruta completa del archivo donde guardar los datos
out_path = f'/home/fernando.huaranca/test_satellite/output_matriz_satelite/{name_file}.npz'

# Guardar los arreglos en el archivo

np.savez(out_path,pp_daily = pp, latitudes = lat,longitudes = lon,name = name_file)



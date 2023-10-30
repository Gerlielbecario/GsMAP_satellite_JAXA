

#--------Librerias---------------------

#Librerias
import gsmap_tool as gsmap 
import os
from datetime import datetime
import numpy as np

#-----------Cargar archivos------------------------

#Carpeta
#folder = '/home/fernando.huaranca/datos/Datos_GSMAP/testeo_septiembre_fallados'

#file = 'gsmap_gauge.20010122.0.1d.daily.00Z-23Z.v8.0000.0.dat.gz'

#----------Limites--para-el-subset--------------------------------

#Region de sudamerica

#ini_lon=260.0
#end_lon=330.0
#ini_lat=-65.0
#end_lat=15.0



#Ruta del archivo
#path = os.path.join(folder,file)

#Extraer la fecha del file

#fecha_str = file.split('.')[1]
#fecha_datetime = datetime.strptime(fecha_str, '%Y%m%d')

# Formatear la fecha como DD-MM-YYYY
#name_file = fecha_datetime.strftime('%d-%m-%Y')

#print(f'Leyendo {path}')


#------------Subset-del-archivo----------------------------------

#print(f'Realizando subset de {path}')
#Utilizamos la funcion para realizar un subset
#var = gsmap.read_gsmap_subset(path , ini_lon , end_lon , ini_lat , end_lat )

#print(f'Subset de {path} finalizado')
#----------Extraemos-variables-de-interes--------------------

#print(f'Se inicia la extraccion de variables de interes de {path}')
#Matriz bidimensional de precipitaciones diarias. Redondeamos
#pp = np.round(var[0],3)

#Array con longitudes
#lon = var[1]

#Array con latitudes
#lat = var[2]

#print(f'Se extrajo las variables de {path} correctamente')

    
#-----------Output--------------------------

#print(f'Se inicia la creacion de {name_file}.npz')

#Ruta completa del archivo donde guardar los datos
#out_path = f'/home/fernando.huaranca/datos/Datos_GSMAP/testeo_septiembre_fallados/{name_file}.npz'

# Guardar los arreglos en el archivo

#np.savez(out_path,pp_daily = pp, latitudes = lat,longitudes = lon,name = name_file)

#print(f'Archivo {name_file} creado y guardado correctamente')

#print('Termino el proceso')




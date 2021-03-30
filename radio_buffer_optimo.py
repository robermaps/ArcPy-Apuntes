# Este script genera buffers entidad por entidad 
# de una capa vectorial, incrementando su radio
# hasta que el valor de la suma de los píxeles 
# de otra capa que se encuentren en el buffer
# supere cierto umbral, momento en el que pasará
# a la siguiente entidad.
#
# El resultado es una nueva columna en la capa
# de entidades indicando el radio del buffer 
# necesario para superar dicho umbral para 
# cada entidad.
#

# Importación de módulos

import arcpy, os
from arcpy import env
from arcpy.sa import *

# Variables de entorno

ruta = 'C:\\ruta\\'

env.overwriteOutput = True
env.workspace = ruta
arcpy.CheckOutExtension("Spatial")

# Crear carpeta de resultados (si no existiera)

resultados = ruta + '\\resultados\\'

if os.path.exists(resultados):
    print("Ya existe la carpeta \'resultados\'")
else:
    os.mkdir(resultados)
    print("Directorio \'resultados\' creado")

# Capas de entidades y raster

entidades = 'capa.shp'
raster = Raster('capa.tif')

# Crear el campo que contendrá el valor del radio

nuevo_campo = 'radio'
listaCampos = arcpy.ListFields(entidades)
existencia = 0

for campo in listaCampos:
    if campo.name == nuevo_campo:
        existencia = 1

if existencia == 1:
    print('El campo ' + nuevo_campo + ' ya existe')
else:
    arcpy.AddField_management(entidades,nuevo_campo,'SHORT')
    print('El campo ' + nuevo_campo + ' ha sido creado')

# Variables locales

umbral = X
densidad = 0
distancia = 100
cursor = arcpy.UpdateCursor('capa.shp')
FID = 0



### Procesos ###

# Crear capa temporal de la que extraer las plantas

arcpy.MakeFeatureLayer_management(entidades, 'lyr')

# Bucle que calcule los buffers hasta obtener el valor de distancia necesario

for elemento in cursor:
    print('Evaluando la entidad número ' + str(FID))

    # Extracción de entidades
    expresion = '"FID" = ' + str(FID)
    arcpy.SelectLayerByAttribute_management('lyr', "NEW_SELECTION", expresion)

    # Bucle que calculará los distintos buffers para cada entidad
    while densidad < umbral:
        area = arcpy.Buffer_analysis('lyr', resultados + 'buffer_' + str(FID) + '_' + str(distancia) + '.shp', distancia, "FULL", "ROUND", "NONE", "", "PLANAR")

        # Extracción de píxeles
        recorte = arcpy.ExtractByMask(raster, area)
        recorte_archivo = resultados + 'recorte_' + str(FID) + '_' + str(distancia) + '.tif'
        recorte.save(recorte_archivo)

        # Cálculo de productividad
        evaluar = Raster(recorte_archivo)
        raster_matriz = arcpy.RasterToNumPyArray(evaluar, nodata_to_value=0)
        densidad = raster_matriz.sum()
        print('Productividad para un radio de ' + str(distancia) + ' metros...')
        print(densidad)

        # Aumento del radio del buffer
        distancia += 100

        # Acciones a realizar tras hallar el radio
        if densidad >= umbral:
            planta.radio = distancia - 100
            cursor.updateRow(elemento)
            FID += 1
            distancia = 100
            densidad = 0
            break


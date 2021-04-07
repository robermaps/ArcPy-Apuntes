## Este script convierte el raster de entrada en una matriz
## o tabla de numpy para realizar operaciones sobre ella
##

# Modulos
import arcpy, numpy
from arcpy import env

# Entorno
ruta = 'C:\\...'
env.workspace = ruta
env.overwriteOutput = True

# Cargar raster y convertirlo en matriz 
capa_raster = raster('MDT.tif')
raster_matriz = arcpy.RasterToNumPyArray(capa_raster,nodata_to_value=0)

## OPERACIONES CON METODOS DE NUMPY ##
# Sumar todos los valores de los pixeles
raster_matriz.sum()
 
# Extraer el valor minimo
raster_matriz.min()
 
# Extraer el valor maximo
raster_matriz.max()

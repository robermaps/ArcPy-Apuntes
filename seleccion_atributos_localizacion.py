## Este script combina una selección espacial con una selección 
## por atributos para obtener una nueva capa con las entidades
## comunes a ambas selecciones.
##
## El ejemplo se realiza con una hipotética capa de puntos con
## el arbolado de España y su altura en metros y una segunda capa
## con las provincias para obtener los árboles con más de 15m de
## altura en Toledo.
##

# Modulos
import arcpy
from arcpy import env

# Entorno
ruta = 'C:\\...'
env.workspace = ruta
env.overwriteOutput = True

# Cargar capas
arbolado = 'arbolado.shp'
provincias = 'provincias.shp'

# Creación de capas temporales
arcpy.MakeFeatureLayer_management(arbolado, "arbolado_temp") 
arcpy.MakeFeatureLayer_management(provincias, "toledo_temp") 

# Selección por atributos - obtener la provincia de Toledo
arcpy.SelectLayerByAttribute_management('toledo_temp', "NEW_SELECTION", '"NOMBRE" = \'Toledo\'')

# Selección espacial - arbolado de la provincia de Toledo 
arcpy.management.SelectLayerByLocation('arboles_lyr', 'WITHIN', 'toledo_temp', 'NEW_SELECTION')

# Selección por atributos - arbolado mayor de 15m
arcpy.SelectLayerByAttribute_management('arbolado_temp', "SUBSET_SELECTION", '"ALTURA" = 15')

# Guardar en capa nueva
arcpy.CopyFeatures_management('arboles_lyr', 'arboles_toledo_15m.shp')

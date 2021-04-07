## Ejemplos para listar las capas del directorio de trabajo establecido en 
## las variables de entorno en función de su nombre y su formato
#

# Modulos
import arcpy
from arcpy import env
 
# Entorno
ruta = 'C:\\...'
env.workspace = ruta


##### --- VECTORIAL --- #####

# Listar todas las capas vectoriales
arcpy.ListFeatureClasses()
 
# Listar solo las capas de puntos
arcpy.ListFeatureClasses(,'Point')
 
# Listar solo las capas de líneas
arcpy.ListFeatureClasses(,'Line')
 
# Listar solo las capas de polígonos
arcpy.ListFeatureClasses(,'Polygon')
 
# Listar solo las capas cuyo nombre empiece por 'Col'
arcpy.ListFeatureClasses('Col*')
 
# Listar solo las capas cuyo nombre termine por por 'egios'
arcpy.ListFeatureClasses('*egios')
 
# Listar solo las capas cuyo nombre coincida con 'Colegios'
arcpy.ListFeatureClasses('Colegios')
 
# Listar solo las capas cuyo nombre coincida con 'Colegios' y sean de tipo poligonal
arcpy.ListFeatureClasses('Colegios', 'Polygon')


##### --- RASTER --- #####

# Listar todos los rasters
arcpy.ListRasters()
 
# Listar solo los rasters de tipo TIFF
arcpy.ListRasters(,'tif')
 
# Listar solo los rasters GRID
arcpy.ListRasters(,'grid')
 
# Listar solo los rasters IMG
arcpy.ListRasters(,'img')
 
# Listar solo los rasters cuyo nombre empiece por 'Temp'
arcpy.ListRasters('Temp*')
 
# Listar solo las capas cuyo nombre termine por por 'maximas'
arcpy.ListRasters('*maximas')
 
# Listar solo las capas cuyo nombre coincida con 'Temperaturas maximas'
arcpy.ListRasters('Temperaturas maximas')
 
# Listar solo las capas cuyo nombre empiece por 'Temp' y sean de tipo TIFF
arcpy.ListRasters('Temp*', 'TIFF')

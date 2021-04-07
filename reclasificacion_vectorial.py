## Este script reclasifica los valores continuos de temperatura de una hipotetica
## capa de puntos que almacena estaciones meteorologicas para que pasen a ser valores discretos.
## Los nuevos valores se guardan en un campo nuevo.
##

# Modulos
import arcpy
from arcpy import env
 
# Entorno
ruta = 'C:\\...'
env.workspace = ruta
env.overwriteOutput = True

# Cargar capa y crear cursor
capa = 'estaciones_meteo.shp'
cursor = arcpy.UpdateCursor(capa)

# Crear campo nuevo
nuevo_campo = 'descripcion'
longitud_campo = 8
listaCampos = arcpy.ListFields(capa)
existencia = 0
for campo in listaCampos:
    if campo.name == nuevo_campo:
        existencia = 1
        
if existencia == 1:
    print('El campo ' + nuevo_campo + ' ya existe')
else:
    arcpy.AddField_management(capa, nuevo_campo, 'TEXT', '', '', longitud_campo)
    print('El campo ' + nuevo_campo + ' ha sido creado') 

# Reclasificacion
for fila in cursor:
    if fila.temperatura < 10:
        fila.descripcion = 'frio'
        cursor.updateRow(fila)
    elif fila.temperatura >= 10 AND fila.temperatura < 25:
        fila.descripcion = 'templado'
        cursor.updateRow(fila)
    else: 
        fila.descripcion = 'calido'
        cursor.updaterow(fila)
 
del cursor

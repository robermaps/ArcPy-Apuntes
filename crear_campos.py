# Este script comprueba si un campo existe, y si no lo crea
#

# Modulos
import arcpy
 
# Variables de entorno
ruta = 'C:\\...'
env.workspace = ruta
env.overwriteOutput = True

# Variables locales
nuevo_campo = 'nombre_campo'
capa = 'nombre_capa.shp'
listaCampos = arcpy.ListFields(capa)
existencia = 0

# Comprobar si existe 
for campo in listaCampos:
    if campo.name == nuevo_campo:
        existencia = 1
        
# Si existe no hacer nada 
if existencia == 1:
    print('El campo ' + nuevo_campo + ' ya existe')
    
# Si no existe crearlo
else:
    arcpy.AddField_management(capa,nuevo_campo,tipo...)
    print('El campo ' + nuevo_campo + ' ha sido creado') 

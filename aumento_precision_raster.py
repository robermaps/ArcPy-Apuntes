## Este script permite aumentar la precisión de los datos de un ráster
## repartiendo el valor original de cada píxel entre los nuevos píxeles
## que genera el aumento de su resolución.
##

# Modulos
import arcpy
from arcpy import env

# Entorno
ruta = 'C:\\...'
env.workspace = ruta
env.overwriteOutput = True

# Cargar capa entrada
raster_entrada = Raster('capa.ext')

# Resoluciones
resolucion_1 = int(raster_entrada.meanCellWidth)
print('La resolución del ráster de entrada es ' + str(resolucion_1))
resolucion_2 = 0 # No tocar

# Función para obtener el número de píxeles que rellenará cada píxel
# del ráster de entrada
def numpix(lado1, lado2):
    resultado = lado1 ** 2 / lado2 ** 2
    print('Cada píxel se dividió en ' + str(resultado))
    return resultado

# Obtención de múltiplos
resol_propuesta = []

for i in range(0, resolucion_1):
    try:
        if resolucion_1 % i == 0 and resolucion_1 % i == 0:
            resol_propuesta.append(i)
    except:
        continue

print('Puede cambiar la resolución a cualquiera de las siguientes: ', resol_propuesta)

# Nueva resolución
while True:
    try:
        resolucion_2 = input('Introduce la nueva resolución: ')
        if resolucion_2 not in resol_propuesta:
            print('ERROR - Introduzca solo alguna de las siguientes resoluciones: \n', resol_propuesta)
            continue
        else:
            break
    except:
        print('ERROR - Asegúrese de introducir un valor numérico coincidente con los propuestos')
        continue

# Aumento de la resolución
print('Aumentando la resolución a ' + str(resolucion_2))
arcpy.Resample_management(raster_entrada, ruta + 'raster_temp.tif', str(resolucion_2), 'NEAREST')
raster_temp = Raster(ruta + 'raster_temp.tif') / numpix(resolucion_1, resolucion_2)
raster_temp.save(ruta + 'raster_' + str(resolucion_2) + '.tif')
nuevo_raster = Raster(ruta + 'raster_' + str(resolucion_2) + '.tif')
 

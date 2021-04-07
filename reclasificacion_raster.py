## Este script contiene ejemplos para reclasificar datos raster
## de distintas formas según el resultadon esperado
##

# Modulos
import arcpy
from arcpy import env
from arcpy.sa import *
 
# Entorno
ruta = 'C:\\...'
env.workspace = ruta
env.overwriteOutput = True
arcpy.CheckOutExtension("Spatial")

# Cargar capa y calcular estadisticas
capa = Raster('capa.extension')
arcpy.CalculateStatistics_management(capa)

## ---------------------Ejemplos-------------------------

## Los pixeles del raster de entrada que superen el valor de la variable 'umbral' 
## pasaran a tener valor 1 y el resto 0 en una capa nueva 
umbral = x
reclasificacion = capa > valor
reclasificacion.save('capa_reclas.tif')

## Todos los pixeles de la capa son multiplicados por el valor  
## de la variable 'factor' y se guarda en una capa nueva
factor = 3.6
conversion = capa * factor
conversion.save('capa_conversion.tif')

## ASPECT - los valores entre 45 y 135 grados de un mapa de orientaciones 
## pasan a tener valor 1, creando con ello una capa con los valores este solo
orientacion_este = (Raster('aspect.tif') > 45) & (Raster('aspect.tif') < 135)
orientacion_este.save('aspect_este.tif')

## ORIENTACION y PENDIENTES - los pixeles con valor entre 300 y 500 metros de altitud 
## y que además tienen una pendiente superior a 5 grados (segun unidades de la capa) 
## pasan a tener valor 1 en una nueva capa
altitud_pendientes = (Raster('MDT.tif') > 300) & (Raster('MDT.tif') < 500 & (Raster('slope.tif') > 5)
altitud_pendientes.save('reclasificacion.tif')
                                                
## RECLASIFICACION CATEGORIZADA POR VALOR - asigna un nuevo valor a cada pixel que posea el valor indicado 
lista = [1,2,3]                                              
reclasificacion = Reclassify(capa, "Value", RemapValue([[100,lista[0]],[200,lista[1]],[300,lista[2]]]))
reclasificacion.save('raster_reclas.tif')
                                                  
## RECLASIFICACION CATEGORIZADA POR RANGOS - asigna un nuevo valor a cada rango de datos establecido 
## En este ejemplo se han creado 3 intervalos a una distancia de 1000 unidades cada uno
lista = [5,10,15]                                                  
reclasificacion = Reclassify(capa, "Value", RemapRange([[0,1000,lista[0]],[1000,2000,lista[1]],[2000,3000,lista[2]]]))
reclasificacion.save('raster_reclas.tif')                                                  

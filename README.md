# Apuntes de ArcPy 
<img src="https://programapa.files.wordpress.com/2021/03/arcpy.png" width="300" height="200" text-align: center>
<p>Por Rober J</p>
<h2><strong>Introducción 🤓</strong></h2>
<details>
  <summary><strong>Python y ArcGIS</strong></summary><br>
  Python es un lenguaje de programación que puede usarse junto a los Sistemas de Información Geográfica (SIG) para ampliar sus funcionalidades mediante la automatización de geoprocesos, gestión avanzada de los datos y creación de nuevas herramientas (entre otras cosas), convirtiéndose en uno de los lenguajes favoritos para hacer toda clase de virguerías con la información geoespacial y no por casualidad: su facilidad de uso (relativa) y flexibilidad lo hace muy atractivo para usarlo en múltiples plataformas por usuarios no muy familiarizados con la programación informática.
Cada SIG cuenta con su propia librería de Python que permite acceder a los geoprocesos de dicho SIG. En este caso, ArcPy es la librería que da acceso a las funciones de ArcGIS en un entorno Python, dándonos acceso a las cajas de herramientas de geoprocesamiento estándar y a la posibilidad de usar otros módulos (siempre que tengamos licencia para usarlos)
¿Qué es lo que cambia? Parece contraintuitivo sustituir un amigable cuadro de texto por un churro de texto, pero gracias a ello accedemos a una herramienta mucho más flexible, ya que dentro de un script (un pequeño código) podemos diseñar qué se ejecuta, cuándo se ejecuta y con qué parámetros, encadenando unos procesos con otros y obteniendo resultados a nuestra medida.
  
  
  ![arcpy_clip](https://user-images.githubusercontent.com/81579458/142191380-5a3f7ba3-8a54-49af-81f6-3be5ba406011.png)
  Por ejemplo, ese ‘output’ que hemos especificado en la función arcpy.Clip podemos meterlo a continuación en otra función distinta, o en varias, y esos resultados pasarlos por otro geoproceso y así sucesivamente.
  
<br></details> 
<details>
  <summary><strong>Cómo comenzar a usar ArcPy</strong></summary><br>
  <p>Puede hacerse de varias maneras, principalmente:</p>
<p>A través de la <strong>ventana de Python incorporada en ArcMap</strong>. Es una opción rápida para ejecutar pequeños scripts sin complicarnos demasiado, pero se queda corto puesto que su funcionalidad se reduce a la de escribir código o pegarlo desde otra fuente y ejecutarlo. </p>
<p>En este caso he ejecutado el Clip de la imagen anterior, recortando la red fluvial usando el polígono de un municipio cualquiera: </p>
<figure><img src="https://programapa.files.wordpress.com/2021/03/ventana_puthon_arcmap.png?w=1024" alt="" srcset="https://programapa.files.wordpress.com/2021/03/ventana_puthon_arcmap.png?w=1024 1024w, https://programapa.files.wordpress.com/2021/03/ventana_puthon_arcmap.png?w=150 150w, https://programapa.files.wordpress.com/2021/03/ventana_puthon_arcmap.png?w=300 300w, https://programapa.files.wordpress.com/2021/03/ventana_puthon_arcmap.png?w=768 768w, https://programapa.files.wordpress.com/2021/03/ventana_puthon_arcmap.png 1045w" sizes="(max-width: 1024px) 100vw, 1024px" /></figure>
<p>Haciendo uso de un <strong>entorno de desarrollo integrado (IDE)</strong>, es decir, un software diseñado para trabajar con código y que dispone de herramientas para hacernos la vida más fácil: predicción de texto, resalte de sintaxis, documentación instantánea, cambios múltiples&#8230;</p>
<p>Existen múltiples IDEs y es cosa de cada uno escoger el que le vaya bien. Personalmente he usado Microsoft Visual Studio Code y PyCharm, y me quedo con el segundo puesto que está diseñado específicamente para Python y me ha dado menos problemas a nivel general (todos tienen sus cosillas&#8230;)</p>
<figure ><img src="https://programapa.files.wordpress.com/2021/03/image.png?w=1024" alt="" class="wp-image-5364" srcset="https://programapa.files.wordpress.com/2021/03/image.png?w=1024 1024w, https://programapa.files.wordpress.com/2021/03/image.png?w=150 150w, https://programapa.files.wordpress.com/2021/03/image.png?w=300 300w, https://programapa.files.wordpress.com/2021/03/image.png?w=768 768w, https://programapa.files.wordpress.com/2021/03/image.png 1366w" sizes="(max-width: 1024px) 100vw, 1024px" /><figcaption><em>Aspecto de PyCharm</em></figcaption></figure>
<p>En cualquier caso, deberás configurar el IDE para que tenga acceso a los módulos de ArcGIS <strong>vinculándolo con el intérprete que ArcGIS trae por defecto</strong>. <strong>El intérprete es el programa que traduce el código de Python para que el ordenador pueda ejecutarlo</strong>, y el módulo ArcPy solo funcionará si se utiliza el IDE junto a este intérprete.</p>
<p>Generalmente, ArcGIS instala Python en una carpeta llamada Python27 en la raíz del disco duro (generalmente suele ser C:\\ ) por lo que habrá que buscar en esa carpeta el archivo <strong>python.exe</strong> y seleccionarlo como intérprete.</p>
  
  
  
<br></details> 
<details>
  <summary><strong>Obtener scripts de Model Builder</strong></summary><br>
  <p>Una forma de comenzar montar un código de Python para ArcGIS es utilizar Model Builder para conceptualizar el trabajo que queremos hacer y extraer de él las funciones de geoproceso que necesitaremos. </p>
<p>En el artículo <em><a href="https://programapa.wordpress.com/2021/02/23/analisis-ubicacion-vertedero/">Análisis de ubicación de un vertedero con Model&nbsp;Builder</a> </em>comento brevemente las ventajas y limitaciones que presenta Model Builder y sus semejanzas con Python. Pues bien, podemos exportar los modelos a archivos Python (archivos con extensión .py) y abrirlos con una IDE para editarlos.</p>
<p>Siguiendo con el ejemplo del Clip, he construido el modelo en Model Builder y lo he exportado de la siguiente manera:</p>
<figure ><img src="https://programapa.files.wordpress.com/2021/03/exportar_modelo.png?w=767" alt="" class="wp-image-5369" srcset="https://programapa.files.wordpress.com/2021/03/exportar_modelo.png 767w, https://programapa.files.wordpress.com/2021/03/exportar_modelo.png?w=150 150w, https://programapa.files.wordpress.com/2021/03/exportar_modelo.png?w=300 300w" sizes="(max-width: 767px) 100vw, 767px" /></figure>
<p>A continuación lo abro en un IDE y presenta el siguiente aspecto. Como comentaba, es muy interesante porque te da una <strong>estructura básica</strong> a partir de la cual continuar desarrollando el script, pero habrá que modificarlo para que funcione:</p>
<div><pre>
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# clip.py
# Created on: 2021-03-04 22:32:42.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------
# Import arcpy module
import arcpy
# Local variables:
Red_fluvial = "Red_fluvial"
seleccion = "seleccion"
output = "C:\\Users\\Roberto\\Documents\\ArcGIS\\Default.gdb\\output"
# Process: Clip
arcpy.Clip_analysis(Red_fluvial, seleccion, output, "")
</pre>
  
<br></details> 
<details>
  <summary><strong>Estructura de un script</strong></summary><br>
  <p>Del código anterior podemos diferenciar varias partes que funcionan a modo de esqueleto para un script:</p>
<ol><li>La <a rel="noreferrer noopener" href="https://programapa.wordpress.com/2021/01/23/fundamentos-de-python-1-variables-clases-funciones-y-metodos/#codificacion" target="_blank">codificación de caracteres</a> que va a usarse (utf-8)</li><li>Metadatos del archivo .py como su nombre o fecha de creación</li><li><strong>Importación del módulo arcpy</strong> (¡no olvidar!)</li><li><a rel="noreferrer noopener" href="https://programapa.wordpress.com/2021/01/23/fundamentos-de-python-1-variables-clases-funciones-y-metodos/#clases_y_variables" target="_blank">Variables</a> locales: conjunto de variables que definen los parámetros de los geoprocesos, como son las rutas de las capas de entrada (<em>Red_fluvial</em> y <em>seleccion</em>) y de salida (<em>output</em>) </li><li>Procesos: la parte del código que ejecutará las <a rel="noreferrer noopener" href="https://programapa.wordpress.com/2021/01/23/fundamentos-de-python-1-variables-clases-funciones-y-metodos/#metodos_y_funciones" target="_blank">funciones</a> de geoproceso haciendo uso de las variables que definimos en el punto anterior</li></ol>
<p>Sin embargo, esta estructura base <strong>no funcionará correctamente</strong> fuera del entorno de ArcMap porque no reconocerá las capas, por lo que tendremos que modificar las variables añadiendo una <a rel="noreferrer noopener" href="https://programapa.wordpress.com/2021/01/23/fundamentos-de-python-1-variables-clases-funciones-y-metodos/#rutas" target="_blank">ruta válida</a>. Además, aunque cambiemos la ruta, este script solo podrá ejecutarse 1 sola vez porque se generaría una capa con un nombre que ya existe, por lo que tendremos que asegurarnos de tener correctamente configurados algunos parámetros de <strong>variables de entorno</strong> como veremos a continuación.</p>
<div><figure><img src="https://programapa.files.wordpress.com/2021/03/estructura_arcpy.png?w=677" alt="" class="wp-image-5385" srcset="https://programapa.files.wordpress.com/2021/03/estructura_arcpy.png 677w, https://programapa.files.wordpress.com/2021/03/estructura_arcpy.png?w=150 150w, https://programapa.files.wordpress.com/2021/03/estructura_arcpy.png?w=300 300w" sizes="(max-width: 677px) 100vw, 677px" /></figure>
  
<br></details> 
  
<details>
  <summary><strong>Importación de módulos</strong></summary><br>
  
  <p>Antes de nada, tendremos que importar ArcPY junto al resto de módulos que vayamos a usar durante el script. Si, por ejemplo, vamos a querer que se cree automáticamente una nueva carpeta con el resultado, no se nos puede olvidar importar también el módulo os:</p>
<pre >
import arcpy, os
</pre>
<p>Importar arcpy tal como mostramos arriba da acceso a las siguientes funcionalidades (<em>fuente: <a rel="noreferrer noopener" href="https://desktop.arcgis.com/es/arcmap/10.3/analyze/python/importing-arcpy.htm" target="_blank">Esri</a></em>):</p>
<ul><li><a href="https://desktop.arcgis.com/es/arcmap/10.3/tools/analysis-toolbox/an-overview-of-the-analysis-toolbox.htm">Caja de herramientas de Análisis</a> (Analysis Tools)</li><li><a href="https://desktop.arcgis.com/es/arcmap/10.3/tools/cartography-toolbox/an-overview-of-the-cartography-toolbox.htm">Caja de herramientas Cartografía</a> (Cartography tools)</li><li><a href="https://desktop.arcgis.com/es/arcmap/10.3/tools/conversion-toolbox/an-overview-of-the-conversion-toolbox.htm">Caja de herramientas Conversión</a> (Conversion tools)</li><li><a href="https://desktop.arcgis.com/es/arcmap/10.3/tools/data-management-toolbox/an-overview-of-the-data-management-toolbox.htm">Caja de herramientas Administración de datos</a> (Data Management Tools)</li><li><a href="https://desktop.arcgis.com/es/arcmap/10.3/tools/editing-toolbox/an-overview-of-the-editing-toolbox.htm">Caja de herramientas Edición</a> (Editing Tools)</li><li><a href="https://desktop.arcgis.com/es/arcmap/10.3/tools/geocoding-toolbox/an-overview-of-the-geocoding-toolbox.htm">Caja de herramientas Geocodificación</a> (Geocoding Tools)</li><li><a href="https://desktop.arcgis.com/es/arcmap/10.3/tools/linear-ref-toolbox/an-overview-of-the-linear-referencing-toolbox.htm">Caja de herramientas Referencia lineal</a> (Linear Referencing Tools)</li><li><a href="https://desktop.arcgis.com/es/arcmap/10.3/tools/multidimension-toolbox/an-overview-of-the-multidimension-toolbox.htm">Caja de herramientas de Multidimensión</a> (Multidimension Tools)</li><li><a href="https://desktop.arcgis.com/es/arcmap/10.3/tools/spatial-statistics-toolbox/an-overview-of-the-spatial-statistics-toolbox.htm">Caja de herramientas Estadística espacial</a> (Spatial Statistics Analyst)</li></ul>
<p>Sin embargo, existen <strong>otros módulos</strong> que deben importarse a parte para acceder a más funciones de ArcGIS:</p>
<ul><li><a rel="noreferrer noopener" href="https://desktop.arcgis.com/es/arcmap/10.3/analyze/arcpy-data-access/what-is-the-data-access-module-.htm" target="_blank">arcpy.da</a> &#8211; módulo de acceso de datos</li><li><a rel="noreferrer noopener" href="https://desktop.arcgis.com/es/arcmap/10.3/analyze/arcpy-mapping/introduction-to-arcpy-mapping.htm" target="_blank">arcpy.mapping</a> &#8211; módulo de representación cartográfica</li><li><a rel="noreferrer noopener" href="https://desktop.arcgis.com/es/arcmap/10.3/analyze/arcpy-spatial-analyst/what-is-the-spatial-analyst-module.htm" target="_blank">arcpy.sa</a> &#8211; módulo del Spatial Analyst</li><li><a rel="noreferrer noopener" href="https://desktop.arcgis.com/es/arcmap/10.3/analyze/arcpy-network-analyst/what-is-network-analyst-module.htm" target="_blank">arcpy.na</a> &#8211; módulo del Network Analyst </li><li><a rel="noreferrer noopener" href="https://desktop.arcgis.com/es/arcmap/latest/extensions/geostatistical-analyst/what-is-arcgis-geostatistical-analyst-.htm" target="_blank">arcpy.ga</a> &#8211; módulo del Geostatistical Analyst</li></ul>
<p>Para llevar a cabo las operaciones con geodatos vectoriales que presento a continuación se deben importar los siguientes módulos y definir las siguientes variables de entorno:</p>
<pre># Modulos
import arcpy
from arcpy import env
# Entorno
ruta = 'C:\\...'
env.workspace = ruta
env.overwriteOutput = True</pre>
<p>Para llevar a cabo las operaciones con datos ráster que presento a continuación se deben importar los siguientes módulos y definir las siguientes variables de entorno:</p>
<pre ># Modulos
import arcpy
from arcpy import env
from arcpy.sa import *
# Entorno
ruta = 'C:\\...'
env.workspace = ruta
env.overwriteOutput = True
arcpy.CheckOutExtension("Spatial")</pre>
  
  
<br></details>
<details>
  <summary><strong>Variables de entorno</strong></summary><br>
  <p>Las variables de entorno o <em>environments</em> son unos parámetros o funciones que conviene definir al comienzo del script (justo tras la importación de módulos) para que los geoprocesos funcionen de una u otra manera. Son, por así decirlo, &#8216;las reglas&#8217; que regirán el script.</p>
<p>Estas variables se encuentran dentro de la clase <em>env</em> de ArcPy. Son bastante numerosas y <a rel="noreferrer noopener" href="https://desktop.arcgis.com/es/arcmap/10.3/analyze/arcpy-classes/env.htm" target="_blank">podéis encontrarlas todas aquí</a>, pero los más básicos serían:</p>
<ul><li><strong>Directorio de trabajo</strong> &#8211; la carpeta en la que se localizan los geodatos. Definirlo es útil porque nos permitirá ahorrarnos el tener que escribir rutas completas en el futuro, es decir, podremos llamar a las capas solo por su nombre y su extensión, ya sean inputs u outputs. </li><li><strong>Sobreescritura de archivos</strong> &#8211; al definirla como <em>True</em> se borrarán de forma automática las capas antiguas que tengan el mismo nombre que una capa nueva que se acabe de generar. En nuestro ejemplo del Clip, al tener este parámetro activado el segundo Clip borraría el primero ya que el output en este caso tiene siempre el mismo nombre.</li><li><strong>Sistema de proyección</strong> &#8211; establecer el SRC de nuestro marco de datos. Al igual que en ArcMap, se proyectarán las capas &#8216;al vuelo&#8217; usando el SRC de la primera capa leída por nuestro script.</li><li><strong>Activación de extensiones</strong> &#8211; muchos geoprocesos como los del módulo Spatial Analyst se encuentran bajo licencia, por lo que deben activarse del mismo modo que hacemos en ArcMap &#8211; Customize &#8211; Extensions&#8230;</li></ul>
<pre >
# Definir el directorio de trabajo
arcpy.env.workspace = 'ruta'
# Activar la sobreescritura de archivos
arcpy.env.overwriteOutput = True
# Establecer el SRC al ETRS89 UTM Zona 30 Norte
arcpy.env.cartographicCoordinateSystem = "Coordinate Systems\Projected Coordinate Systems\UTM\Europe\ETRS 1989 UTM Zone 30N.prj"
# Activar la extensión Spatial Analyst
arcpy.CheckOutExtension('spatial') 
</pre>
<p>Entre otros entornos están el de establecer un SRC para las capas de salida, la resolución de las nuevas capas ráster, crear pirámides o el añadir las nuevas capas a la visualización.</p>
  
<br></details> 
<details>
  <summary><strong>Variables locales</strong></summary><br>
  <p>Como dijimos antes, son el conjunto de <a rel="noreferrer noopener" href="https://programapa.wordpress.com/2021/01/23/fundamentos-de-python-1-variables-clases-funciones-y-metodos/#clases_y_variables" target="_blank">variables</a> que usarán los geoprocesos para llevarse a cabo.  Suelen ser variables locales:</p>
<ul><li>Las rutas de las capas de entrada</li><li>Las rutas de las capas de salida</li><li>Filtros de archivos</li><li>Cálculos de valores </li><li>Expresiones <a href="https://programapa.wordpress.com/2021/02/01/fundamentos-de-sql-y-postgre/" target="_blank" rel="noreferrer noopener">SQL</a> para hacer selecciones</li><li>&#8230;</li></ul>
<p>Hay tantas variables variables locales como distintos geoprocesos que vayamos a utilizar y parámetros de éstos tengamos que introducir. Para la definición de estas variables, es habitual usar <a rel="noreferrer noopener" href="https://programapa.wordpress.com/2021/01/23/fundamentos-de-python-1-variables-clases-funciones-y-metodos/#inputs" target="_blank">inputs</a> para que sea el usuario el que las defina sobre la marcha. </p>
  
<br></details> 
<details>
  <summary><strong>Geoprocesos</strong></summary><br>
  <p>Es al final del script cuando deberíamos colocar los geoprocesos, puesto que éstos harán uso de las variables que hemos definido previamente.</p>
<p>La sintaxis de todos estos procesos se encuentran en la documentación oficial de Esri a la que podéis acceder a través de los enlaces del apartado Importación de módulos.</p>
<p>Algunas de las funciones de geoproceso más básicas de ArcPy son:</p>
<pre >
## Crear una capa temporal a partir de una capa existente
arcpy.MakeFeatureLayer_management('capa_entrada', 'lyr')
## Seleccionar entidades según sus atributos
arcpy.SelectLayerByAttribute_management('lyr', 'TIPO_SELECCION', 'expresión SQL')
## Copiar entidades a una nueva capa
arcpy.CopyFeatures_management('lyr', 'nueva_capa')
## CLIP
arcpy.Clip_analysis('capa_entrada', 'capa_clip', 'capa_salida', ' ')
## BUFFER 
arcpy.Buffer_analysis('capa_entrada', 'capa_salida', 'distancia', 'FULL', 'ROUND', 'NONE', ' ', 'PLANAR')
## CALCULATE STATISTICS (raster)
arcpy.CalculateStatistics_management('capa_entrada')
## RESAMPLE (modificar resolución)
arcpy.Resample_management('capa_entrada', 'capa_salida', 'nueva_resolución', 'MÉTODO')
</pre>
  
<br></details> 
<h2><strong>Datos vectoriales 📐</strong></h2>
<details>
  <summary><strong>Comprobar si un campo existe, y si no crearlo</strong></summary><br>
    
  <p>Para ello hay que usar la <strong>función<em> arcpy.ListFields()</em> para obtener una lista con objetos de tipo campo </strong>correspondientes a los campos de la tabla de atributos de una capa y comprobar su existencia. Si no existe, usar la función <em>arcpy.AddField_management()</em> para agregar el campo</p>
<pre >nuevo_campo = 'nombre_campo' 
capa = 'nombre_capa.shp'
listaCampos = arcpy.ListFields(capa)
existencia = 0
for campo in listaCampos:
    if campo.name == nuevo_campo:
        existencia = 1
if existencia == 1:
    print('El campo ' + nuevo_campo + ' ya existe')
else:
    arcpy.AddField_management(capa,nuevo_campo,tipo...)
    print('El campo ' + nuevo_campo + ' ha sido creado')   </pre>
    
<br></details>
<details>
  <summary><strong>Listar capas vectoriales de un directorio</strong></summary><br>
    
<p>La función ListFeatureClasses crea listas con los nombres de las capas junto a su extensión que se encuentran en el directorio de trabajo definido en las variables de entorno. Además, permite filtrarlas por nombre y tipo:</p>
<pre ># Listar todas las capas vectoriales
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
arcpy.ListFeatureClasses('Colegios', 'Polygon')</pre>
    
<br></details>
<details>
  <summary><strong>Crear capas temporales</strong></summary><br>
    
    
<p>Las capas temporales o capas layer que solo existen mientras se ejecuta el script y nos permiten hacer selecciones y otras operaciones sin modificar la capa original. El primer argumento es para la capa que vamos a 'duplicar' y el segundo para darle el nombre con el que se identificará durante el script:</p>
<pre >arcpy.MakeFeatureLayer_management("capa_entrada.shp", "capa_lyr") </pre>
<p>No es necesario indicar la extensión de la capa temporal. </p>
    
<br></details>
<details>
  <summary><strong>Seleccionar entidades por atributos y guardarlas en una capa nueva</strong></summary><br>
    
  <p>El siguiente código crea una nueva selección con los árboles que miden más de 15 metros y los guarda en un archivo nuevo.</p>
<pre >arcpy.MakeFeatureLayer_management("arboles.shp", "arboles_lyr") 
arcpy.SelectLayerByAttribute_management('arboles_lyr', "NEW_SELECTION", '"ALTURA" > 15')
arcpy.CopyFeatures_management('arboles_lyr', 'arboles_15m.shp'')</pre>
<p>En la documentación de Esri tenéis más detalles sobre la función <em><a rel="noreferrer noopener" href="https://pro.arcgis.com/es/pro-app/latest/tool-reference/data-management/select-layer-by-attribute.htm" target="_blank">SelectLayerByAttribute</a></em>  </p>
    
<br></details>
<details>
  <summary><strong>Seleccionar entidades por localización y guardarlas en una capa nueva</strong></summary><br>
    
  <p>También se pueden hacer selecciones espaciales basadas en las distintas <a href="https://programapa.wordpress.com/2020/11/13/relaciones-espaciales/">relaciones espaciales</a> entre entidades geográficas. En el siguiente ejemplo se seleccionan aquellos árboles que se encuentren <strong>dentro</strong> de una determinada parcela guardada como capa individual:</p>
<pre >arcpy.MakeFeatureLayer_management('arboles.shp', 'arboles_lyr') 
SelectLayerByLocation('arboles_lyr', 'WITHIN', 'parcela.shp', 'NEW_SELECTION')
arcpy.CopyFeatures_management('arboles_lyr', 'arboles_parcela.shp'')</pre>
<p> En la documentación de Esri tenéis más detalles sobre la función <em><a rel="noreferrer noopener" href="https://desktop.arcgis.com/es/arcmap/latest/tools/data-management-toolbox/select-layer-by-location.htm" target="_blank">SelectLayerByLocation</a></em> </p>
    
    
<br></details>
<details>
  <summary><strong>Cursores - acceder a las tablas de atributos</strong></summary><br>
    
  <p>Los cursores crean listas con objetos de tipo fila. Cada uno de estos objetos nos permite acceder a los valores de los distintos campos que contiene una fila.</p>
<p>Son necesarios para acceder a los registros de las tablas de atributos de nuestras capas. Hay 3 tipos:</p>
<ul><li><em><strong>arcpy.SearchCursor()</strong></em> es el cursor de búsqueda, válido para hacer consultas sin modificar valores</li><li><em><strong>arcpy.UpdateCursor()</strong></em> es el cursor de actualización necesario para hacer cambios en los registros existentes</li><li><em><strong>arcpy.InsertCursor()</strong></em> es el cursor para insertar nuevos registros en una tabla de atributos</li></ul>
<p>A continuación tenéis ejemplos del uso de los cursores:</p>
 
<h4><strong>Imprimir todos los valores de un campo</strong></h4>
<p>Para hacer esto hay que aplicar el <strong>cursor de búsqueda</strong> <em>arcpy.SearchCursor()</em> a la capa de la queramos leer la información y guardarlo como objeto. Después habrá que llamar a este objeto para que se imprima el campo indicado dentro de un bucle:</p>
<pre >cursor = arcpy.SearchCursor('nombre_capa.shp')
for fila in cursor:
    print(fila.nombre_campo)</pre>
<h4 id="modificar-todos-los-valores-de-un-campo"><strong>Modificar todos los valores de un campo</strong></h4>
<p>Para ello hay que guardar como objeto el <strong>cursor de actualización</strong> <em>arcpy.UpdateCursor()</em> aplicado a la capa que queremos modificar. Después deberemos pasarle a este objeto un bucle for o while.</p>
<p>En este caso se usa un <strong>bucle <em>for</em></strong> para <strong>cambiar todos los valores</strong> de un campo por el número 3:</p>
<pre >cursor = arcpy.UpdateCursor('nombre_capa.shp')
for fila in cursor:
    fila.campo = 3
    cursor.updateRow(fila)</pre>
<p>También se podría usar en su lugar un <strong>bucle while</strong>. Para que este bucle itere sobre cada fila hay que indicarle que vaya moviéndose a la siguiente posición del cursor a cada paso que da con el <strong>método .next</strong>. Cuando llega al final no devuelve ningún valor y el bucle se cierra:</p>
<pre >cursor = arcpy.UpdateCursor('nombre_capa.shp')
fila = cursor.next()
while fila:
    fila.campo = 3
    cursor.updateRow(fila)
    fila = cursor.next()</pre>
<p>Al acabar de hacer cambios se deberían <strong>eliminar los objetos</strong> creados para <strong>evitar errores</strong> en el almacenamiento de los nuevos valores:</p>
<pre >del cursor
del fila</pre>
<h4><strong>Reclasificar atributos</strong></h4>
<p>Se puede, por ejemplo, cambiar solo algunos valores, como por ejemplo los que sean mayores que 7 para que pasen a ser 0:</p>
<pre >cursor = arcpy.UpdateCursor('nombre_capa.shp')
for fila in cursor:
    if fila.prueba > 7:
        fila.prueba = 0
        cursor.updateRow(fila)
    else:
        continue
del cursor</pre>
<p>Además de modificar quirúrgicamente los valores que nos interesan de un campo concreto, podemos usar este procedimiento para <strong>reclasificar todos los valores</strong> de un campo, algo muy útil cuando queremos transformar variables continuas en discretas:</p>
<pre >cursor = arcpy.UpdateCursor('estaciones_meteo.shp')
for fila in cursor:
    if fila.temperatura &lt; 10:
        fila.descripcion = 'frío'
        cursor.updateRow(fila)
    elif fila.temperatura >= 10 AND fila.temperatura &lt; 25:
        fila.descripcion = 'templado'
        cursor.updateRow(fila)
    else: 
        fila.descripcion = 'cálido'
        cursor.updaterow(fila)
del cursor</pre>
    
<br></details>
<h2><strong>Datos ráster 🛰</strong></h2>
<details>
  <summary><strong>Listar y filtrar capas ráster</strong></summary><br>
    
  <p> La función ListRasters crea listas con los nombres de las capas junto a su extensión que se encuentran en el directorio de trabajo definido en las variables de entorno. Además, permite filtrarlas por nombre y tipo: </p>
<pre ># Listar todos los rasters
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
arcpy.ListRasters('Temp*', 'TIFF')</pre>
    
<br></details>
<details>
  <summary><strong>Obtener la resolución de una capa</strong></summary><br>
    
<p>Las unidades del valor devuelto variarán en función de la proyección de la capa (grados, metros...)</p>
<pre >capa_raster = Raster('MDT.tif')
resolucion = capa_raster.meanCellWidth</pre>
    
    
<br></details>
<details>
  <summary><strong>Calcular estadísticas</strong></summary><br>
   
  <p>Este geoproceso habilita a las capas ráster para aplicar posteriormente algunas herramientas de ArcPy y evitar el error 001100: <em>Failed because no statistics is available</em> </p>
<pre >arcpy.CalculateStatistics_management(capa_raster)</pre>
    
    
<br></details>
<details>
  <summary><strong>Obtener las coordenadas de los límites de la capa</strong></summary><br>
   
  <p>Con la función <strong>Point</strong> se puede obtener un <a rel="noreferrer noopener" href="https://desktop.arcgis.com/es/arcmap/10.3/analyze/arcpy-classes/point.htm" target="_blank">objeto de tipo punto</a> con los valores devueltos por los <strong>métodos .extent</strong>:</p>
<pre >capa_raster = Raster('MDT.tif')
limites = 'XMIN = {0}, XMAX = {1}, YMIN = {2}, YMAX = {3}'.format(capa.extent.XMin,capa.extent.XMax,capa.extent.YMin,capa.extent.YMax)
print(limites)</pre>
  
<p>Este código devolverá algo así: </p>
<p>XMIN = 569301.0, XMAX = 810701.0, YMIN = 4413136.0, YMAX = 4755136.0</p>
    
<br></details>
<details>
  <summary><strong>Reclasificar valores - álgebra de mapas</strong></summary><br>
    
  <p>Para <strong>realizar operaciones sobre los pixeles</strong> de un ráster se debe usar la <strong>función Raster()</strong> sobre la imagen que se quiere reclasificar y a continuación utilizar los<strong> operadores</strong> de Python para modificar los valores. </p>
<p>Hay que recordar que las reclasificaciones <strong>se guardan</strong> como variables que deben ser almacenadas en archivos nuevos usando el <strong>método .save()</strong></p>
<p>En el siguiente ejemplo se <strong>reclasifica</strong> un mapa de radiación solar generando una nueva imagen en la que los valores superiores a los 5 kWh/m2 pasen a tener valor 1 y el resto 0:</p>
<pre >reclasificacion = Raster('radiacion.tif') > 5
reclasificacion.save('radiacion_reclas.tif')</pre>
<p>También se pueden <strong>reconvertir las unidades</strong>, convirtiendo los kWh en megajulios multiplicando los valores por 3.6:</p>
<pre >conversion = Raster('radiacion.tif') * 3.6
conversion.save('radiacion_mjulios.tif')</pre>
<p>Además, se pueden <strong>usar varios operadores</strong> combinando consultas separadas por paréntesis. En el siguiente ejemplo se van a reclasificar los valores de un mapa de orientaciones para que los valores entre el noreste y el sureste (entre 45º y 135º) cambien a valor 1 y el resto sean 0:</p>
<pre >orientacion_este = (Raster('aspect.tif') > 45) &amp; (Raster('aspect.tif') &lt; 135)
orientacion_este.save('aspect_este.tif')</pre>
<p>Incluso se pueden <strong>combinar los datos de varias capas ráster</strong> para combinar variables distintas. Con este código pasarían a valer 1 los píxeles de un MDT que se encuentran entre los 300 y los 500 metros de altitud y que además se encuentren en una pendiente superior a los 5º tomada de otra capa ráster:</p>
<pre >altitud_pendientes = (Raster('MDT.tif') > 300) &amp; (Raster('MDT.tif') &lt; 500 &amp; (Raster('slope.tif') > 5)
altitud_pendientes.save('reclasificacion.tif')</pre>
<p>🗺 Nota: si se usan capas distintas éstas deben encontrarse en el mismo SRC, o si no los píxeles no coincidirán</p>  
    
<br></details>
<details>
  <summary><strong>Matrices</strong></summary><br>
    
  <p>Operar con matrices reduce el tiempo de procesado de las operaciones sobre capas ráster. Consiste en convertir la información del ráster, que es en sí una matriz de valores, en una matriz o 'tabla' con la que poder operar usando el <a rel="noreferrer noopener" href="https://numpy.org/doc/stable/user/index.html" target="_blank">módulo <strong>NumPy</strong></a> de Python (activado por defecto).</p>
<figure ><img src="https://programapa.files.wordpress.com/2021/03/image-1.png?w=273" alt="" class="wp-image-5498"/><figcaption><em><a href="https://docs.qgis.org/2.14/es/docs/gentle_gis_introduction/raster_data.html" target="_blank" rel="noreferrer noopener"></a></em></figcaption></figure>
Fuente: docs.qgis
<p>Para convertir una capa ráster en una matriz de <strong>NumPy</strong>, ArcPy posee la función <em>arcpy.RasterToNumPyArray()</em>. En el siguiente ejemplo se lleva a cabo dicha conversión especificando que los valores nulos del ráster tengan valor 0:</p>
<pre >capa_raster = raster('MDT.tif')
raster_matriz = arcpy.RasterToNumPyArray(capa_raster,nodata_to_value=0)</pre>
<p>Una vez hecho esto, podremos usar el objeto o variable raster_matriz que hemos creado para <strong>aplicarle los métodos</strong> propios del módulo <strong>NumPy</strong>. Tenéis a continuación ejemplos de operaciones usando algunos de estos métodos:</p>
<pre ># Sumar todos los valores de lo píxeles
raster_matriz.sum()
# Extraer el valor mínimo
raster_matriz.min()
# Extraer el valor máximo
raster_matriz.max()</pre>
    
<br></details>
<details>
  <summary><strong>Cambiar la resolución de una capa</strong></summary><br>
    
  <p>El siguiente código comprueba si el tamaño del píxel de una capa ráster supera un umbral que hayamos establecido. En tal caso, se creará una nueva imagen con la resolución establecida en dicho umbral:</p>
<pre >capa_raster = Raster('nombre_archivo.extensión')
umbral = X
resolucion = capa_raster.meanCellWidth
print('La resolución del ráster es ' + str(resolucion))
if resolucion > umbral:
      print('La resolución es demasiado baja. Aumentando la resolución a' + str(umbral) + ' metros' )
      arcpy.Resample_management(capa_raster,  'nombre_salida_' + str(umbral) + '.extensión', umbral, 'NEAREST')
      nuevo_raster = Raster('nombre_salida_' + str(umbral) + '.extensión')
else:
      print('Resolución óptima')</pre>
<p>En la documentación de Esri tenéis más detalles sobre la función <em><a href="https://pro.arcgis.com/es/pro-app/latest/tool-reference/data-management/resample.htm" target="_blank" rel="noreferrer noopener">Resample_management</a></em></p>
    
<br></details>
  
## ¡Sígueme!
[![](https://img.shields.io/badge/@progra_mapa-white?style=for-the-badge&labelColor=blue&logo=Twitter&logoColor=white)](https://twitter.com/progra_mapa)[![](https://img.shields.io/badge/PrograMapa-grey?style=for-the-badge&logo=wordpress)](https://programapa.wordpress.com)[![](https://img.shields.io/badge/Roberto-blue?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/robertojl)[![](https://img.shields.io/badge/@progra_mapa-white?style=for-the-badge&logo=instagram)](https://instagram.com/progra_mapa)

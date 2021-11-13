# Empezando con ArcPy 
<p>Siguiendo con el post sobre los <a href="https://programapa.wordpress.com/2021/03/06/arcpy-el-modulo-python-de-arcgis/" target="_blank" rel="noreferrer noopener">fundamentos de ArcPY</a>, la librería Python de ArcGIS, en esta entrada voy a resumir algunos de los procedimientos más comunes de los scripts que usan esta librería.</p>

[![](https://img.shields.io/badge/@progra_mapa-white?style=for-the-badge&labelColor=blue&logo=Twitter&logoColor=white)](https://twitter.com/progra_mapa)[![](https://img.shields.io/badge/PrograMapa-grey?style=for-the-badge&logo=wordpress)](https://programapa.wordpress.com)[![](https://img.shields.io/badge/Roberto-blue?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/robertojl)[![](https://img.shields.io/badge/@progra_mapa-white?style=for-the-badge&logo=instagram)](https://instagram.com/progra_mapa)



<h3 class="indice"><strong>Índice</strong></h3>

<p><strong>Datos vectoriales</strong><br>&nbsp; &nbsp;- <a href="#modulos_vectorial">Importación de módulos</a><br>&nbsp; &nbsp;- <a href="#campos">Comprobar si un campo existe, y si no crearlo</a><br>&nbsp; &nbsp;- <a href="#listar_vectorial">Listar capas vectoriales de un directorio</a><br>&nbsp; &nbsp;- <a href="#capas_temporales">Crear capas temporales</a><br>&nbsp; &nbsp;- <a href="#seleccion_atributos">Seleccionar entidades por atributos</a><br>&nbsp; &nbsp;- <a href="#seleccion_localizacion">Seleccionar entidades por localización</a><br>&nbsp; &nbsp;- <a href="#cursores">Cursores - acceder a la tabla de atributos</a><br>&nbsp; &nbsp;- <a href="#ver_valores">Imprimir valores de un campo</a><br>&nbsp; &nbsp;- <a href="#modificar_valores">Modificar valores de un campo</a><br>&nbsp; &nbsp;- <a href="#reclasificar_atributos">Reclasificación de atributos</a><br><strong>Datos ráster</strong><br>&nbsp; &nbsp;- <a href="#modulos_raster">Importación de módulos</a><br>&nbsp; &nbsp;- <a href="#listar_raster">Listar capas ráster de un directorio</a><br>&nbsp; &nbsp;- <a href="#obtener_resolucion">Obtener la resolución de una capa</a><br>&nbsp; &nbsp;- <a href="#calcular_estadisticas">Calcular estadísticas</a><br>&nbsp; &nbsp;- <a href="#obtener_limites">Obtener las coordenadas de los límites de una capa</a><br>&nbsp; &nbsp;- <a href="#reclasificar_raster">Reclasificar valores - álgebra de mapas</a><br>&nbsp; &nbsp;- <a href="#matrices">Matrices</a><br>&nbsp; &nbsp;- <a href="#cambiar_resolucion">Cambiar la resolución de una capa</a></p>

<br>


<h2 class="has-text-align-center" id="datos-vectoriales"><strong>Datos vectoriales</strong></h2>


<p><a id="modulos_vectorial"></a></p>

<!-- wp:heading {"textAlign":"center","level":3} -->

<h3 class="has-text-align-center" id="importacion-de-modulos"><strong>Importación de módulos</strong></h3>

<!-- /wp:heading -->

<!-- wp:paragraph -->

<p>Para llevar a cabo las operaciones con geodatos vectoriales que presento a continuación se deben importar los siguientes módulos y definir las siguientes variables de entorno:</p>

<!-- /wp:paragraph -->

<!-- wp:syntaxhighlighter/code {"language":"python"} -->

<pre class="wp-block-syntaxhighlighter-code"># Modulos

import arcpy

from arcpy import env

# Entorno

ruta = 'C:\\...'

env.workspace = ruta

env.overwriteOutput = True</pre>

<!-- /wp:syntaxhighlighter/code -->

<!-- wp:spacer {"height":20} -->

<div style="height:20px" aria-hidden="true" class="wp-block-spacer"></div>

<!-- /wp:spacer -->

<p><a id="campos"></a></p>

<!-- wp:heading {"textAlign":"center","level":3} -->

<h3 class="has-text-align-center" id="comprobar-si-un-campo-existe-y-si-no-crearlo"><strong>Comprobar si un campo existe, y si no crearlo</strong></h3>

<!-- /wp:heading -->

<!-- wp:paragraph -->

<p>Para ello hay que usar la <strong>función<em> arcpy.ListFields()</em> para obtener una lista con objetos de tipo campo </strong>correspondientes a los campos de la tabla de atributos de una capa y comprobar su existencia. Si no existe, usar la función <em>arcpy.AddField_management()</em> para agregar el campo</p>

<!-- /wp:paragraph -->

<!-- wp:syntaxhighlighter/code {"language":"python"} -->

<pre class="wp-block-syntaxhighlighter-code">nuevo_campo = 'nombre_campo' 

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

<!-- /wp:syntaxhighlighter/code -->

<!-- wp:spacer {"height":20} -->

<div style="height:20px" aria-hidden="true" class="wp-block-spacer"></div>

<!-- /wp:spacer -->

<p><a id="listar_vectorial"></a></p>

<!-- wp:heading {"textAlign":"center","level":3} -->

<h3 class="has-text-align-center" id="listar-capas-vectoriales-de-un-directorio"><strong>Listar capas vectoriales de un directorio</strong></h3>

<!-- /wp:heading -->

<!-- wp:paragraph -->

<p>La función ListFeatureClasses crea listas con los nombres de las capas junto a su extensión que se encuentran en el directorio de trabajo definido en las variables de entorno. Además, permite filtrarlas por nombre y tipo:</p>

<!-- /wp:paragraph -->

<!-- wp:syntaxhighlighter/code {"language":"python"} -->

<pre class="wp-block-syntaxhighlighter-code"># Listar todas las capas vectoriales

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

<!-- /wp:syntaxhighlighter/code -->

<!-- wp:spacer {"height":20} -->

<div style="height:20px" aria-hidden="true" class="wp-block-spacer"></div>

<!-- /wp:spacer -->

<p><a id="capas_temporales"></a></p>

<!-- wp:heading {"textAlign":"center","level":3} -->

<h3 class="has-text-align-center" id="crear-capas-temporales"><strong>Crear capas temporales</strong></h3>

<!-- /wp:heading -->

<!-- wp:paragraph -->

<p>Las capas temporales o <em><strong>capas layer</strong></em> que solo existen mientras se ejecuta el script y nos permiten hacer selecciones y otras operaciones sin modificar la capa original. El primer argumento es para la capa que vamos a 'duplicar' y el segundo para darle el nombre con el que se identificará durante el script:</p>

<!-- /wp:paragraph -->

<!-- wp:syntaxhighlighter/code {"language":"python"} -->

<pre class="wp-block-syntaxhighlighter-code">arcpy.MakeFeatureLayer_management("capa_entrada.shp", "capa_lyr") </pre>

<!-- /wp:syntaxhighlighter/code -->

<!-- wp:paragraph -->

<p>No es necesario indicar la extensión de la capa temporal. </p>

<!-- /wp:paragraph -->

<!-- wp:spacer {"height":20} -->

<div style="height:20px" aria-hidden="true" class="wp-block-spacer"></div>

<!-- /wp:spacer -->

<p><a id="seleccion_atributos"></a></p>

<!-- wp:heading {"textAlign":"center","level":3} -->

<h3 class="has-text-align-center" id="seleccionar-entidades-por-atributos-y-guardarlas-en-una-capa-nueva"><strong>Seleccionar entidades por atributos y guardarlas en una capa nueva</strong></h3>

<!-- /wp:heading -->

<!-- wp:paragraph -->

<p>El siguiente código crea una nueva selección con los árboles que miden más de 15 metros y los guarda en un archivo nuevo.</p>

<!-- /wp:paragraph -->

<!-- wp:syntaxhighlighter/code {"language":"python"} -->

<pre class="wp-block-syntaxhighlighter-code">arcpy.MakeFeatureLayer_management("arboles.shp", "arboles_lyr") 

arcpy.SelectLayerByAttribute_management('arboles_lyr', "NEW_SELECTION", '"ALTURA" > 15')

arcpy.CopyFeatures_management('arboles_lyr', 'arboles_15m.shp'')</pre>

<!-- /wp:syntaxhighlighter/code -->

<!-- wp:paragraph -->

<p>En la documentación de Esri tenéis más detalles sobre la función <em><a rel="noreferrer noopener" href="https://pro.arcgis.com/es/pro-app/latest/tool-reference/data-management/select-layer-by-attribute.htm" target="_blank">SelectLayerByAttribute</a></em>  </p>

<!-- /wp:paragraph -->

<!-- wp:spacer {"height":20} -->

<div style="height:20px" aria-hidden="true" class="wp-block-spacer"></div>

<!-- /wp:spacer -->

<p><a id="seleccion_localizacion"></a></p>

<!-- wp:heading {"textAlign":"center","level":3} -->

<h3 class="has-text-align-center" id="seleccionar-entidades-por-localizacion-y-guardarlas-en-una-capa-nueva"><strong>Seleccionar entidades por localización y guardarlas en una capa nueva </strong></h3>

<!-- /wp:heading -->

<!-- wp:paragraph -->

<p>También se pueden hacer selecciones espaciales basadas en las distintas <a href="https://programapa.wordpress.com/2020/11/13/relaciones-espaciales/">relaciones espaciales</a> entre entidades geográficas. En el siguiente ejemplo se seleccionan aquellos árboles que se encuentren <strong>dentro</strong> de una determinada parcela guardada como capa individual:</p>

<!-- /wp:paragraph -->

<!-- wp:syntaxhighlighter/code {"language":"python"} -->

<pre class="wp-block-syntaxhighlighter-code">arcpy.MakeFeatureLayer_management('arboles.shp', 'arboles_lyr') 

SelectLayerByLocation('arboles_lyr', 'WITHIN', 'parcela.shp', 'NEW_SELECTION')

arcpy.CopyFeatures_management('arboles_lyr', 'arboles_parcela.shp'')</pre>

<!-- /wp:syntaxhighlighter/code -->

<!-- wp:paragraph -->

<p> En la documentación de Esri tenéis más detalles sobre la función <em><a rel="noreferrer noopener" href="https://desktop.arcgis.com/es/arcmap/latest/tools/data-management-toolbox/select-layer-by-location.htm" target="_blank">SelectLayerByLocation</a></em> </p>

<!-- /wp:paragraph -->

<!-- wp:spacer {"height":20} -->

<div style="height:20px" aria-hidden="true" class="wp-block-spacer"></div>

<!-- /wp:spacer -->

<p><a id="cursores"></a></p>

<!-- wp:heading {"textAlign":"center","level":3} -->

<h3 class="has-text-align-center" id="cursores-acceder-a-las-tablas-de-atributos"><strong>Cursores - acceder a las tablas de atributos</strong></h3>

<!-- /wp:heading -->

<!-- wp:paragraph -->

<p>Los cursores crean listas con objetos de tipo fila. Cada uno de estos objetos nos permite acceder a los valores de los distintos campos que contiene una fila.</p>

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

<p>Son necesarios para acceder a los registros de las tablas de atributos de nuestras capas. Hay 3 tipos:</p>

<!-- /wp:paragraph -->

<!-- wp:list -->

<ul><li><em><strong>arcpy.SearchCursor()</strong></em> es el cursor de búsqueda, válido para hacer consultas sin modificar valores</li><li><em><strong>arcpy.UpdateCursor()</strong></em> es el cursor de actualización necesario para hacer cambios en los registros existentes</li><li><em><strong>arcpy.InsertCursor()</strong></em> es el cursor para insertar nuevos registros en una tabla de atributos</li></ul>

<!-- /wp:list -->

<!-- wp:paragraph -->

<p>A continuación tenéis ejemplos del uso de los cursores:</p>

<!-- /wp:paragraph -->

<!-- wp:spacer {"height":20} -->

<div style="height:20px" aria-hidden="true" class="wp-block-spacer"></div>

<!-- /wp:spacer -->

<p><a id="ver_valores"></a></p>

<!-- wp:heading {"level":4} -->

<h4 id="imprimir-todos-los-valores-de-un-campo"><strong>Imprimir todos los valores de un campo</strong></h4>

<!-- /wp:heading -->

<!-- wp:paragraph -->

<p>Para hacer esto hay que aplicar el <strong>cursor de búsqueda</strong> <em>arcpy.SearchCursor()</em> a la capa de la queramos leer la información y guardarlo como objeto. Después habrá que llamar a este objeto para que se imprima el campo indicado dentro de un bucle:</p>

<!-- /wp:paragraph -->

<!-- wp:syntaxhighlighter/code {"language":"python"} -->

<pre class="wp-block-syntaxhighlighter-code">cursor = arcpy.SearchCursor('nombre_capa.shp')

for fila in cursor:

    print(fila.nombre_campo)</pre>

<!-- /wp:syntaxhighlighter/code -->

<!-- wp:spacer {"height":20} -->

<div style="height:20px" aria-hidden="true" class="wp-block-spacer"></div>

<!-- /wp:spacer -->

<p><a id="modificar_valores"></a></p>

<!-- wp:heading {"level":4} -->

<h4 id="modificar-todos-los-valores-de-un-campo"><strong>Modificar todos los valores de un campo</strong></h4>

<!-- /wp:heading -->

<!-- wp:paragraph -->

<p>Para ello hay que guardar como objeto el <strong>cursor de actualización</strong> <em>arcpy.UpdateCursor()</em> aplicado a la capa que queremos modificar. Después deberemos pasarle a este objeto un bucle for o while.</p>

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

<p>En este caso se usa un <strong>bucle <em>for</em></strong> para <strong>cambiar todos los valores</strong> de un campo por el número 3:</p>

<!-- /wp:paragraph -->

<!-- wp:syntaxhighlighter/code {"language":"python"} -->

<pre class="wp-block-syntaxhighlighter-code">cursor = arcpy.UpdateCursor('nombre_capa.shp')

for fila in cursor:

    fila.campo = 3

    cursor.updateRow(fila)</pre>

<!-- /wp:syntaxhighlighter/code -->

<!-- wp:paragraph -->

<p>También se podría usar en su lugar un <strong>bucle while</strong>. Para que este bucle itere sobre cada fila hay que indicarle que vaya moviéndose a la siguiente posición del cursor a cada paso que da con el <strong>método .next</strong>. Cuando llega al final no devuelve ningún valor y el bucle se cierra:</p>

<!-- /wp:paragraph -->

<!-- wp:syntaxhighlighter/code {"language":"python"} -->

<pre class="wp-block-syntaxhighlighter-code">cursor = arcpy.UpdateCursor('nombre_capa.shp')

fila = cursor.next()

while fila:

    fila.campo = 3

    cursor.updateRow(fila)

    fila = cursor.next()</pre>

<!-- /wp:syntaxhighlighter/code -->

<!-- wp:paragraph -->

<p>Al acabar de hacer cambios se deberían <strong>eliminar los objetos</strong> creados para <strong>evitar errores</strong> en el almacenamiento de los nuevos valores:</p>

<!-- /wp:paragraph -->

<!-- wp:syntaxhighlighter/code {"language":"python"} -->

<pre class="wp-block-syntaxhighlighter-code">del cursor

del fila</pre>

<!-- /wp:syntaxhighlighter/code -->

<!-- wp:spacer {"height":20} -->

<div style="height:20px" aria-hidden="true" class="wp-block-spacer"></div>

<!-- /wp:spacer -->

<p><a id="reclasificar_atributos"></a></p>

<!-- wp:heading {"level":4} -->

<h4 id="reclasificar-atributos"><strong>Reclasificar atributos</strong></h4>

<!-- /wp:heading -->

<!-- wp:paragraph -->

<p>Se puede, por ejemplo, cambiar solo algunos valores, como por ejemplo los que sean mayores que 7 para que pasen a ser 0:</p>

<!-- /wp:paragraph -->

<!-- wp:syntaxhighlighter/code {"language":"python"} -->

<pre class="wp-block-syntaxhighlighter-code">cursor = arcpy.UpdateCursor('nombre_capa.shp')

for fila in cursor:

    if fila.prueba > 7:

        fila.prueba = 0

        cursor.updateRow(fila)

    else:

        continue

del cursor</pre>

<!-- /wp:syntaxhighlighter/code -->

<!-- wp:paragraph -->

<p>Además de modificar quirúrgicamente los valores que nos interesan de un campo concreto, podemos usar este procedimiento para <strong>reclasificar todos los valores</strong> de un campo, algo muy útil cuando queremos transformar variables continuas en discretas:</p>

<!-- /wp:paragraph -->

<!-- wp:syntaxhighlighter/code {"language":"python"} -->

<pre class="wp-block-syntaxhighlighter-code">cursor = arcpy.UpdateCursor('estaciones_meteo.shp')

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

<!-- /wp:syntaxhighlighter/code -->

<!-- wp:spacer {"height":20} -->

<div style="height:20px" aria-hidden="true" class="wp-block-spacer"></div>

<!-- /wp:spacer -->

<p><a id="raster"></a></p>

<!-- wp:heading {"textAlign":"center"} -->

<h2 class="has-text-align-center" id="datos-raster"><strong>Datos ráster</strong></h2>

<!-- /wp:heading -->

<p><a id="modulos_raster"></a></p>

<!-- wp:heading {"textAlign":"center","level":3} -->

<h3 class="has-text-align-center" id="importacion-de-modulos"><strong>Importación de módulos</strong></h3>

<!-- /wp:heading -->

<!-- wp:paragraph -->

<p>Para llevar a cabo las operaciones con datos ráster que presento a continuación se deben importar los siguientes módulos y definir las siguientes variables de entorno:</p>

<!-- /wp:paragraph -->

<!-- wp:syntaxhighlighter/code {"language":"python"} -->

<pre class="wp-block-syntaxhighlighter-code"># Modulos

import arcpy

from arcpy import env

from arcpy.sa import *

# Entorno

ruta = 'C:\\...'

env.workspace = ruta

env.overwriteOutput = True

arcpy.CheckOutExtension("Spatial")</pre>

<!-- /wp:syntaxhighlighter/code -->

<!-- wp:spacer {"height":20} -->

<div style="height:20px" aria-hidden="true" class="wp-block-spacer"></div>

<!-- /wp:spacer -->

<p><a id="listar_raster"></a></p>

<!-- wp:heading {"textAlign":"center","level":3} -->

<h3 class="has-text-align-center" id="listar-y-filtrar-las-capas-raster-del-directorio-de-trabajo"><strong>Listar y filtrar las capas ráster del directorio de trabajo</strong></h3>

<!-- /wp:heading -->

<!-- wp:paragraph -->

<p> La función ListRasters crea listas con los nombres de las capas junto a su extensión que se encuentran en el directorio de trabajo definido en las variables de entorno. Además, permite filtrarlas por nombre y tipo: </p>

<!-- /wp:paragraph -->

<!-- wp:syntaxhighlighter/code {"language":"python"} -->

<pre class="wp-block-syntaxhighlighter-code"># Listar todos los rasters

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

<!-- /wp:syntaxhighlighter/code -->

<!-- wp:spacer {"height":20} -->

<div style="height:20px" aria-hidden="true" class="wp-block-spacer"></div>

<!-- /wp:spacer -->

<p><a id="obtener_resolucion"></a></p>

<!-- wp:heading {"textAlign":"center","level":3} -->

<h3 class="has-text-align-center" id="obtener-la-resolucion-de-una-capa"><strong>Obtener la resolución de una capa</strong></h3>

<!-- /wp:heading -->

<!-- wp:paragraph -->

<p>Las unidades del valor devuelto variarán en función de la proyección de la capa (grados, metros...)</p>

<!-- /wp:paragraph -->

<!-- wp:syntaxhighlighter/code {"language":"python"} -->

<pre class="wp-block-syntaxhighlighter-code">capa_raster = Raster('MDT.tif')

resolucion = capa_raster.meanCellWidth</pre>

<!-- /wp:syntaxhighlighter/code -->

<!-- wp:spacer {"height":20} -->

<div style="height:20px" aria-hidden="true" class="wp-block-spacer"></div>

<!-- /wp:spacer -->

<p><a id="calcular_estadisticas"></a></p>

<!-- wp:heading {"textAlign":"center","level":3} -->

<h3 class="has-text-align-center" id="calcular-estadisticas"><strong>Calcular estadísticas</strong></h3>

<!-- /wp:heading -->

<!-- wp:paragraph -->

<p>Este geoproceso habilita a las capas ráster para aplicar posteriormente algunas herramientas de ArcPy y evitar el error 001100: <em>Failed because no statistics is available</em> </p>

<!-- /wp:paragraph -->

<!-- wp:syntaxhighlighter/code {"language":"python"} -->

<pre class="wp-block-syntaxhighlighter-code">arcpy.CalculateStatistics_management(capa_raster)</pre>

<!-- /wp:syntaxhighlighter/code -->

<!-- wp:spacer {"height":20} -->

<div style="height:20px" aria-hidden="true" class="wp-block-spacer"></div>

<!-- /wp:spacer -->

<p><a id="obtener_limites"></a></p>

<!-- wp:heading {"textAlign":"center","level":3} -->

<h3 class="has-text-align-center" id="obtener-las-coordenadas-de-los-limites-de-la-capa"><strong>Obtener las coordenadas de los límites de la capa</strong></h3>

<!-- /wp:heading -->

<!-- wp:paragraph -->

<p>Con la función <strong>Point</strong> se puede obtener un <a rel="noreferrer noopener" href="https://desktop.arcgis.com/es/arcmap/10.3/analyze/arcpy-classes/point.htm" target="_blank">objeto de tipo punto</a> con los valores devueltos por los <strong>métodos .extent</strong>:</p>

<!-- /wp:paragraph -->

<!-- wp:syntaxhighlighter/code {"language":"python"} -->

<pre class="wp-block-syntaxhighlighter-code">capa_raster = Raster('MDT.tif')

limites = 'XMIN = {0}, XMAX = {1}, YMIN = {2}, YMAX = {3}'.format(capa.extent.XMin,capa.extent.XMax,capa.extent.YMin,capa.extent.YMax)

print(limites)</pre>

<!-- /wp:syntaxhighlighter/code -->

<!-- wp:paragraph -->

<p>Este código devolverá algo así: </p>

<!-- /wp:paragraph -->

<!-- wp:paragraph {"align":"center","backgroundColor":"cyan-bluish-gray","fontSize":"small"} -->

<p class="has-text-align-center has-cyan-bluish-gray-background-color has-background has-small-font-size">XMIN = 569301.0, XMAX = 810701.0, YMIN = 4413136.0, YMAX = 4755136.0</p>

<!-- /wp:paragraph -->

<!-- wp:spacer {"height":20} -->

<div style="height:20px" aria-hidden="true" class="wp-block-spacer"></div>

<!-- /wp:spacer -->

<p><a id="reclasificar_raster"></a></p>

<!-- wp:heading {"textAlign":"center","level":3} -->

<h3 class="has-text-align-center" id="reclasificar-valores-algebra-de-mapas"><strong>Reclasificar valores - álgebra de mapas</strong></h3>

<!-- /wp:heading -->

<!-- wp:paragraph -->

<p>Para <strong>realizar operaciones sobre los pixeles</strong> de un ráster se debe usar la <strong>función Raster()</strong> sobre la imagen que se quiere reclasificar y a continuación utilizar los<strong> operadores</strong> de Python para modificar los valores. </p>

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

<p>Hay que recordar que las reclasificaciones <strong>se guardan</strong> como variables que deben ser almacenadas en archivos nuevos usando el <strong>método .save()</strong></p>

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

<p>En el siguiente ejemplo se <strong>reclasifica</strong> un mapa de radiación solar generando una nueva imagen en la que los valores superiores a los 5 kWh/m2 pasen a tener valor 1 y el resto 0:</p>

<!-- /wp:paragraph -->

<!-- wp:syntaxhighlighter/code {"language":"python"} -->

<pre class="wp-block-syntaxhighlighter-code">reclasificacion = Raster('radiacion.tif') > 5

reclasificacion.save('radiacion_reclas.tif')</pre>

<!-- /wp:syntaxhighlighter/code -->

<!-- wp:paragraph -->

<p>También se pueden <strong>reconvertir las unidades</strong>, convirtiendo los kWh en megajulios multiplicando los valores por 3.6:</p>

<!-- /wp:paragraph -->

<!-- wp:syntaxhighlighter/code {"language":"python"} -->

<pre class="wp-block-syntaxhighlighter-code">conversion = Raster('radiacion.tif') * 3.6

conversion.save('radiacion_mjulios.tif')</pre>

<!-- /wp:syntaxhighlighter/code -->

<!-- wp:paragraph -->

<p>Además, se pueden <strong>usar varios operadores</strong> combinando consultas separadas por paréntesis. En el siguiente ejemplo se van a reclasificar los valores de un mapa de orientaciones para que los valores entre el noreste y el sureste (entre 45º y 135º) cambien a valor 1 y el resto sean 0:</p>

<!-- /wp:paragraph -->

<!-- wp:syntaxhighlighter/code {"language":"python"} -->

<pre class="wp-block-syntaxhighlighter-code">orientacion_este = (Raster('aspect.tif') > 45) &amp; (Raster('aspect.tif') &lt; 135)

orientacion_este.save('aspect_este.tif')</pre>

<!-- /wp:syntaxhighlighter/code -->

<!-- wp:paragraph -->

<p>Incluso se pueden <strong>combinar los datos de varias capas ráster</strong> para combinar variables distintas. Con este código pasarían a valer 1 los píxeles de un MDT que se encuentran entre los 300 y los 500 metros de altitud y que además se encuentren en una pendiente superior a los 5º tomada de otra capa ráster:</p>

<!-- /wp:paragraph -->

<!-- wp:syntaxhighlighter/code {"language":"python"} -->

<pre class="wp-block-syntaxhighlighter-code">altitud_pendientes = (Raster('MDT.tif') > 300) &amp; (Raster('MDT.tif') &lt; 500 &amp; (Raster('slope.tif') > 5)

altitud_pendientes.save('reclasificacion.tif')</pre>

<!-- /wp:syntaxhighlighter/code -->

<!-- wp:paragraph {"backgroundColor":"light-green-cyan"} -->

<p class="has-light-green-cyan-background-color has-background">🗺 Nota: si se usan capas distintas éstas deben encontrarse en el mismo SRC, o si no los píxeles no coincidirán</p>

<!-- /wp:paragraph -->

<!-- wp:spacer {"height":20} -->

<div style="height:20px" aria-hidden="true" class="wp-block-spacer"></div>

<!-- /wp:spacer -->

<p><a id="matrices"></a></p>

<!-- wp:heading {"textAlign":"center","level":3} -->

<h3 class="has-text-align-center" id="matrices"><strong>Matrices</strong></h3>

<!-- /wp:heading -->

<!-- wp:paragraph -->

<p>Operar con matrices reduce el tiempo de procesado de las operaciones sobre capas ráster. Consiste en convertir la información del ráster, que es en sí una matriz de valores, en una matriz o 'tabla' con la que poder operar usando el <a rel="noreferrer noopener" href="https://numpy.org/doc/stable/user/index.html" target="_blank">módulo <strong>NumPy</strong></a> de Python (activado por defecto).</p>

<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":5498,"sizeSlug":"large","linkDestination":"none"} -->

<div class="wp-block-image"><figure class="aligncenter size-large"><img src="https://programapa.files.wordpress.com/2021/03/image-1.png?w=273" alt="" class="wp-image-5498"/><figcaption><em><a href="https://docs.qgis.org/2.14/es/docs/gentle_gis_introduction/raster_data.html" target="_blank" rel="noreferrer noopener"></a></em></figcaption></figure></div>

Fuente: docs.qgis

<p>Para convertir una capa ráster en una matriz de <strong>NumPy</strong>, ArcPy posee la función <em>arcpy.RasterToNumPyArray()</em>. En el siguiente ejemplo se lleva a cabo dicha conversión especificando que los valores nulos del ráster tengan valor 0:</p>

<!-- /wp:paragraph -->

<!-- wp:syntaxhighlighter/code {"language":"python"} -->

<pre class="wp-block-syntaxhighlighter-code">capa_raster = raster('MDT.tif')

raster_matriz = arcpy.RasterToNumPyArray(capa_raster,nodata_to_value=0)</pre>

<!-- /wp:syntaxhighlighter/code -->

<!-- wp:paragraph -->

<p>Una vez hecho esto, podremos usar el objeto o variable raster_matriz que hemos creado para <strong>aplicarle los métodos</strong> propios del módulo <strong>NumPy</strong>. Tenéis a continuación ejemplos de operaciones usando algunos de estos métodos:</p>

<!-- /wp:paragraph -->

<!-- wp:syntaxhighlighter/code {"language":"python"} -->

<pre class="wp-block-syntaxhighlighter-code"># Sumar todos los valores de lo píxeles

raster_matriz.sum()

# Extraer el valor mínimo

raster_matriz.min()

# Extraer el valor máximo

raster_matriz.max()</pre>

<!-- /wp:syntaxhighlighter/code -->

<!-- wp:spacer {"height":20} -->

<div style="height:20px" aria-hidden="true" class="wp-block-spacer"></div>

<!-- /wp:spacer -->

<p><a id="cambiar_resolucion"></a></p>

<!-- wp:heading {"textAlign":"center","level":3} -->

<h3 class="has-text-align-center" id="cambiar-la-resolucion-de-una-capa"><strong>Cambiar la resolución de una capa </strong></h3>

<!-- /wp:heading -->

<!-- wp:paragraph -->

<p>El siguiente código comprueba si el tamaño del píxel de una capa ráster supera un umbral que hayamos establecido. En tal caso, se creará una nueva imagen con la resolución establecida en dicho umbral:</p>

<!-- /wp:paragraph -->

<!-- wp:syntaxhighlighter/code {"language":"python"} -->

<pre class="wp-block-syntaxhighlighter-code">capa_raster = Raster('nombre_archivo.extensión')

umbral = X

resolucion = capa_raster.meanCellWidth

print('La resolución del ráster es ' + str(resolucion))

if resolucion > umbral:

      print('La resolución es demasiado baja. Aumentando la resolución a' + str(umbral) + ' metros' )

      arcpy.Resample_management(capa_raster,  'nombre_salida_' + str(umbral) + '.extensión', umbral, 'NEAREST')

      nuevo_raster = Raster('nombre_salida_' + str(umbral) + '.extensión')

else:

      print('Resolución óptima')</pre>

<!-- /wp:syntaxhighlighter/code -->

<!-- wp:paragraph -->

<p>En la documentación de Esri tenéis más detalles sobre la función <em><a href="https://pro.arcgis.com/es/pro-app/latest/tool-reference/data-management/resample.htm" target="_blank" rel="noreferrer noopener">Resample_management</a></em></p>

<!-- /wp:paragraph -->

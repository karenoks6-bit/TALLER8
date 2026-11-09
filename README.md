Ejercicio 1: Matrices de Ventas
¿Por qué resulta conveniente utilizar una matriz en lugar de cuatro listas independientes?

Respuesta: Utilizar una matriz (lista anidada) permite agrupar y organizar la información en una sola estructura bidimensional donde las filas representan a los vendedores y las columnas a las semanas. Esto simplifica la gestión de datos al no depender de múltiples variables independientes, facilitando el recorrido dinámico mediante ciclos anidados (for) para calcular totales, promedios y búsquedas de forma eficiente.

¿Qué diferencia existe entre recorrer una fila y recorrer una columna?

Respuesta: Recorrer una fila implica fijar el índice del vendedor i e iterar a través de todas las columnas j (semanas). Por el contrario, recorrer una columna consiste en fijar la semana j e iterar a través de todas las filas i (vendedores). En Python, el recorrido por filas es el acceso natural de las listas anidadas.

¿Qué sucede si se modifica un elemento de la matriz? ¿Cómo afecta esto a los resultados?

Respuesta: Dado que las listas en Python son estructuras mutables, al cambiar el valor en la posición matriz[i][j] la celda se actualiza directamente en memoria. Si los cálculos de totales por vendedor, totales por semana, promedios y valores máximos se recalculan tras la modificación, todos los resultados reflejarán de inmediato el impacto del nuevo valor introducido.

Ejercicio 2: Análisis de Participación en Cursos (Conjuntos)¿Por qué un conjunto es más apropiado que una lista para representar estudiantes inscritos sin duplicados?Respuesta: El tipo de dato conjunto (set) en Python garantiza por definición la unicidad de sus elementos, evitando datos repetidos sin necesidad de programar validaciones manuales. Además, la búsqueda e inserción en conjuntos opera en tiempo constante promedio gracias al uso interno de tablas hash.  

Si un estudiante se inscribe dos veces en el mismo curso, ¿qué sucede con la información almacenada?

Respuesta: El conjunto ignora automáticamente el segundo intento de inserción. La información almacenada se conserva intacta con una sola representación del nombre del estudiante, garantizando la integridad de la lista sin generar registros duplicados.

¿Cuál es la diferencia entre la unión y la diferencia simétrica?
Respuesta:Unión (A u B): Reúne a todos los estudiantes que pertenecen al Curso A, al Curso B o a ambos sin repetirlos.   Diferencia Simétrica (A (triangulo) B): Reúne a los estudiantes que están inscritos en exactamente uno de los dos cursos, excluyendo a aquellos que están matriculados simultáneamente en ambos (A n B).

¿En qué situaciones reales sería útil utilizar conjuntos para analizar información?

Respuesta: Es ideal para filtrado de usuarios únicos en plataformas web, análisis de audiencias compartidas entre dos productos en marketing, cruce de listas en auditorías de sistemas, control de acceso por roles y consolidación de datos en procesos ETL para bases de datos sin duplicaciones.

3. Explicación del Procedimiento UtilizadoEjercicio 1: Matriz de VentasRepresentación de datos: Se definió la matriz de ventas $V$ de dimensión $3 \times 4$ mediante una lista anidada list[list] donde cada sublista contiene los ingresos en millones por semana para cada vendedor. 

Procesamiento manual (sin librerías externas)
Se utilizaron estructuras de control anidadas for y acumuladores numéricos para sumar las filas (ventas por vendedor) y las columnas (ventas por semana).   
Se implementaron algoritmos de búsqueda del valor máximo mediante comparaciones secuenciales para identificar el vendedor con mayor rendimiento y la semana de mayor venta.   
Se calculó el promedio dividiendo la sumatoria global entre el total de celdas (3 * 4 = 12). 
Actualización: Se incluyó un bloque interactivo con manejo de excepciones try-except para solicitar al usuario la posición a modificar y actualizar la matriz en tiempo de ejecución.

Ejercicio 2: Análisis de Cursos con ConjuntosRepresentación de datos: Se declararon dos variables de tipo set (curso_A y curso_B) conteniendo los nombres de los estudiantes matriculados en cada asignatura.   
Operaciones algebraicas: Se aplicaron de forma directa los operadores de conjuntos nativos de Python:  
 Unión (|): Para consolidar el total de estudiantes diferentes.   
Intersección (&): Para hallar los inscritos en ambos cursos.   
Diferencia (-): Para identificar los pertenecientes de forma exclusiva al Curso A o al Curso B.   
Diferencia simétrica (^): Para filtrar quienes están en un solo curso.   
Inclusión (issubset()): Para evaluar si el Curso A es subconjunto del Curso B.   
Actualización dinámica: Se utilizó el método .add() para incorporar nuevos estudiantes y recalcular de forma transparente las relaciones entre conjuntos.

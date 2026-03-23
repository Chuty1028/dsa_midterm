# dsa_midterm

# Time Profiling: 

Los resultados de profiling muestran que la carga de la playlist es altamente eficiente tanto en tiempo como en memoria. En términos de rendimiento, se lograron cargar 100 canciones en aproximadamente 0.11 ms.

![alt text](image.png)

# Memory Profiling: 
En cuanto al uso de memoria, el consumo se mantiene estable en 28.8 MiB durante todo el proceso, sin incrementos significativos por operación, lo que sugiere que la estructura de datos (lista doblemente enlazada) está bien implementada y no genera sobrecarga adicional al insertar elementos.

![alt text](image-1.png)

# Shuffle: 

El mecanismo de shuffle no reorganiza físicamente la lista doblemente enlazada, sino que genera un arreglo de índices aleatorios que representan el orden de reproducción. Cuando el modo shuffle está activo, la navegación (next y previous) se realiza accediendo a nodos específicos mediante estos índices, utilizando la función get_node_at. Esto permite mantener intacta la estructura original de la playlist mientras se simula un orden aleatorio.

    - Activar shuffle (toggle_shuffle) tiene un costo de O(n) debido a la generación y mezcla de los índices.

    - La navegación (next / previous) en modo shuffle tiene un costo de O(n), ya que cada acceso a un nodo por índice requiere recorrer la lista desde el inicio.

    - En modo normal (sin shuffle), las operaciones next y previous son O(1), gracias a los punteros de la lista doblemente enlazada.

# Clonar repo y ejecutar el programa 

Para clonar y ejecutar el proyecto, primero abre una terminal y ejecuta `git clone https://github.com/tu-usuario/tu-repo.git` para descargar el repositorio; luego entra a la carpeta con `cd tu-repo`, verifica que tienes Python 3 instalado usando `python --version`, y finalmente ejecuta el programa con `python ll.py`, lo que iniciará la interfaz en la terminal donde podrás interactuar con la playlist (play, next, previous y shuffle).










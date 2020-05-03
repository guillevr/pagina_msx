# Proyecto Página MSC

**-** La aplicación debe tener una hoja de estilo. Para ello lo mejor es que busques una plantilla HTML/CSS: con lo que ya tienes la hoja de estilo y ...  
**-** Las plantillas que uses en la aplicación se heredarán de la plantilla base.html (esta plantilla la puedes crear a partir de la plantilla HTML que has buscado).  
**-** La plantilla base tendrá al menos dos bloques: uno para indicar el título y otro para poner el contenido.  
**-** La página principal tendrá una imagen con el logotipo MSX al pulsar sobre está imagen  nos llevará a a página /juegos.  
**-** La página /juegos nos mostrara un buscador, para ello pon un formulario con un cuadro de texto donde puedas poner el nombre de un juego que quieres buscar. Cuando pulséis el botón de buscar enviará la información a la página /listajuegos. El formulario enviará los datos con el método POST.  
**-** En la página /listajuegos (qué sólo se puede acceder por el método POST) aparecerán los juegos cuyo nombre empiezan por la cadena que hemos añadido al formulario. **-** Si no hemos indicado ninguna cadena mostrará toos los juegos.  
**-** La página /listajuegos mostrará una tabla generada dinámicamente a partir de los datos del fichero msx.json y la búsqueda que se haya realizado.  
**-** La tabla tendrá tres columnas: en la primera aparecerá el nombre, en la segunda el desarrollador y en la tercera habrá un enlace con la palabra “Detalle” que me llevará a la página del juego con la ruta /juego/<identificador>.  
**-** Como ves, estamos volviendo a hacer el patrón de diseño : Lista - detalle. La lista está en la página /listajuegos y el detalle está en la página /juego/<identificador> donde aparecerán todos los datos del juego que tenga ese identificador. Si el identificador no existe devolverá un 404. Tendrá un enlace que me devuelve a la página /juegos.  
**-** La aplicación hay que desplegarla en heroku  

> Hasta aquí es suficiente para sacar la mitad de los puntos que vale la práctica. Te propongo varias mejoras que irán sumando puntos al resultados final, tienes que hacerlas en orden y puede hacer las que quieras.
    1. Realizar la búsqueda utilizando una sola ruta: Es decir que en la página /juegos este el formulario de búsqueda y la lista de juegos seleccionado. La información del formulario se enviará a la misma página. No existirá la página /listajuegos.
    2. Como el protocolo HTTP no tiene estado, no es capaz de acordarse de los datos anteriores, por lo tanto cada vez que hagáis una búsqueda aparecerá la lista de juegos pero el formulario estará vacío, no recuerda lo que pusimos. Modifica el programa para que aparezca en el formulario la cadena que habías introducido en la búsqueda (Pista: tendrá que utilizar el atributo value del elemento input).
    3. Añade otro criterio de búsqueda, es decir vas a poder buscar por nombre y por categoría. Para buscar por categoría vas a generar dinámicamente una lista desplegable (elemento select) en el formulario con las categorías de los juegos). Por lo tanto podremos buscar un juego que empiece por una cadena de una determinada categoría.
    4. De la misma forma que en el apartado 1 programar la lista desplegable para que recuerde la opción elegida en la búsqueda. (Pista: Usar el atributo selected del elemento option del elemento select)
¿Qué debes entregar?
    1. La url del repositorio github donde has desarrollado el programa. Recuerda que debes hacer el programa poco a poco y que los cambios lo tienes que ir guardando con distintos commits.
    2. Debes entregar la URL de la aplicación funcionando en heroku.
    3. Entrega capturas de pantallas de las páginas de la aplicación desplegada en Heroku donde se vea todos los elementos que se han solicitado.
    4. Indica qué mejoras has desarrollado 

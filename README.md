# PythonApp_CalculoEnlace
Proyecto para la materia Diseño y Simulacion de Sistemas de Comunicacion (DSSC) - Ing Telecomunicaciones

<p align="center">
     <img src="https://github.com/chewydc/PythonApp_CalculoEnlace/blob/d98a9442f1ea4f042fb24683b0105259184f1431/Img/Equipo.JPG">
</p>

***
## Contenido
1. [Enunciado](#Enunciado)
2. [Introduccion](#Introduccion)
3. [Desarrollo](#Desarrollo) 
4. [Calculo de Enlace](#Calculo)
5. [Zona de Fresnel](#Fresnel)
6. [Propagacion en el Espacio Libre](#Propagacion-Espacio-Libre)
7. [Reflexiones](#Reflexiones)
8. [Atenuacion por Lluvia](#Atenuacion-por-Lluvia)
9. [Simulacion](#Simulacion)
10. [Conclusion](#Conclusion)


***
<a name="Enunciado"></a>
### Enunciado

1.  Objetivos
    * Desarrollar un sistemas de enlace.
    * Entender el comportamiento de las simulaciones
    * Desarrollar capacidades con herramientas de programación

2.  Trabajo      
Desarrolle un conjunto de librerías/funciones en un lenguaje de programación de scripting adecuado (se recomienda python), según las capacidades teóricas expuestas en clase.
A partir de la herramienta de Google Earth, también vista en clase, selecciones dos puntos donde podría instalar dos estaciones y desarrollar un enlace de radio. A partir de la selección de estos dos puntos B y A, obtenga el perfil del terreno utilizado y vuelque dichos valores sobre un archivo perfil.txt.
Enfunción de esto, determine el despeje de un enlace de RF en 4 GHz entre dos estaciones A y B distantes entre la distancia elegida, con un perfil del terreno obtenido
dentro del archivo de texto perfil.txt.
    * Calcule la mínima alturas de las antenas, considerando que el obstáculo no introduce perdidas, usando tramos de torres de 6 metros.
    * Determine a través del stdout del lenguaje de programación utilizado, el margen de Fading que se posee en este mismo enlace, en donde el PIRE es de 41dbm, si se posee antenas iguales en la recepción y transmisión con ganancia de 18dBi y un receptor con potencia mínima detectable de -95dbm.

***
<a name="Introduccion"></a>
### Introduccion
Se opto por desarrollar el trabajo en Python debido a la poca experiencia del grupo en dicho lenguaje. Se tomo mucha información de la web, como asi tambien extractos del codigo, por lo que se debe tomar con mucha precaucion el codigo aqui subido. 
Gran parte del abordaje a la solucion del problema planteado se logro con la página web [GPS Visualizer](https://www.gpsvisualizer.com/) que se complementó perfecto con los requerimientos pedidos y con el uso de la aplicación [Google Earth](https://earth.google.com/).
El script desarrollado busco ser amigable con el usuario, permitiendo vía consola ingresar y modificar alguna de las variables del estudio, como ser frecuencia de trabajo, la distancia entre torres, incluso el nombre del archivo de input se puede editar. No fuimos más lejos en este sentido para que la experiencia de uso no sea tediosa al tener que ingresar muchos valores, pero de requerir más campos no se podrían incluir rápidamente.

<a name="Desarrollo"></a>
### Desarrollo
Nuestro punto de partida consistió en armar el perfil topográfico entre dos ubicaciones cualesquiera (no teníamos un requerimiento puntual ni distancia prefijada). Optamos por simular y descargar varios enlaces punto a punto desde la herramienta Google Earth, dichos archivos nos servirían luego para testear que tan bien se comportaba nuestro script al modificarle el input.
De esta forma, luego de marcar los puntos en Google Earth, exportamos el trayecto lineal en formato KML. Descubrimos que, si bien la información de coordenadas fue simple conseguirla desde el software de Google, no lo fue la altura o perfil del terreno entre dichos puntos (pese a que se visualizaban correctamente, ver Figura 1).

<p align="center">
     <img src="https://github.com/chewydc/PythonApp_CalculoEnlace/blob/377beaf83d0e9eb3a70d5300b443d2b06e3f3d82/Img/Figura1.JPG">
</p>

Es por ello que recurrimos a una segunda herramienta, GPS Visualizer (Figura 2), la cual fue verdaderamente muy potente, no solo formateamos el archivo original extensión KML (del tipo xml) a un texto plano. Sino también que nos permitió agregar a cada punto la altura del terreno, para si entonces armar nuestro perfil.

<p align="center">
     <img src="https://github.com/chewydc/PythonApp_CalculoEnlace/blob/377beaf83d0e9eb3a70d5300b443d2b06e3f3d82/Img/Figura2.JPG">
</p>

Completados estos pasos, contamos con los archivos de input al script. Como mencionamos previamente optamos por utilizar Python para el armado del programa, por su simpleza y también como una oportunidad de trabajarlo (no contábamos con experiencia previa). La estructura del script general puede visualizarse en la Figura 4.
Tomamos algunos recaudos dentro del script, como por ejemplo un chequeo básico del ingreso por teclado de las variables, con un contador de error, al tercer error en el ingreso se toma un valor por defecto y sigue al siguiente paso. Dependiendo el caso es el chequeo, por ejemplo para el ingreso de la distancia entre torres, solo admite valores enteros y positivos, de lo contrario da error de ingreso y solicita nuevamente.
Este bucle de revisión, está ajustado al dato solicitado, y en el paso del ingreso del nombre de archivo, también se revisa que exista dicho archivo. (Ver figura 3)
Si bien revisamos estos bucles, generamos casuística y los testeamos, podremos encontrar  algún caso no contemplado donde el programa termine en un error durante su ejecución.

<p align="center">
     <img src="https://github.com/chewydc/PythonApp_CalculoEnlace/blob/377beaf83d0e9eb3a70d5300b443d2b06e3f3d82/Img/Figura3.JPG">
</p>
<p align="center">
     <img src="https://github.com/chewydc/PythonApp_CalculoEnlace/blob/377beaf83d0e9eb3a70d5300b443d2b06e3f3d82/Img/Figura4.JPG">
</p>

<a name="Calculo"></a>
### Calculo de Enlace

En los enlaces con línea de vista, la onda electromagnética viaja directamente sin obstrucciones entre la estación transmisora y la receptora. La línea de visión implica que la antena en un extremo del radio enlace debe visualizar la antena del otro extremo, marcando sobre el mapa una línea recta, siendo esta la línea de vista que va desde el punto inicial hasta el punto final del enlace.
Por lo tanto, en este análisis la onda electromagnética tiene que viajar desde el punto de transmisión y tiene que encontrarse libre de obstáculos con el objetivo de que la señal no se reduzca significativamente, de esta manera se calcula la primera zona de Fresnel, donde por lo menos el 60% debe estar esté libre de obstáculos (montañas, arboles, casas).

<a name="Fresnel"></a>
### Zona de Fresnel

Por consiguiente, se define Zona de Fresnel al volumen de espacio entre el emisor de una onda electromagnética y un receptor, de modo que el desfase de las ondas en dicho volumen no supere los 180º (60% libre de obstáculos), adoptando la forma de un elipsoide, a esta zona se le llama primera zona de Fresnel.
Es aquí donde se concentra la mayor potencia de la señal que viaja de la antena transmisora hacia la antena receptora, cuya primera zona de Fresnel por lo menos el 60% de ella tiene que estar libre de obstáculos de esta manera se garantiza que la señal llegue a la estación receptora con buena potencia para cumplir un enlace ideal. (Figura 5)

<p align="center">
     <img src="https://github.com/chewydc/PythonApp_CalculoEnlace/blob/377beaf83d0e9eb3a70d5300b443d2b06e3f3d82/Img/Figura5.JPG">
</p>

Para calcular la primera zona de Fresnel se utiliza la siguiente ecuación la cual describe una elipse:

![Image text](https://github.com/chewydc/PythonApp_CalculoEnlace/blob/377beaf83d0e9eb3a70d5300b443d2b06e3f3d82/Img/Ecuacion1.JPG)

Donde:
n = Constante de la zona de Fresnel (n=17,31)
Rf1: Radio de la primera zona de fresnel (m)
d1: Distancia desde el obstáculo al extremo emisor (m)
d2: Distancia desde el obstáculo al extremo receptor (m)
dt: Distancia total del enlace (m)
f: Frecuencia de transmisión del enlace (MHz)

<a name="Propagacion-Espacio-Libre"></a>
### Propagacion en el Espacio Libre

Este modelo se deduce de las ecuaciones de maxwell y permite calcular la potencia recibida a cierta distancia en condiciones ideales, es decir sin obstáculos de ninguna naturaleza. Se compone de una expression matemática que se utiliza para la propagación general de una señal. Este tipo de propagación define la cantidad de fuerza que la señal pierde durante la trayectoria entre transmisor y el receptor. La propagación del espacio libre depende de la frecuencia y la distancia del enlace.
El cálculo se realiza mediante la siguiente ecuación:

![Image text](https://github.com/chewydc/PythonApp_CalculoEnlace/blob/63735a4ee0713684da37ec5dda7923c1f7d14dfb/Img/Ecuacion2.JPG)

Pel (dB) = Pérdida de propagación en el espacio libre (dB)
f = Frecuencia (MHz)
d = Distancia total del enlace (Km)

<a name="Reflexiones"></a>
### Reflexiones

Otro de los problemas que presentan los radio enlaces microondas punto a punto son los desvanecimientos producidos por multitrayectos. Esto se realiza cuando una onda de radio puede llegar al receptor a través de múltiples trayectorias debido a la reflexión de las ondas superficies reflectoras (agua, rocas, árboles). La señal sufre interferencia que causan problemas en la recepción.
Un parámetro muy importante a tomar en cuenta en la propagación de una onda son sus reflexiones. Si la onda directa y la onda reflejada están defasadas 180° habrá lo que se llama desvanecimiento, esto se debe a las reflexiones del agua, por lo tanto para evitar el desvanecimiento especialmente en los enlaces que pasan por agua, se utiliza una altura adecuada en el tamaño de las torres donde la onda reflejada no se defase en su trayectoria con el fin de obtener un buen funcionamiento del enlace. (Ver Figura 6)

<p align="center">
     <img src="https://github.com/chewydc/PythonApp_CalculoEnlace/blob/377beaf83d0e9eb3a70d5300b443d2b06e3f3d82/Img/Figura6.JPG">
</p>

<a name="Atenuacion-por-Lluvia"></a>
### Atenuacion por Lluvia

Otro parámetro que se toma en cuenta en la propagación de la onda electromagnética es debido a los factores atmosféricos especialmente las producidas por lluvia. Por lo tanto es necesario calcular la atenuación producida por la lluvia, aunque la atenuación causada puede despreciarse para frecuencias por debajo de los 10 GHz. Para nuestro caso la frecuencia de trabajo es de 4GHz, si bien el script admite modificar este valor, no está contemplada esta atenuación en los cálculos, por lo que si se ingresa un valor superior no se tendrá en cuenta.

<a name="Simulacion"></a>
### Simulacion

En la figura 5 podemos apreciar algunos de los perfiles obtenidos. Estos archivos son leídos por nuestro script, le deberemos indicar el nombre correcto del archivo, el número de columna donde se encuentra los datos de la elevación del terreno (generalmente en la columna 3, también se excluye la primera fila reservada para los nombres de las columnas). (Ver figura 7)

<p align="center">
     <img src="https://github.com/chewydc/PythonApp_CalculoEnlace/blob/377beaf83d0e9eb3a70d5300b443d2b06e3f3d82/Img/Figura7.JPG">
</p>

Con los datos de los archivos de input, se genera un vector con los datos de altura. Finalmente se solicitan datos como la distancia entre torres y frecuencia de trabajo y se calculan los datos solicitados. En esta versión del script, no estamos tomando en consideración a la curvatura de la tierra en nuestros cálculos como tampoco posibles problemas de refracción.
Como resultado de la Simulación obtenemos:

<p align="center">
     <img src="https://github.com/chewydc/PythonApp_CalculoEnlace/blob/377beaf83d0e9eb3a70d5300b443d2b06e3f3d82/Img/Figura8.JPG">
</p>

En el siguiente grafico (Figura 9) se puede apreciar en el origen de coordenadas la Antena punto A y al final de coordenadas punto B (para este ejemplo corrimos el perfil PergaminoJunin). La líneas rojas y azules representan el área de Fresnel siendo la azul el área de como resultado de la simulación. Las líneas verdes corresponden al perfil del terreno.

<p align="center">
     <img src="https://github.com/chewydc/PythonApp_CalculoEnlace/blob/377beaf83d0e9eb3a70d5300b443d2b06e3f3d82/Img/Figura9.JPG">
</p>
<p align="center">
     <img src="https://github.com/chewydc/PythonApp_CalculoEnlace/blob/377beaf83d0e9eb3a70d5300b443d2b06e3f3d82/Img/Figura10.JPG">
</p>

<a name="Conclusion"></a>
### Conclusion

Resulto muy positiva la experiencia de trabajar en equipo en la formulación de este trabajo. Logramos familiarizarnos con un lenguaje de programación que actualmente se encuentra en pleno auge. Repasamos teoría vista en materias previas que ya muchos habíamos olvidado, por lo que requirió un esfuerzo el recordar los cálculos y ecuaciones.
En la figura 9 y 10 podemos apreciar como al variar la frecuencia de trabajo la zona de Fresnel varia. Siendo más pequeña al aumentar la frecuencia. Dato que nos da pistas que el cálculo realizado es correcto.
En cuanto al script, si bien no llega a ser un software completo de simulación, carece de algunas consideraciones en sus cálculos, como por ejemplo la atenuación por reflexión o la curvatura terrestre, sin embargo es una herramienta que se acerca mucho a lo que una herramienta de mercado arrojaría como resultado.


# Software de simulación de espacios en blanco de televisión

_Producto final de un estudio de simulación._

Specx es un software que permite la configuración de escenarios adecuados para la generación de variables aleatorias cada cierto tiempo de acuerdo con ciertas distribuciones de probabilidad identificadas en un proceso de muestreo realizado a las frecuencias de televisión digital en la ciudad de Villavicencio. El software realiza una la simulación de un proceso estocástico de tiempo sincrónico. Cuenta con las siguientes funcionalidades:

-Asignar a cada frecuencia entendida como una variable aleatoria, alguna de las distribuciones de probabilidad tratadas anteriormente, y configurar los parámetros necesarios de esta.

-Guardar y cargar archivos con las configuraciones realizadas para las distribuciones, con el fin de no repetir procesos. Los datos se almacenan en archivos con formato JSON.

-Fijar un tiempo de muestreo en minutos.

-La simulación solo se podrá iniciar en cuanto cada frecuencia tenga asignada y configurada una distribución de probabilidad.

-Pausar y reanudar la simulación en cualquier momento.

-Manipular el flujo del tiempo, lo que implica una escalización al tiempo de muestreo durante el proceso de simulación.

-Visualizar la secuencia de valores generados para cada frecuencia en una gráfica por individual que se actualiza en tiempo real.

-Guardar las gráficas construidas durante la simulación en formato PNG.

-Al final de la simulación, el programa genera un archivo de texto plano con información de los valores generados.

La finalidad con la que fue creado Specx es reforzar la información sobre los espacios en blanco de televisión que contienen las bases de datos como las que usa el protocolo [PAWS](https://tools.ietf.org/html/rfc7545). Información que brinda grandes oportunidades para un uso eficiente del espectro.

## Comenzando 🚀

_Estas instrucciones le permitirán obtener una copia del proyecto en funcionamiento en su máquina local:_

* Puede clonar el repositorio [aqui](https://github.com/danialeresbar/Simulation_EPI) o descargar las fuentes en un archivo comprimido.

* Ahora que tiene los fuentes de Specx, antes de ejecutar por primera vez el software debe tener instaladas las siguientes librerías y dependencias en su máquina o entorno virtual.

### Pre-requisitos 📋

_Specx está desarrollado completamente en Python._

### Python

En primer lugar, asegúrese de que Python 3 está instalado en su sistema. Puede verificar esto fácilmente abriendo la terminal e ingresando el comando python3. Si necesita instalarlo, en caso de usar Windows consulte la [página de inicio](https://www.python.org/downloads/) de Python, o instálelo con homebrew (brew install python3) en OS X, o su administrador de paquetes de Linux favorito:


### Instalación 🔧

_Lleve a cabo los siguientes pasos para poder ejecutar Specx con todas sus funcionalidades:_

Una vez instalada la versión de Python, lo siguiente es la instalación de las librerías que no so son nativas, para lo cual puede hacer uso del archivo "requirements.txt" ejecutando el siguiente comando:

```
pip install -r requirements.txt
```

## Ejecutando las pruebas ⚙️

_Para ejecutar Specx por primera vez sigue las siguientes instrucciones:_

* Dirígete por consola al directorio src con:

```
cd src
```

* Una vez allí, ejecuta el siguiente comando:

```
python main_window.py
```

Esto debería ser suficiente para iniciar el software y realizar las simulaciones deseadas

## Construido con 🛠️

_Para el desarrollo de Specx se utilizaron las siguientes herramientas_

* [Qt](https://doc.qt.io/) - El framework para interfaces gráficas de usuario

## Autores ✒️

_El equipo de trabajo que llevó a cabo el estudio de simulación, el cual hizo posible el desarrollo del software Specx está formado por las siguientes personas:_

* **Héctor Iván Reyes Moncayo** - *Formulación del problema y consideraciones al modelo* - [Director]()
* **Ángel Alfonso Cruz Roa** - *Modelo del sistema* - [Codirector]()
* **Daniel Alejandro Restrepo Barbosa** - *Proceso de muestreo y determinación de distribuciones de probabilidad, diseño y construcción de interfaces gráficas de usuario.* - [Analista]()
* **Siervo Francisco Rodríguez Castellanos** - *Codificación de algoritmos de simulación y optimización de rutinas* - [Desarrollador]()


## Licencia 📄

Este proyecto está bajo la Licencia [GPLv3](http://www.gnu.org/licenses/gpl-3.0.html).


## Expresiones de Gratitud 🎁

* A los directores de este proyecto. El doctor Ángel Cruz por sus aportes tan valiosos al modelo del sistema, sin el cual Specx no podría operar correctamente; además de la dedicación a la revisión de cada funcionalidad del software. El doctor Héctor Reyes por sus conocimientos en el área de telecomunicaciones y radiotransmisiones, ya que su idea de un radio tvws fue la que llevó al desarrollo de Specx.

* A Francisco Rodríguez por sus habilidades en el desarrollo, que permitieron la construcción de varios generadores de variables aleaotorias, así como la optimización en el uso de recursos por parte de la aplicación.

* A la universidad de los llanos por brindar sus espacios y material bibliográfico para el estudio de simulación realizado.

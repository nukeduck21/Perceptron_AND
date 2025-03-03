Simulador de Perceptrón - Compuerta AND
Descripción
Este proyecto es una aplicación web que simula una neurona artificial utilizando el algoritmo del perceptrón simple para modelar la compuerta lógica AND. La aplicación permite entrenar el perceptrón con datos predefinidos de la compuerta AND, realizar evaluaciones automáticas con entradas predefinidas, y aceptar valores reales personalizados ingresados por el usuario. Está implementada siguiendo el paradigma orientado a objetos, utilizando Python con Flask para la interfaz web, HTML/CSS para la presentación, y matplotlib para visualizar el aprendizaje mediante una gráfica del error por iteración.

El proyecto cumple con los siguientes requisitos:

Simular una neurona artificial mediante el perceptrón simple.
Entrenar el modelo con la base de conocimiento de la compuerta lógica AND.
Realizar evaluaciones automáticas con valores reales de entrada.
Seguir el paradigma orientado a objetos en su implementación.
Características
Interfaz Web Interactiva: Permite al usuario entrenar el perceptrón, evaluar la compuerta AND, y probar entradas personalizadas con valores reales (0-1).
Controles Dinámicos: Configuración manual de pesos iniciales, sesgo, y número de iteraciones (1-500) para el entrenamiento.
Visualización del Aprendizaje: Muestra una gráfica del error promedio por iteración, ilustrando la convergencia del perceptrón.
Diseño Orientado a Objetos: Estructura modular con clases como Perceptron, TrainingData, UserInput, WebApp, y ErrorPlot.
Estructura del Proyecto
text

Collapse

Ajuste

Copiar
Perceptron_AND/
├── app.py            # Lógica principal en Python con Flask y Perceptron
├── templates/        # Plantillas HTML para la interfaz
│   └── index.html    # Interfaz web con controles y salida
├── static/           # Archivos estáticos (estilos y gráficos)
│   └── styles.css    # Estilos CSS para la interfaz y gráfica
└── README.md         # Este archivo
Requisitos
Python 3.8+
Flask: pip install flask
Matplotlib: pip install matplotlib
Java (opcional): Para generar el diagrama de clases con PlantUML, si lo usas.
Instalación
Clona o descarga este repositorio en tu máquina:
bash

Collapse

Ajuste

Copiar
git clone <ruta_del_repositorio>  # Si usas Git
# O descarga manualmente los archivos en una carpeta llamada "Perceptron_AND"
Navega al directorio del proyecto:
bash

Collapse

Ajuste

Copiar
cd Perceptron_AND
Instala las dependencias requeridas:
bash

Collapse

Ajuste

Copiar
pip install flask matplotlib
Verifica que Python, Flask y matplotlib estén instalados correctamente:
bash

Collapse

Ajuste

Copiar
python --version
python -c "import flask; print(flask.__version__)"
python -c "import matplotlib; print(matplotlib.__version__)"
Uso
Ejecuta la aplicación desde la terminal en la raíz del proyecto:
bash

Collapse

Ajuste

Copiar
python app.py
Abre un navegador y visita http://127.0.0.1:5000/ para acceder a la interfaz web.
Utiliza la interfaz para:
Ajustar el número de iteraciones con la barra deslizante (1-500).
Ingresar pesos iniciales (W1, W2) y sesgo manualmente.
Hacer clic en "Entrenar Perceptrón" para entrenar el modelo con la compuerta AND.
Usar "Evaluar AND" para verificar las predicciones predefinidas de AND.
Ingresar valores reales (0-1) en los campos "Entrada 1" y "Entrada 2", y usar "Evaluar Personalizado" para probar entradas personalizadas.
Observar la salida en la consola oscura, que incluye pesos iniciales, finales, sesgo, iteraciones, y (si aplica) la gráfica del error.
Funcionalidades Clave
Entrenamiento del Perceptrón: Usa datos predefinidos de la compuerta AND para ajustar pesos y sesgo iterativamente, mostrando su evolución.
Evaluación Automática: Muestra resultados para [0,0], [0,1], [1,0], y [1,1], comparando con los valores esperados.
Entradas Personalizadas: Permite al usuario ingresar valores reales (por ejemplo, 0.5, 0.7) para evaluar con el perceptrón entrenado.
Visualización del Error: Genera una gráfica que muestra cómo el error promedio disminuye con las iteraciones, visualizando el aprendizaje.
Diseño Orientado a Objetos: La lógica está encapsulada en clases como Perceptron, TrainingData, UserInput, WebApp, y ErrorPlot, con relaciones claras.
Diagrama de Clases
El proyecto incluye un diagrama de clases en PlantUML que representa su estructura orientada a objetos. Puedes generar el diagrama con PlantUML (requiere Java) o visualizarlo en línea usando el código proporcionado en la documentación. El diagrama está organizado en tres paquetes: 'Modelo Perceptrón', 'Interfaz Web (Flask)', y 'Visualización', mostrando Perceptron, TrainingData, UserInput, WebApp, y ErrorPlot con sus relaciones y notas explicativas.

Contribuciones
Si deseas contribuir, por favor:

Haz un fork de este repositorio.
Crea una rama para tus cambios (git checkout -b feature/nueva-funcionalidad).
Realiza tus modificaciones y haz commit (git commit -m "Descripción del cambio").
Envía un pull request con una descripción clara de tus cambios.
Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles (si aplica, puedes añadir un archivo LICENSE o especificar aquí).

Contacto
Para preguntas o sugerencias, contacta al autor en [tu correo o red social, si aplica] o abre un issue en este repositorio.

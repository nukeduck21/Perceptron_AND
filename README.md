🚀 Simulador de Perceptrón - Compuerta AND
📄 Descripción
Este proyecto es una aplicación web que simula una neurona artificial utilizando el algoritmo del Perceptrón Simple para modelar la compuerta lógica AND.

Permite:

Entrenar el perceptrón con datos predefinidos.
Evaluar automáticamente entradas estándar.
Probar valores reales personalizados ingresados por el usuario.
Está desarrollado siguiendo el paradigma orientado a objetos, utilizando:

Python con Flask para la interfaz web.
HTML/CSS para la presentación.
Matplotlib para visualizar el aprendizaje mediante una gráfica del error.
✅ Requisitos cumplidos
Simular una neurona artificial mediante el perceptrón simple.
Entrenar el modelo con la base de conocimiento de la compuerta lógica AND.
Evaluar automáticamente con valores reales de entrada.
Seguir el paradigma orientado a objetos.
🎯 Características
Interfaz Web Interactiva: Entrena, evalúa y prueba entradas personalizadas (valores entre 0 y 1).
Controles Dinámicos: Configuración manual de pesos, sesgo y número de iteraciones (1-500).
Visualización del Aprendizaje: Gráfica del error promedio por iteración.
Diseño Modular (POO): Clases como Perceptron, TrainingData, UserInput, WebApp y ErrorPlot.
📁 Estructura del Proyecto
csharp
Copiar
Editar
Perceptron_AND/
├── app.py            # Lógica principal (Python + Flask)
├── templates/
│   └── index.html    # Interfaz web
├── static/
│   └── styles.css    # Estilos CSS
└── README.md         # Este archivo
⚙️ Requisitos
Python 3.8+
Flask:
bash
Copiar
Editar
pip install flask
Matplotlib:
bash
Copiar
Editar
pip install matplotlib
Java (opcional): Para generar el diagrama de clases con PlantUML.
💾 Instalación
Clona o descarga el repositorio:

bash
Copiar
Editar
git clone <ruta_del_repositorio>
# O descarga manualmente los archivos y guárdalos en "Perceptron_AND"
Entra al directorio del proyecto:

bash
Copiar
Editar
cd Perceptron_AND
Instala las dependencias:

bash
Copiar
Editar
pip install flask matplotlib
Verifica las versiones:

bash
Copiar
Editar
python --version
python -c "import flask; print(flask.__version__)"
python -c "import matplotlib; print(matplotlib.__version__)"
🚀 Uso
Ejecuta la aplicación:

bash
Copiar
Editar
python app.py
Abre tu navegador y visita:
http://127.0.0.1:5000/

Desde la interfaz puedes:

Ajustar iteraciones (1-500).
Ingresar pesos iniciales y sesgo.
Entrenar el perceptrón.
Evaluar automáticamente la compuerta AND.
Probar entradas personalizadas (valores entre 0 y 1).
Visualizar resultados y la gráfica del error.
🔑 Funcionalidades Clave
Entrenamiento: Ajuste iterativo de pesos y sesgo con datos de la compuerta AND.
Evaluación Automática: Resultados para [0,0], [0,1], [1,0], [1,1].
Entradas Personalizadas: Evaluación con valores reales como 0.5, 0.7.
Visualización del Error: Gráfica de la evolución del error promedio.
Diseño POO: Estructura con clases específicas para modularidad y mantenimiento.
🧩 Diagrama de Clases
El proyecto incluye un diagrama de clases realizado en PlantUML que ilustra:

![DIAGRAMAperceptrónV2](https://github.com/user-attachments/assets/14d111fd-0b12-4535-8057-368509516529)



🤝 Contribuciones
¡Las contribuciones son bienvenidas!

Haz un fork del repositorio.
Crea una nueva rama:
bash
Copiar
Editar
git checkout -b feature/nueva-funcionalidad
Realiza tus cambios y haz commit:
bash
Copiar
Editar
git commit -m "Descripción del cambio"
Envía un pull request con la explicación detallada.
📜 Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

📬 Contacto
¿Preguntas o sugerencias?
Puedes contactar al autor en [tu correo o red social] o abrir un issue en este repositorio.

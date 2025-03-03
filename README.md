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

La estructura orientada a objetos.
Las relaciones entre clases.
Notas explicativas de cada componente.
Puedes generarlo con PlantUML (requiere Java) o visualizarlo online.

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

¿Quieres que te lo deje como archivo .md para que solo copies y pegues? 👀

Dijiste:
se ve algo desordenado, dame un formato que se vea bien 
ChatGPT dijo:
¡Entiendo totalmente! Aquí te dejo el README.md con un formato claro, limpio y ordenado, perfecto para GitHub. Me aseguré de que cada sección esté bien separada, los títulos sean coherentes y la vista sea agradable:

🔷 Simulador de Perceptrón - Compuerta AND
📌 Descripción
Este proyecto es una aplicación web que simula una neurona artificial mediante el Perceptrón Simple para modelar la compuerta lógica AND.

Tecnologías utilizadas:
Python con Flask para la lógica e interfaz web.
HTML/CSS para la presentación.
Matplotlib para graficar el error durante el aprendizaje.
Paradigma orientado a objetos (POO) para organizar la estructura del código.
🎯 Funcionalidades principales
✅ Entrenamiento del perceptrón con la tabla de verdad de la compuerta AND.
✅ Evaluación automática con entradas predefinidas.
✅ Pruebas con valores personalizados entre 0 y 1.
✅ Visualización gráfica del error promedio por iteración.
✅ Configuración manual de pesos, sesgo y número de iteraciones.

🏗️ Estructura del proyecto
csharp
Copiar
Editar
Perceptron_AND/
├── app.py            # Lógica principal (Python + Flask)
├── templates/
│   └── index.html    # Interfaz web
├── static/
│   └── styles.css    # Estilos de la aplicación
└── README.md         # Documentación del proyecto
⚙️ Requisitos
Python 3.8+
Flask
bash
Copiar
Editar
pip install flask
Matplotlib
bash
Copiar
Editar
pip install matplotlib
Java (opcional, para generar el diagrama de clases con PlantUML)
🚀 Instalación
1️⃣ Clona el repositorio:

bash
Copiar
Editar
git clone <ruta_del_repositorio>
O descarga los archivos manualmente y colócalos en una carpeta llamada Perceptron_AND.

2️⃣ Accede al directorio del proyecto:

bash
Copiar
Editar
cd Perceptron_AND
3️⃣ Instala las dependencias necesarias:

bash
Copiar
Editar
pip install flask matplotlib
4️⃣ Verifica las instalaciones:

bash
Copiar
Editar
python --version
python -c "import flask; print(flask.__version__)"
python -c "import matplotlib; print(matplotlib.__version__)"
🖥️ Uso
Ejecuta la aplicación desde la terminal:

bash
Copiar
Editar
python app.py
Luego, abre tu navegador y visita:
http://127.0.0.1:5000/

Desde la interfaz podrás:
Ajustar el número de iteraciones (1-500).
Configurar pesos iniciales y sesgo.
Entrenar el perceptrón con la compuerta AND.
Evaluar resultados automáticos ([0,0], [0,1], [1,0], [1,1]).
Probar entradas personalizadas (valores entre 0 y 1).
Visualizar la evolución del error en una gráfica.
📊 Visualización del aprendizaje
La aplicación genera una gráfica que muestra cómo disminuye el error promedio con cada iteración, permitiendo observar la convergencia del perceptrón durante el entrenamiento.

📐 Diagrama de clases
El proyecto incluye un diagrama de clases diseñado con PlantUML que describe su estructura orientada a objetos, mostrando las siguientes clases principales:



![DIAGRAMAperceptrónV2](https://github.com/user-attachments/assets/e1e8135a-e18f-4946-92b9-3ae4d78aab23)




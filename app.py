from flask import Flask, render_template, request, send_from_directory
import random
import matplotlib

matplotlib.use('Agg')  # Usar backend no interactivo (sin GUI)
import matplotlib.pyplot as plt
import os
import numpy as np

app = Flask(__name__)


# Clase Perceptron
class Perceptron:
    def __init__(self, learning_rate=0.1, initial_weights=None, initial_bias=None):
        if initial_weights is None:
            self.weights = [random.random(), random.random()]  # Pesos iniciales aleatorios por defecto
        else:
            self.weights = initial_weights  # Pesos iniciales manuales
        if initial_bias is None:
            self.bias = random.random()  # Sesgo inicial aleatorio por defecto
        else:
            self.bias = initial_bias  # Sesgo inicial manual
        self.learning_rate = learning_rate

    def activate(self, output_sum):
        return 1 if output_sum > 0 else 0

    def guess(self, inputs):
        output_sum = sum(w * i for w, i in zip(self.weights, inputs)) + self.bias
        return self.activate(output_sum)

    def train(self, inputs, target):
        guess = self.guess(inputs)
        error = target - guess
        for i in range(len(self.weights)):
            self.weights[i] += error * inputs[i] * self.learning_rate
        self.bias += error * self.learning_rate
        return error  # Devolver el error para graficar


# Base de conocimiento: Compuerta AND
training_data = [
    {"inputs": [0, 0], "target": 0},
    {"inputs": [0, 1], "target": 0},
    {"inputs": [1, 0], "target": 0},
    {"inputs": [1, 1], "target": 1}
]

# Instancia global del perceptrón (inicialmente con valores aleatorios)
perceptron = Perceptron()

# Carpeta para guardar las gráficas
STATIC_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
if not os.path.exists(STATIC_FOLDER):
    os.makedirs(STATIC_FOLDER)


# Ruta principal
@app.route("/", methods=["GET", "POST"])
def index():
    global perceptron  # Declarar perceptron como global al inicio de la función
    output = ""
    custom_input1 = ""
    custom_input2 = ""
    iterations = 100  # Valor por defecto (dentro del rango 1-500)
    initial_w1 = request.form.get("w1", "")  # Obtener valores iniciales del formulario o vacíos
    initial_w2 = request.form.get("w2", "")
    initial_bias = request.form.get("bias", "")

    graph_path = None  # Variable para rastrear si se generó la gráfica

    if request.method == "POST":
        action = request.form.get("action", "")
        if action == "train":
            # Obtener los valores iniciales de pesos y sesgo del formulario, si existen
            try:
                w1 = float(request.form.get("w1", 0.0)) if request.form.get("w1") else random.random()
                w2 = float(request.form.get("w2", 0.0)) if request.form.get("w2") else random.random()
                bias = float(request.form.get("bias", 0.0)) if request.form.get("bias") else random.random()
                # Crear o actualizar la instancia global del perceptrón con los valores manuales o aleatorios
                perceptron = Perceptron(initial_weights=[w1, w2], initial_bias=bias)

                initial_weights = perceptron.weights.copy()  # Guardar pesos iniciales
                initial_bias = perceptron.bias  # Guardar sesgo inicial
                iterations = int(
                    request.form.get("iterations", 100))  # Obtener número de iteraciones del formulario (1-500)

                # Calcular error por iteración para graficar (solo si hay más de 1 iteración)
                errors = []
                if iterations > 1:
                    for i in range(iterations):
                        total_error = 0
                        for data in training_data:
                            error = perceptron.train(data["inputs"], data["target"])
                            total_error += abs(error)
                        errors.append(total_error / len(training_data))  # Promedio del error por iteración

                    # Generar gráfica del error solo si hay datos suficientes
                    if errors:
                        plt.figure(figsize=(10, 6))
                        plt.plot(range(1, iterations + 1), errors, color='blue', label='Error promedio por iteración')
                        plt.title('Evolución del Error durante el Entrenamiento')
                        plt.xlabel('Iteración')
                        plt.ylabel('Error promedio')
                        plt.legend()
                        plt.grid(True)
                        graph_path = os.path.join(STATIC_FOLDER, 'error_plot.png')
                        plt.savefig(graph_path)
                        plt.close()
                    else:
                        graph_path = None

                output = (
                    "Entrenamiento completado.\n"
                    f"Pesos iniciales: W1 = {initial_weights[0]:.2f}, W2 = {initial_weights[1]:.2f}\n"
                    f"Sesgo inicial: {initial_bias:.2f}\n"
                    f"Pesos finales: W1 = {perceptron.weights[0]:.2f}, W2 = {perceptron.weights[1]:.2f}\n"
                    f"Sesgo final: {perceptron.bias:.2f}\n"
                    f"Iteraciones usadas: {iterations}"
                )
            except ValueError:
                output = "Error: Por favor, ingresa valores numéricos válidos para pesos, sesgo e iteraciones."
        elif action == "test_and":
            if not perceptron.weights:  # Si perceptron no está inicializado, crear uno por defecto
                perceptron = Perceptron()
            output = "Evaluando compuerta AND:\n"
            for data in training_data:
                result = perceptron.guess(data["inputs"])
                output += f"Entrada: {data['inputs']} -> Salida: {result} (Esperado: {data['target']})\n"
        elif action == "test_custom":
            if not perceptron.weights:  # Si perceptron no está inicializado, crear uno por defecto
                perceptron = Perceptron()
            try:
                custom_input1 = float(request.form.get("input1", 0))
                custom_input2 = float(request.form.get("input2", 0))
                custom_inputs = [custom_input1, custom_input2]
                result = perceptron.guess(custom_inputs)
                output = f"Evaluando entrada personalizada: [{custom_input1}, {custom_input2}] -> Salida: {result}\n"
            except ValueError:
                output = "Error: Por favor, ingresa valores numéricos válidos (0 o 1 recomendados)."

    return render_template("index.html", output=output, custom_input1=custom_input1, custom_input2=custom_input2,
                           iterations=iterations, initial_w1=initial_w1, initial_w2=initial_w2,
                           initial_bias=initial_bias,
                           graph_path=graph_path)


# Ruta para servir la gráfica estática
@app.route('/static/error_plot.png')
def serve_plot():
    if os.path.exists(os.path.join(STATIC_FOLDER, 'error_plot.png')):
        return send_from_directory(STATIC_FOLDER, 'error_plot.png')
    return "", 404  # Retornar 404 si la gráfica no existe


if __name__ == "__main__":
    app.run(debug=True)
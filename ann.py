import numpy as np

class NeuralNetwork:
    def __init__(self, n_inputs, n_outputs, n_hidden_layers, n_neurons_per_layer):
        self.n_inputs = n_inputs
        self.n_outputs = n_outputs
        self.n_hidden_layers = n_hidden_layers
        self.n_neurons_per_layer = n_neurons_per_layer
        
        # Inicjalizacja wag i biasów
        self.weights = []
        self.biases = []
        
        # Inicjalizacja wag dla warstw ukrytych
        for i in range(n_hidden_layers):
            if i == 0:
                self.weights.append(np.random.randn(n_inputs, n_neurons_per_layer))
            else:
                self.weights.append(np.random.randn(n_neurons_per_layer, n_neurons_per_layer))
            self.biases.append(np.zeros((1, n_neurons_per_layer)))
        
        # Inicjalizacja wag dla warstwy wyjściowej
        self.weights.append(np.random.randn(n_neurons_per_layer, n_outputs))
        self.biases.append(np.zeros((1, n_outputs)))
    
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def forward(self, x):
        for w, b in zip(self.weights, self.biases):
            x = self.sigmoid(np.dot(x, w) + b)
        return x

# Przykład użycia
n_inputs = 3
n_outputs = 2
n_hidden_layers = 2
n_neurons_per_layer = 4

# Inicjalizacja sieci neuronowej
network = NeuralNetwork(n_inputs, n_outputs, n_hidden_layers, n_neurons_per_layer)

# Przykładowe dane wejściowe
input_data = np.random.rand(1, n_inputs)

# Propagacja w przód
output = network.forward(input_data)

print("Dane wejściowe:")
print(input_data)
print("Wyjście sieci:")
print(output)

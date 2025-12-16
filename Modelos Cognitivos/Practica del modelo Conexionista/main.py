import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

#cargar el data set digits
digits = load_digits()
X = digits.data
y = digits.target

#ver imagenes dataset
plt.figure(figsize=(8, 4))

for i in range(8):
    plt.subplot(2, 4, i + 1)
    plt.imshow(digits.images[i], cmap='gray')
    plt.title(f"digito: {digits.target[i]}")
    plt.axis('off')
    
plt.tight_layout()
plt.show()

#dividir datos 
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#crear modelo mlp
mlp = MLPClassifier(
    hidden_layer_sizes=(100,),
    activation='relu',
    solver='adam',
    max_iter=300,
    random_state=42
)

# entrenar modelo
mlp.fit(X_train, y_train)

#predicciones
y_pred = mlp.predict(X_test)

#calcular precison
accuracy = accuracy_score(y_test, y_pred)
print("\nPresicion del modelo: ")
print(f"{accuracy:.4f}")

#mostrar matriz de confucion
cm = confusion_matrix(y_test, y_pred)

print("\nMatriz de confusion")
print("filas  = valores reales | columnas = valores predichos\n")
print(cm)
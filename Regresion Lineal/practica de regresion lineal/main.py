import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from mpl_toolkits.mplot3d import Axes3D

plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')

#cargamos csv
data = pd.read_csv("articulos_ml.csv")

print("Dimensiones del dataset:", data.shape)
print(data.head())
print(data.describe())

#cambiamos valores vacios por 0
data['# of comments'] = data['# of comments'].fillna(0)
data['# of Links'] = data['# of Links'].fillna(0)
data['# Images video'] = data['# Images video'].fillna(0)

filtered_data = data[
    (data['Word count'] <= 3500) &
    (data['# Shares'] <= 80000)
]

f1 = filtered_data['Word count'].values
f2 = filtered_data['# Shares'].values

colores = []
for _, row in filtered_data.iterrows():
    if row['Word count'] > 1808:   
        colores.append('orange')
    else:
        colores.append('blue')

plt.scatter(f1, f2, c=colores, s=30)
plt.xlabel("Cantidad de Palabras")
plt.ylabel("Cantidad de Shares")
plt.title("Word count vs Shares")
plt.show()

#regresion lineal sim
dataX = filtered_data[['Word count']]
X_train = np.array(dataX)
y_train = filtered_data['# Shares'].values

regr = linear_model.LinearRegression()
regr.fit(X_train, y_train)

y_pred = regr.predict(X_train)

print("\n--- REGRESION LINEAL SIMPLE ---")
print("Pendiente (m):", regr.coef_)
print("Intercepto (b):", regr.intercept_)
print("MSE:", mean_squared_error(y_train, y_pred))
print("R2:", r2_score(y_train, y_pred))

#prediccion
y_2000 = regr.predict([[2000]])
print("Shares estimados para 2000 palabras:", int(y_2000))

#regresion lineal multivariable
suma = (
    filtered_data['# of Links'] +
    filtered_data['# of comments'] +
    filtered_data['# Images video']
)

dataX2 = pd.DataFrame()
dataX2['Word count'] = filtered_data['Word count']
dataX2['suma'] = suma

XY_train = np.array(dataX2)
z_train = filtered_data['# Shares'].values

regr2 = linear_model.LinearRegression()
regr2.fit(XY_train, z_train)

z_pred = regr2.predict(XY_train)

print("\n--- REGRESION LINEAL MULTIVARIABLE ---")
print("Coeficientes:", regr2.coef_)
print("Intercepto:", regr2.intercept_)
print("MSE:", mean_squared_error(z_train, z_pred))
print("R2:", r2_score(z_train, z_pred))

#greafica 3d
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

xx, yy = np.meshgrid(
    np.linspace(0, 3500, 10),
    np.linspace(0, 60, 10)
)

z = (regr2.coef_[0] * xx) + (regr2.coef_[1] * yy) + regr2.intercept_

ax.plot_surface(xx, yy, z, alpha=0.3, cmap='hot')
ax.scatter(XY_train[:, 0], XY_train[:, 1], z_train, c='blue', s=30)
ax.scatter(XY_train[:, 0], XY_train[:, 1], z_pred, c='red', s=40)

ax.set_xlabel('Cantidad de Palabras')
ax.set_ylabel('Links + Comentarios + Imagenes')
ax.set_zlabel('Shares')
ax.set_title('Regresion Lineal Multivariable')

ax.view_init(elev=30, azim=65)
plt.show()

#pred final
z_2000 = regr2.predict([[2000, 10 + 4 + 6]])
print("Shares estimados (multivariable):", int(z_2000))

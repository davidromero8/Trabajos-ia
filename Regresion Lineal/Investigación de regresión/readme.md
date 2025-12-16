# Regresión Lineal y No Lineal

## ¿Qué es la regresión lineal?

La regresión lineal es una técnica de análisis de datos que predice el valor de datos desconocidos mediante el uso de otro valor de datos relacionado y conocido. Modela matemáticamente la variable desconocida o dependiente y la variable conocida o independiente como una ecuación lineal.

Por ejemplo, supongamos que tiene datos sobre sus gastos e ingresos del año pasado. Las técnicas de regresión lineal analizan estos datos y determinan que tus gastos son la mitad de tus ingresos. Luego calculan un gasto futuro desconocido al reducir a la mitad un ingreso conocido futuro.

---

## ¿Cómo funciona la regresión lineal?

En esencia, una técnica de regresión lineal simple intenta trazar un gráfico lineal entre dos variables de datos, **x** e **y**.

Como variable independiente, **x** se traza a lo largo del eje horizontal. Las variables independientes también se denominan variables explicativas o variables predictivas.

La variable dependiente, **y**, se traza en el eje vertical. También puede hacer referencia a los valores **y** como variables de respuesta o variables pronosticadas.

---

## ¿Cuáles son los tipos de regresión lineal?

Algunos tipos de análisis de regresión son más adecuados que otros para gestionar conjuntos de datos complejos. A continuación se muestran algunos ejemplos.

---

### Regresión lineal simple

La regresión lineal simple se define mediante la función lineal:

Y = β0*X + β1 + ε


β0 y β1 son dos constantes desconocidas que representan la pendiente de regresión, mientras que ε (épsilon) es el término de error.

Puede utilizar la regresión lineal simple para modelar la relación entre dos variables, como las siguientes:

- Lluvia y rendimiento de los cultivos  
- Edad y estatura en niños  
- Temperatura y expansión del mercurio metálico en un termómetro  

---

### Regresión lineal múltiple

En el análisis de regresión lineal múltiple, el conjunto de datos contiene una variable dependiente y múltiples variables independientes. La función de línea de regresión lineal cambia para incluir más factores, de la siguiente manera:

Y = β0*x0 + β1x1 + β2x2 + …… βNxN + ε


A medida que aumenta el número de variables predictivas, las constantes β también aumentan en consecuencia.

La regresión lineal múltiple modela múltiples variables y su impacto en un resultado:

- Lluvia, temperatura y uso de fertilizantes en el rendimiento de los cultivos  
- Dieta y ejercicio sobre enfermedades cardíacas  
- Crecimiento salarial e inflación en las tasas de préstamos hipotecarios  

---

### Regresión logística

Los científicos de datos utilizan la regresión logística para medir la probabilidad de que se produzca un evento. La predicción es un valor entre 0 y 1, donde 0 indica un evento que es poco probable que ocurra y 1 indica una probabilidad máxima de que suceda.

Las ecuaciones logísticas usan funciones logarítmicas para calcular la línea de regresión.

A continuación, se indican varios ejemplos:

- La probabilidad de ganar o perder en un partido deportivo  
- La probabilidad de aprobar o reprobar una prueba  
- La probabilidad de que una imagen sea una fruta o un animal  

---

## ¿Qué es la regresión no lineal?

La regresión no lineal es un método para encontrar un modelo no lineal para la relación entre la variable dependiente y un conjunto de variables independientes.

A diferencia de la regresión lineal tradicional, que está restringida a la estimación de modelos lineales, la regresión no lineal puede estimar modelos con relaciones arbitrarias entre las variables independientes y las dependientes. Esto se lleva a cabo usando algoritmos de estimación iterativos.

Tenga en cuenta que este procedimiento no es necesario para modelos polinomiales simples de la forma:

Y = A + BX**2


Al definir:
W = X**2


Obtenemos un modelo lineal simple:
Y = A + BW


que se puede estimar utilizando métodos tradicionales como el procedimiento de regresión lineal.

---

## Ejemplo de regresión no lineal

¿Puede pronosticarse la población basándose en el tiempo?

Un diagrama de dispersión muestra que parece haber una estrecha relación entre la población y el tiempo, pero la relación es no lineal y por eso exige la utilización de los métodos de estimación especiales del procedimiento de regresión no lineal.

Creando una ecuación adecuada, como la del modelo logístico de crecimiento poblacional, podemos obtener una buena estimación del modelo, lo que nos permitirá hacer predicciones sobre la población para épocas que no se han sido medidas.

---

## ¿Cómo funciona la regresión no lineal?

La regresión no lineal funciona ajustando una ecuación (una curva) a datos que no siguen una línea recta, buscando la curva que minimice la suma de los errores al cuadrado entre la curva y los puntos de datos.

A menudo se usan algoritmos iterativos como **Gauss-Newton** para encontrar los parámetros óptimos, ya que no hay una fórmula directa como en la regresión lineal.

Se usa cuando la relación es exponencial, logarítmica o de otro tipo curvo, usando funciones como:

y = α · e^(βx)


o modelos de potencia, para modelar patrones complejos y predecir nuevas observaciones.

---

## Diferencia entre modelos de regresión lineal y no lineal

La diferencia entre los modelos de regresión lineal y no lineal no es tan sencilla como parece. Se podría pensar que las ecuaciones lineales producen líneas rectas y las ecuaciones no lineales modelan la curvatura. Desafortunadamente, esto no es cierto.

Ambos tipos de modelos pueden ajustar curvas a los datos, por lo que esa no es la característica definitoria.

La diferencia entre no lineal y lineal es el "no". Bueno, suena a broma, pero sinceramente es la forma más fácil de entender la diferencia. Primero se define qué es la regresión lineal, y luego todo lo demás debe ser regresión no lineal.

---

## Bibliografías

- https://aws.amazon.com/es/what-is/linear-regression/  
- https://www.ibm.com/docs/es/spss-statistics/31.0.0?topic=regression-nonlinear  
- https://statisticsbyjim.com/regression/difference-between-linear-nonlinear-regression-models/


import numpy as np
import matplotlib.pyplot as plt

#Defining the start and end of a straight line
x_start, y_start = 0, 0
x_end, y_end = 10, 10

n_points = 100 #Defining the number of points on the path

#Generating x values for the straight line assuming it is linear
x_values = np.linspace(x_start, x_end, n_points)

#Generating ideal straight line without any deviation
y_values = np.linspace(y_start, y_end, n_points)

#Adding perturbations representing quantum fluctuations
random_deviations = np.random.normal(0, 0.2, size=n_points) #The standard deviation is 0.2 for uncertainties
y_values_actual = y_values + random_deviations

print(f"Mean deviation from the straight line representing unceratinty is: {np.mean(random_deviations): .3f}")

plt.figure(figsize=(8,6))
plt.plot(x_values, y_values, label="Ideal Straight Line (Euclidean)", color="blue", linestyle="--")
plt.plot(y_values, y_values_actual, label="Actual path (Quantum Uncertainty)", color="red", marker="o", markersize=3)
plt.title("Stimulation of Uncertainty on a Straight Line")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.show()
#basic Monte Carlo simulation to estimate the value of π (pi). This is a common example to demonstrate the Monte Carlo method.
#Monte Carlo Simulation to Estimate π
#Concept:
#
#    Imagine a square with a circle inscribed in it.
#    The area of the square is 1×1=11×1=1, and the area of the inscribed circle (with radius 0.5) is π×(0.5)2=π4π×(0.5)2=4π​.
#    If we randomly generate points inside the square, the ratio of the number of points inside the circle to the total number of points should be approximately equal to the ratio of the area of the circle to the area of the square.
#    Thus, Points inside circleTotal pointsTotal pointsPoints inside circle​ should be approximately π44π​.
#    We can estimate π by multiplying this ratio by 4.

import random

# Initialize variables
inside_circle = 0
total_points = 0

# Number of points to simulate
num_simulations = int(input("Enter the number of stimulations: "))

# Run the simulation
while total_points < num_simulations:
    # Generate random point (x, y) between 0 and 1
    x = random.random()
    y = random.random()

    # Check if the point is inside the circle
    if x**2 + y**2 <= 1:
        inside_circle += 1

    # Increment the total number of points
    total_points += 1

# Estimate pi
pi_estimate = (inside_circle / total_points) * 4

# Calculate the percentage error (optional)
actual_pi = 3.141592653589793
percentage_error = abs((pi_estimate - actual_pi) / actual_pi) * 100

# Print the results
print(f"Estimated value of pi: {pi_estimate}")
print(f"Percentage error: {percentage_error:.4f}%")

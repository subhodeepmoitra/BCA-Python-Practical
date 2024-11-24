import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81  # Gravity (m/s^2)
num_simulations = 1000  # Number of simulations to run

# Function to simulate missile trajectory
def simulate_missile_path():
    # Randomly sample initial velocity and launch angle
    v0 = np.random.uniform(100, 200)  # Initial velocity in m/s (between 100 and 200)
    theta = np.random.uniform(30, 60)  # Launch angle in degrees (between 30° and 60°)

    # Convert angle to radians
    theta_rad = np.radians(theta)

    # Calculate time of flight and maximum height
    time_of_flight = 2 * v0 * np.sin(theta_rad) / g
    max_height = (v0**2 * np.sin(theta_rad)**2) / (2 * g)

    # Create time points for the trajectory
    t = np.linspace(0, time_of_flight, num=500)

    # Equations of motion
    x = v0 * np.cos(theta_rad) * t
    y = v0 * np.sin(theta_rad) * t - 0.5 * g * t**2

    return x, y

# Running simulations and plotting the results
for _ in range(num_simulations):
    x, y = simulate_missile_path()
    plt.plot(x, y, color='blue', alpha=0.05)  # Plot each trajectory with transparency

# Final plot settings
plt.title("Monte Carlo Simulation of Missile Trajectories")
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Distance (m)")
plt.grid(True)
plt.show()

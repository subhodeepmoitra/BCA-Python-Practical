import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81  # Gravity (m/s^2)
num_simulations = 1000  # Number of simulations
target_width = 300  # Width of the target on the ground in meters

# Function to simulate missile trajectory and check if it hits the target
def simulate_missile_path_and_check_target():
    # Randomly sample initial velocity and launch angle
    v0 = np.random.uniform(50, 100)  # Initial velocity in m/s (change between 50 and 100) at 24-11-2024 19:04 hrs
    theta = np.random.uniform(10, 20)  # Launch angle in degrees (change to 30° and 60°) at 24-11-2024 19:04 hrs

    # Convert angle to radians
    theta_rad = np.radians(theta)

    # Calculate time of flight
    time_of_flight = 2 * v0 * np.sin(theta_rad) / g

    # Create time points for the trajectory
    t = np.linspace(0, time_of_flight, num=500)

    # Equations of motion
    x = v0 * np.cos(theta_rad) * t
    y = v0 * np.sin(theta_rad) * t - 0.5 * g * t**2

    # Final position (landing point)
    landing_x = x[-1]
    landing_y = y[-1]

    # Check if the missile hits the target (within target bounds)
    hit_target = 0 <= landing_x <= target_width and landing_y <= 0

    return hit_target, x, y

# Track number of hits
num_hits = 0

# Running simulations
for _ in range(num_simulations):
    hit_target, x, y = simulate_missile_path_and_check_target()
    if hit_target:
        num_hits += 1
    plt.plot(x, y, color='blue', alpha=0.05)  # Plot each trajectory with transparency

# Final plot settings
plt.title("Monte Carlo Simulation of Missile Trajectories with Targeting")
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Distance (m)")
plt.xlim(0, target_width + 20)  # Add some margin to see beyond the target
plt.ylim(0, 20)  # Limit the y-axis to make the target visible at ground level
plt.axhline(0, color='red', linestyle='--', label="Target Surface Level")
plt.axvline(target_width, color='red', linestyle='--', label="Target Width")
plt.grid(True)

# Show the plot
plt.legend()
plt.show()

# Calculate and print the probability of hitting the target
probability_of_hit = num_hits / num_simulations
print(f"Probability of hitting the target: {probability_of_hit * 100:.2f}%")

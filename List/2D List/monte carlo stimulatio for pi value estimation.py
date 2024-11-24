import random

def estimate_pi(num_points):
    inside_circle = 0

    for _ in range(num_points):
        x, y = random.random(), random.random()  # Random point in the unit square
        if x**2 + y**2 <= 1:  # Check if inside quarter circle
            inside_circle += 1

    return (inside_circle / num_points) * 4

# Estimate Pi with 1 million points
print(f"Estimated Pi: {estimate_pi(1_000_000)}")

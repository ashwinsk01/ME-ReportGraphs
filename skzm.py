import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Define time (years from 2015 to 2025)
t = np.linspace(2015, 2025, 100)

# Parameters for Skype's decline and Zoom's growth
S0 = 0.60  # Initial market share of Skype (60%)
a = 0.3    # Decline rate for Skype

K = 0.60   # Carrying capacity for Zoom (maximum market share it can capture)
r = 0.5    # Growth rate of Zoom
t0 = 2019  # Inflection point for Zoom (when growth accelerates)

# Skype's market share over time (exponential decay)
def skype_share(t):
    return S0 * np.exp(-a * (t - 2015))

# Zoom's market share over time (logistic growth)
def zoom_share(t):
    return K / (1 + np.exp(-r * (t - t0)))

# Function to find intersection: Skype's share = Zoom's share
def intersection_function(t):
    return skype_share(t) - zoom_share(t)

# Solve for the intersection point
t_intersection = fsolve(intersection_function, 2019)[0]
skype_at_intersection = skype_share(t_intersection)
zoom_at_intersection = zoom_share(t_intersection)

# Plotting the market shares
plt.figure(figsize=(10, 6))
plt.plot(t, skype_share(t), label="Skype", color='blue', linestyle='--')
plt.plot(t, zoom_share(t), label="Zoom", color='red')

# Mark the intersection point
plt.scatter(t_intersection, skype_at_intersection, color='green', zorder=5, label=f'Intersection: {t_intersection:.2f}')
plt.axvline(t_intersection, color='green', linestyle=':', label=f"Year: {t_intersection:.2f}")

# Labeling the graph
plt.title("Market Share Dynamics: Skype vs. Zoom (2015-2025)")
plt.xlabel("Year")
plt.ylabel("Market Share")
plt.legend()

# Show plot
plt.grid(True)
plt.show()

# Print intersection point
print(f"Intersection point occurs in year: {t_intersection:.2f}")
print(f"At this point, Skype's share = Zoom's share = {skype_at_intersection:.2f}")

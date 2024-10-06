import numpy as np
import matplotlib.pyplot as plt

# Define price ranges (Y-axis)
price = np.linspace(50, 7, 11)  # From $50 to $7, representing price of premium services

# Define quantity ranges (X-axis)
# Freemium model (elastic demand)
quantity_freemium = np.array([100, 120, 150, 200, 250, 320, 400, 450, 500, 600, 700])

# Paid model (inelastic demand, Skype's traditional model)
quantity_paid = np.array([100, 110, 120, 130, 135, 140, 145, 147, 148, 149, 150])

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the freemium (elastic) demand curve
ax.plot(quantity_freemium, price, color='blue', marker='o', linestyle='-', label="Freemium Model (Elastic)")

# Plot the paid (inelastic) demand curve
ax.plot(quantity_paid, price, color='red', marker='o', linestyle='--', label="Paid Model (Inelastic, Skype)")

# Add titles and labels
ax.set_title("Elasticity of Demand: Freemium vs Paid Model", fontsize=16)
ax.set_xlabel("Quantity of Paid Users (in thousands)", fontsize=12)
ax.set_ylabel("Price of Premium Service (USD)", fontsize=12)

# Add a legend to differentiate between the two models
ax.legend()

# Highlight key text
ax.text(500, 20, 'Freemium: High Elasticity', fontsize=12, verticalalignment='center', horizontalalignment='center', color='blue')
ax.text(130, 40, 'Paid: Low Elasticity', fontsize=12, verticalalignment='center', horizontalalignment='center', color='red')

# Display the grid
ax.grid(True)

# Show the plot
plt.show()

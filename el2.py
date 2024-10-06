import numpy as np
import matplotlib.pyplot as plt

# Define price/investment per user (Y-axis) and quantity of users acquired (X-axis)
investment = np.linspace(10, 100, 100)  # Investment per user (price)
quantity_users_freemium = 1000 / investment  # Freemium model (elastic demand)
quantity_users_paid = 500 / investment ** 0.5  # Paid model (inelastic demand)

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the demand curve for the freemium model (elastic)
ax.plot(quantity_users_freemium, investment, color='blue', linewidth=2, label="Demand (Freemium Model)")

# Plot the demand curve for the paid model (inelastic)
ax.plot(quantity_users_paid, investment, color='red', linestyle='--', linewidth=2, label="Demand (Paid Model)")

# Plot the supply curve (constant supply as a horizontal line)
constant_supply = np.full_like(investment, 50)  # Assume a constant supply where price is constant at 50
ax.plot(quantity_users_freemium, constant_supply, color='black', linestyle='-', linewidth=2, label="Supply")

# Add titles and labels (without specific units)
ax.set_title("Demand and Supply: Freemium vs Paid Models", fontsize=16)
ax.set_xlabel("Quantity of Users Acquired", fontsize=12)
ax.set_ylabel("Investment per User", fontsize=12)

# Adding lines and arrows to represent curves
ax.axvline(x=600, color='grey', linestyle=':', linewidth=1)  # Freemium quantity marker
ax.axvline(x=150, color='grey', linestyle=':', linewidth=1)  # Paid quantity marker
ax.axhline(y=50, color='grey', linestyle=':', linewidth=1)  # Constant supply marker

# Add a legend to differentiate between demand and supply
ax.legend()

# Highlighting the general concepts of elastic vs inelastic demand
ax.text(750, 20, 'Elastic Demand', fontsize=12, color='blue', verticalalignment='center', horizontalalignment='center')
ax.text(150, 70, 'Inelastic Demand', fontsize=12, color='red', verticalalignment='center', horizontalalignment='center')
ax.text(600, 50, 'Constant Supply', fontsize=12, color='black', verticalalignment='center', horizontalalignment='center')

# Show grid for clarity
ax.grid(True, linestyle='--', alpha=0.6)

# Show the plot
plt.show()

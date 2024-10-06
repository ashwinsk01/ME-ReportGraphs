import numpy as np
import matplotlib.pyplot as plt

# Create quantities
Q = np.linspace(0, 100, 200)

# Demand Curves
D1_skype = 100 - Q  # Initial demand curve for Skype (more inelastic)
D0_skype = 80 - Q   # Decreased demand for Skype after losing market share

D_zoom = 110 - 0.5 * Q  # Elastic demand for Zoom (flatter curve, higher elasticity)
D_teams = 100 - 0.6 * Q  # Elastic demand for Teams (similar, slightly less elastic than Zoom)

# Supply Curve
P_supply_initial = 20  # Initial supply (paid model, higher marginal cost)
P_supply_freemium = 10  # New lower supply after Skype introduces freemium model

# Plotting
plt.figure(figsize=(10, 7))

# Skype Demand Curves
plt.plot(Q, D1_skype, label='Skype Initial Demand (D1)', color='orange')
plt.plot(Q, D0_skype, label='Skype Decreased Demand (D0)', linestyle='--', color='red')

# Competitors' Demand Curves
plt.plot(Q, D_zoom, label='Zoom Demand (High Elasticity)', color='blue')
plt.plot(Q, D_teams, label='Teams Demand (High Elasticity)', color='green')

# Supply Curves
plt.axhline(y=P_supply_initial, color='black', label='Initial Supply (S1)', linestyle='-')
plt.axhline(y=P_supply_freemium, color='gray', label='Freemium Supply (S2)', linestyle='--')

# Equilibrium points
# Skype before demand shift (Initial)
eq_Q1_skype = 100 - P_supply_initial
eq_P1_skype = P_supply_initial
plt.plot(eq_Q1_skype, eq_P1_skype, 'ko')
plt.text(eq_Q1_skype + 2, eq_P1_skype + 2, 'E1 (Skype)', color='orange')

# Skype after demand decrease
eq_Q0_skype = 80 - P_supply_freemium
eq_P0_skype = P_supply_freemium
plt.plot(eq_Q0_skype, eq_P0_skype, 'ko')
plt.text(eq_Q0_skype + 2, eq_P0_skype + 2, 'E2 (Skype)', color='red')

# Equilibrium for Zoom and Teams (new demand shift)
eq_Q_zoom = (110 - P_supply_freemium) / 0.5
eq_Q_teams = (100 - P_supply_freemium) / 0.6

plt.plot(eq_Q_zoom, P_supply_freemium, 'ko')
plt.text(eq_Q_zoom + 2, P_supply_freemium + 2, 'E3 (Zoom)', color='blue')

plt.plot(eq_Q_teams, P_supply_freemium, 'ko')
plt.text(eq_Q_teams + 2, P_supply_freemium + 2, 'E4 (Teams)', color='green')

# remove x and y axis units
plt.xticks([])
plt.yticks([])

# Annotations
plt.title('Demand Elasticity for Skype vs. Competitors', fontsize=14)
plt.xlabel('Quantity of Users (Q)')
plt.ylabel('Perceived Value(P)')
plt.legend()
plt.grid(True)

# Display the plot
plt.show()

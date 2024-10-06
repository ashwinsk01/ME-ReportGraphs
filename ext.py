import matplotlib.pyplot as plt
import numpy as np

# Quantities for Skype and Teams
Q = np.linspace(0, 100, 200)

# Demand for Skype (D_skype) decreases as Teams becomes more popular
D_skype_initial = 100 - Q  # Initial demand for Skype
D_skype_after = 60 - Q     # Reduced demand for Skype due to Teams

# Demand for Teams (D_teams) increases as Skype users migrate to Teams
D_teams_initial = 50 - Q   # Initial demand for Teams before cannibalization
D_teams_after = 90 - Q     # Increased demand for Teams after Skype cannibalization

# Supply for both remains constant, assuming capacity doesn't change much
S_skype = 20  # Skype supply remains at a lower constant level
S_teams = 40  # Teams supply remains at a higher constant level

# Plotting
plt.figure(figsize=(10, 6))

# Skype demand curves
plt.plot(Q, D_skype_initial, label="Initial Demand for Skype (D1_skype)", linestyle='-', color='blue')
plt.plot(Q, D_skype_after, label="Reduced Demand for Skype (D2_skype)", linestyle='--', color='blue')

# Teams demand curves
plt.plot(Q, D_teams_initial, label="Initial Demand for Teams (D1_teams)", linestyle='-', color='green')
plt.plot(Q, D_teams_after, label="Increased Demand for Teams (D2_teams)", linestyle='--', color='green')

# Supply curves
plt.axhline(y=S_skype, color='blue', label="Supply for Skype (S_skype)", linestyle=':')
plt.axhline(y=S_teams, color='green', label="Supply for Teams (S_teams)", linestyle=':')

# Equilibrium points (Initial and after cannibalization)
# Initial equilibrium for Skype
eq_skype_Q1 = 80
eq_skype_P1 = S_skype
plt.plot(eq_skype_Q1, eq_skype_P1, 'ko')
plt.text(eq_skype_Q1 + 2, eq_skype_P1 + 2, 'E1 Skype')

# After cannibalization for Skype
eq_skype_Q2 = 40
eq_skype_P2 = S_skype
plt.plot(eq_skype_Q2, eq_skype_P2, 'ko')
plt.text(eq_skype_Q2 + 2, eq_skype_P2 + 2, 'E2 Skype')

# Initial equilibrium for Teams
eq_teams_Q1 = 10
eq_teams_P1 = S_teams
plt.plot(eq_teams_Q1, eq_teams_P1, 'ko')
plt.text(eq_teams_Q1 + 2, eq_teams_P1 + 2, 'E1 Teams')

# After cannibalization for Teams
eq_teams_Q2 = 50
eq_teams_P2 = S_teams
plt.plot(eq_teams_Q2, eq_teams_P2, 'ko')
plt.text(eq_teams_Q2 + 2, eq_teams_P2 + 2, 'E2 Teams')

# Labels and Titles
plt.title('Cannibalisation of Skype by Microsoft Teams')
plt.xlabel('Quantity of Users (Q)')
plt.ylabel('Perceived Value or Utility (P)')
plt.legend()
plt.grid(True)

# Display the plot
plt.show()

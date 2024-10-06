import numpy as np
import matplotlib.pyplot as plt

# Data for Pre-COVID (2015-2019) and Post-COVID (2020-2025)
years = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025])

# Number of users (millions) for Skype, Zoom, and Teams over time
skype_users = np.array([300, 290, 280, 260, 250, 200, 150, 100, 80, 60, 50])
zoom_users = np.array([10, 20, 40, 60, 80, 200, 300, 400, 450, 470, 480])
teams_users = np.array([5, 10, 15, 30, 50, 150, 250, 350, 400, 420, 430])

# CAC (in dollars) for Skype, Zoom, and Teams over time
skype_cac = np.array([5, 6, 7, 8, 10, 15, 18, 20, 22, 25, 30])
zoom_cac = np.array([50, 45, 40, 35, 30, 20, 15, 10, 10, 8, 7])
teams_cac = np.array([60, 55, 50, 45, 40, 25, 18, 15, 12, 10, 8])

# Plotting Pre-COVID vs Post-COVID CAC vs Users for Skype, Zoom, and Teams
plt.figure(figsize=(10, 6))

# Pre-COVID (2015-2019)
plt.plot(skype_users[:5], skype_cac[:5], label="Skype Pre-COVID", color='blue', linestyle='--', marker='o')
plt.plot(zoom_users[:5], zoom_cac[:5], label="Zoom Pre-COVID", color='red', linestyle='--', marker='o')
plt.plot(teams_users[:5], teams_cac[:5], label="Teams Pre-COVID", color='green', linestyle='--', marker='o')

# Post-COVID (2020-2025)
plt.plot(skype_users[5:], skype_cac[5:], label="Skype Post-COVID", color='blue', marker='o')
plt.plot(zoom_users[5:], zoom_cac[5:], label="Zoom Post-COVID", color='red', marker='o')
plt.plot(teams_users[5:], teams_cac[5:], label="Teams Post-COVID", color='green', marker='o')

# Labeling the graph
plt.title("Customer Acquisition Cost (CAC) vs Users: Pre- and Post-COVID")
plt.xlabel("Number of Users (in millions)")
plt.ylabel("Customer Acquisition Cost (CAC) in $")
plt.legend()

# Show plot
plt.grid(True)
plt.show()

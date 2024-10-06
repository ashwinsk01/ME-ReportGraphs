import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Years from 2015 to 2025
years = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025])

# Number of users (millions) for Skype, Zoom, and Teams over time
skype_users = np.array([300, 290, 280, 260, 250, 200, 150, 100, 80, 60, 50])
zoom_users = np.array([10, 20, 40, 60, 80, 200, 300, 400, 450, 470, 480])
teams_users = np.array([5, 10, 15, 30, 50, 150, 250, 350, 400, 420, 430])
google_meet_users = np.array([5, 10, 15, 30, 60, 120, 200, 300, 400, 420, 430])

# CAC (in dollars) for Skype, Zoom, Teams, and Google Meet over time
skype_cac = np.array([5, 6, 7, 8, 10, 15, 18, 20, 22, 25, 30])
zoom_cac = np.array([50, 45, 40, 35, 30, 20, 15, 10, 10, 8, 7])
teams_cac = np.array([60, 55, 50, 45, 40, 25, 18, 15, 12, 10, 8])
google_meet_cac = np.array([50, 45, 40, 35, 30, 20, 15, 10, 8, 7, 6])

# New users gained or lost (difference in user base)
new_skype_users = np.diff(skype_users, prepend=skype_users[0])
new_zoom_users = np.diff(zoom_users, prepend=zoom_users[0])
new_teams_users = np.diff(teams_users, prepend=teams_users[0])
new_google_meet_users = np.diff(google_meet_users, prepend=google_meet_users[0])

# Creating a 3D plot to show the relationship between new users gained/lost, CAC, and time (years)
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot for Zoom
ax.scatter(years, zoom_cac, new_zoom_users, label="Zoom", color='red', marker='o')

# Plot for Teams
ax.scatter(years, teams_cac, new_teams_users, label="Teams", color='green', marker='^')

# Plot for Skype
ax.scatter(years, skype_cac, new_skype_users, label="Skype", color='blue', marker='s')

# Plot for Google Meet
ax.scatter(years, google_meet_cac, new_google_meet_users, label="Google Meet", color='purple', marker='D')

# Set labels for the axes
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Invested CAC / person (USD)", fontsize=12)
ax.set_zlabel("New Users Gained or Lost (Millions)", fontsize=12)

# Set the title
ax.set_title("CAC vs Gain/Loss of Users Over Time (2015-2025)", fontsize=14)

# Add legend outside the plot for better readability
ax.legend(loc="upper left", bbox_to_anchor=(1, 1))

# Display the plot
plt.tight_layout()
plt.show()

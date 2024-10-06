import matplotlib.pyplot as plt

# Data
years = [2018, 2019, 2020, 2021, 2022, 2023]
skype_users = [300, 280, 260, 200, 150, 100]
teams_users = [10, 20, 75, 145, 270, 300]
zoom_users = [5, 10, 200, 300, 350, 370]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(years, skype_users, marker='o', label='Skype')
plt.plot(years, teams_users, marker='o', label='Microsoft Teams')
plt.plot(years, zoom_users, marker='o', label='Zoom')

# Annotations
plt.title('Market Share Trends (2018-2023)')
plt.xlabel('Year')
plt.ylabel('Number of Users (Millions)')
plt.xticks(years)
plt.legend()
plt.grid(True)

# Display the plot
plt.show()

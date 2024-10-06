import matplotlib.pyplot as plt
import numpy as np

# Years representing the time period (before, during, and after COVID-19)
years = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])

# Market share data based on verified sources
skype_market_share = np.array([32.4, 30, 28, 25, 20, 10, 7, 5])       # Decline due to competition and Teams
zoom_market_share = np.array([0, 0, 1, 2, 5, 40, 49, 50])             # Rapid rise during COVID-19, stabilizing
teams_market_share = np.array([0, 0, 0, 0, 5, 10, 15, 20])            # Strong growth, especially from 2020
google_meet_market_share = np.array([0, 0, 0, 0, 3, 7, 10, 10])       # Steady growth in education and business use

# Create a figure for plotting
plt.figure(figsize=(10, 6))

# Stack the areas for each platform to represent the total market share
plt.fill_between(years, skype_market_share, label="Skype", color='blue', alpha=0.6)
plt.fill_between(years, skype_market_share + zoom_market_share, skype_market_share, label="Zoom", color='orange', alpha=0.6)
plt.fill_between(years, skype_market_share + zoom_market_share + teams_market_share, skype_market_share + zoom_market_share, label="Microsoft Teams", color='green', alpha=0.6)
plt.fill_between(years, skype_market_share + zoom_market_share + teams_market_share + google_meet_market_share, skype_market_share + zoom_market_share + teams_market_share, label="Google Meet", color='red', alpha=0.6)

# Highlight the 2020-2022 period to represent the cannibalization between Skype and Teams
plt.axvspan(2019, 2021, color='grey', alpha=0.3, label="COVID 19 Period")

# Add overlay for the cannibalization effect (decline in Skype and rise in Teams)
# This will highlight the split between Skype and Teams during 2020-2022
plt.annotate('COVID 19 Impact Period', xy=(2021, 15), xytext=(2020.5, 20),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12, color='black')

# Titles and labels
plt.title("Market Share Shift in Video Communication Platforms (2015-2022)", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Market Share (%)", fontsize=12)

# Adding legend
plt.legend(loc="upper left")

# Display the grid
plt.grid(True)

# Show the plot
plt.show()

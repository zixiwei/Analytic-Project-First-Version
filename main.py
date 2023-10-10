import json
import matplotlib.pyplot as plt
import requests

# Firebase URL (make sure to replace it with your database URL)
DATABASE_URL = "https://mazeshift-marauders-67598-default-rtdb.firebaseio.com/"


headers = {}  # Add headers if necessary, e.g., for authentication
# headers = {"Authorization": "Bearer " + TOKEN}

response = requests.get(DATABASE_URL + ".json", headers=headers)
data = response.json()

# Parse data from JSON
player_ids = list(data['Player'].keys())
ages = [entry['age'] for entry in data['Player'].values()]

# Plotting
plt.figure(figsize=(10, 6))

plt.bar(player_ids, ages, color=['blue', 'green'])  # Use different colors for each bar
plt.title("Ages of Players")
plt.xlabel("Player IDs")
plt.ylabel("Age")
plt.xticks(rotation=45)  # Rotate x labels for better visibility
plt.tight_layout()
plt.show()


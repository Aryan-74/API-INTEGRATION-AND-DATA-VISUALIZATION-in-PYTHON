import requests
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# === CONFIG ===
API_KEY = "17c82542e754b30e1d3671f56ac8e78d"
CITY = "Delhi"
UNITS = "metric"
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units={UNITS}"

response = requests.get(URL)
data = response.json()

# === ERROR HANDLING ===
if 'list' not in data:
    print("Error fetching data:")
    print(data)
    exit()

# === PARSE DATES & TEMPS ===
dates_raw = []
temps = []

for forecast in data['list']:
    dt = datetime.strptime(forecast['dt_txt'], "%Y-%m-%d %H:%M:%S")
    dates_raw.append(dt)
    temps.append(forecast['main']['temp'])

# === CREATE SHORT X LABELS EVERY 8TH VALUE ===
tick_interval = 4  # You can also try 6 or 4
date_labels = [dt.strftime('%b %d\n%I %p') for dt in dates_raw]

# === PLOT ===
plt.figure(figsize=(14, 6))
sns.lineplot(x=range(len(temps)), y=temps, marker='o', color='steelblue')

# Set only some of the xticks
plt.xticks(
    ticks=range(0, len(date_labels), tick_interval),
    labels=[date_labels[i] for i in range(0, len(date_labels), tick_interval)],
    rotation=45,
    ha='right'
)

plt.title(f"5-Day Temperature Forecast for {CITY}", fontsize=14)
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.tight_layout()
plt.show()

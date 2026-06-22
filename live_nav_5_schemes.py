import requests
import pandas as pd

# SBI Bluechip
url = "https://api.mfapi.in/mf/119551"
response = requests.get(url)
data = response.json()
pd.DataFrame(data["data"]).to_csv("Data/Raw/sbi_bluechip_nav.csv", index=False)

# ICICI Bluechip
url = "https://api.mfapi.in/mf/120503"
response = requests.get(url)
data = response.json()
pd.DataFrame(data["data"]).to_csv("Data/Raw/icici_bluechip_nav.csv", index=False)

# Nippon Large Cap
url = "https://api.mfapi.in/mf/118632"
response = requests.get(url)
data = response.json()
pd.DataFrame(data["data"]).to_csv("Data/Raw/nippon_large_cap_nav.csv", index=False)

# Axis Bluechip
url = "https://api.mfapi.in/mf/119092"
response = requests.get(url)
data = response.json()
pd.DataFrame(data["data"]).to_csv("Data/Raw/axis_bluechip_nav.csv", index=False)

# Kotak Bluechip
url = "https://api.mfapi.in/mf/120841"
response = requests.get(url)
data = response.json()
pd.DataFrame(data["data"]).to_csv("Data/Raw/kotak_bluechip_nav.csv", index=False)

print("All NAV files saved")
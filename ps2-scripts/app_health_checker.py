import requests
from datetime import datetime

url = "https://wisecow.local"
log_file = "app_health.log"

try:
    response = requests.get(url, timeout=5, verify=False)  # disable SSL verification
    status = response.status_code
    if status == 200:
        result = f"{datetime.now()} - {url} is UP (HTTP {status})"
    else:
        result = f"{datetime.now()} - {url} is DOWN (HTTP {status})"
except requests.exceptions.RequestException as e:
    result = f"{datetime.now()} - {url} is DOWN (Exception: {e})"

print(result)

with open(log_file, "a") as f:
    f.write(result + "\n")
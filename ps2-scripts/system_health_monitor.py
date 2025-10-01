import psutil
from datetime import datetime

CPU_THRESHOLD = 80       # percent
MEM_THRESHOLD = 80       # percent
DISK_THRESHOLD = 90      # percent

log_file = "system_health.log"

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

cpu = psutil.cpu_percent(interval=1)
cpu_status = "OK" if cpu < CPU_THRESHOLD else "ALERT"

memory = psutil.virtual_memory().percent
mem_status = "OK" if memory < MEM_THRESHOLD else "ALERT"

disk = psutil.disk_usage("/").percent
disk_status = "OK" if disk < DISK_THRESHOLD else "ALERT"

processes = len(psutil.pids())

report = (
    f"{timestamp} - CPU: {cpu}% ({cpu_status}), "
    f"Memory: {memory}% ({mem_status}), "
    f"Disk: {disk}% ({disk_status}), "
    f"Running Processes: {processes}"
)

# Print to console
print(report)

# Write to log file
with open(log_file, "a") as f:
    f.write(report + "\n")
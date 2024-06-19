import psutil

# Define thresholds
CPU_THRESHOLD = 80.0  # percent
MEMORY_THRESHOLD = 80.0  # percent
DISK_THRESHOLD = 80.0   # percent

# Function to check CPU usage
def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        log_alert(f"High CPU usage detected: {cpu_usage}%")

# Function to check memory usage
def check_memory_usage():
    memory_usage = psutil.virtual_memory().percent
    if memory_usage > MEMORY_THRESHOLD:
        log_alert(f"High memory usage detected: {memory_usage}%")

# Function to check disk usage
def check_disk_usage():
    disk_usage = psutil.disk_usage('/').percent
    if disk_usage > DISK_THRESHOLD:
        log_alert(f"High disk usage detected: {disk_usage}%")
# Function to check running processes
def check_running_processes():
    # Example: check for specific process names
    processes_to_check = ['apache2', 'mysql', 'nginx']
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] in processes_to_check:
            log_alert(f"Process {proc.info['name']} is running (PID: {proc.info['pid']})")

# Function to log alerts (you can modify this to send alerts via email, etc.)
def log_alert(message):
    with open('system_monitor.txt', 'a') as log_file:
        log_file.write(f"{message}\n")
    print(message)

# Main function to run checks
def main():
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_running_processes()

if _name_ == "_main_":
    main()

import psutil
import time

print("System Monitor Started...\n")

while True:
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent

    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {memory}%")

    print("\nProcesses:")
    for proc in psutil.process_iter(['pid', 'name']):
        print(proc.info)

    print("-" * 40)
    time.sleep(3)


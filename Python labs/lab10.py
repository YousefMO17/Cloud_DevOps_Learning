server_name="web-01"

warning_threshold=75
max_attempts=3

attempts=0
cpu_usage_percent=95

print(f"Checking server:{server_name}")
while cpu_usage_percent >= warning_threshold and attempts < max_attempts:
    attempts += 1
    cpu_usage_percent=int(input("enter the CPU usage percentage: "))
    print(f"ATTEMPT # {attempts} - CPU : {cpu_usage_percent}%")

if cpu_usage_percent < warning_threshold:
    print("Server is HEALTHY")
else:
    print("Maximum attempts reached")
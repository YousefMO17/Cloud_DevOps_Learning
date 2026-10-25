cpu_readings = [45, 82, 96, 68, 90, 75]

warning_threshold = 75
critical_threshold = 90

print("=== CPU Monitoring Report ===")

def get_cpu_status(cpu,warning_threshold,critical_threshold):
    if cpu >= critical_threshold:
        return " CRTICAL"
    elif cpu >= warning_threshold:
        return " WARNING"
    else:
        return " NORMAL"



for cpu in cpu_readings:
    status= get_cpu_status(cpu,warning_threshold,critical_threshold)
    print(f"CPU: {cpu} - Status: {status}")
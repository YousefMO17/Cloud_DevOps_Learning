cpu_readings=[45,82,96,68]

warning_threshold=75
critical_threshold=90
print("=== CPU Monitoring Report ===")

for cpu in cpu_readings:
    
    if  cpu >= critical_threshold:
        status="CRITICAL"
    elif cpu >= warning_threshold:
        status="WARNING"
    else:
        status="NORMAL"
    print(f"CPU:{cpu}% - Status:{status}")


print(f"Total CPU Readings: {len(cpu_readings)}")

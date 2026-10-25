cpu_readings = [45, 82, 96, 68, 90, 75]

warning_threshold = 75
critical_threshold = 90

normal_count = 0
warning_count = 0
critical_count = 0

print("=== CPU Monitoring Report ===")


for cpu in cpu_readings:
    if cpu >= critical_threshold :
        status="CRITICAL"
        critical_count += 1

    elif cpu >= warning_threshold :
        status="WARNING"
        warning_count += 1

    else:
        status="NORMAL"
        normal_count += 1

    print(f"CPU: {cpu} % - {status}")
total_counts=normal_count+critical_count+warning_count
print("=== Monitoring Summary ===")
print(f"total readings: {total_counts}")
print(f"Normal: {normal_count}")
print(f"Warning: {warning_count}")
print(f"Critical: {critical_count}")
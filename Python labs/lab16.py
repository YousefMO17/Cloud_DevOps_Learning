disk_usages = [45, 82, 96, 68, 91, 75]

warning_threshold = 75
critical_threshold = 90

print("=== Disk Monitoring Summary ===")

def analyze_disk_usage (usages,warning_threshold,critical_threshold):
    normal_count=0
    warning_count=0
    critical_count=0
    for disk in disk_usages:
        if disk>=critical_threshold:
            status="CRITICAL"
            critical_count+=1
        elif disk>=warning_threshold:
            status="WARNING"
            warning_count+=1
        else:
            status="NORMAL"
            normal_count+=1
    return normal_count,warning_count,critical_count
normal,warning,critical=analyze_disk_usage(disk_usages,warning_threshold,critical_threshold)
result=normal+warning+critical
print(f"Total Servers:{result}")
print(f"Normal:{normal}")
print(f"Warning:{warning}")
print(f"Critical:{critical}")
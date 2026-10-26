disk_usages = [45, 82, 96, -10, 130, 68]

warning_threshold = 75
critical_threshold = 90

print("=== Disk Health Report ===")

def get_disk_status(usage, warning_threshold, critical_threshold):

    if usage < 0 or usage > 100:
        return"INVALID"

    if usage >= critical_threshold:
        return "CRITICAL"
    elif usage>= warning_threshold:
        return "WARINING"
    else:
        return " NORMAL"

for disk in disk_usages:
    status=get_disk_status(disk,warning_threshold,critical_threshold)
    print(f"Disk: {disk}% - Status: {status}")




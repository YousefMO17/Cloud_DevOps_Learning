server_name = "web-01"

cpu_usage = 83
disk_usage = 94

w_threshold = 75
c_threshold = 90



print("=== Server Resource Report ===")
print(f"Server:{server_name}")

def get_resource_status(usage, warning_threshold, critical_threshold):
    if usage >= critical_threshold:
        return "CRITICAL"

    elif usage >= warning_threshold:
        return "WARNING"

    else:
        return "NORMAL"


def analyze_server(cpu_usage, disk_usage, warning_threshold, critical_threshold):
   cpu_status=get_resource_status(cpu_usage,w_threshold,c_threshold)
   disk_usage=get_resource_status(disk_usage,w_threshold,c_threshold)
   return cpu_status,disk_usage


cpu_status, disk_status=analyze_server(cpu_usage,disk_usage,w_threshold,c_threshold)


print(f"CPU Usage:{cpu_usage}%-{cpu_status}")
print(f"Disk Usage: {disk_usage}%-{disk_status}")




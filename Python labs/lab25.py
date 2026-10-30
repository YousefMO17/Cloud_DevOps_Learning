env_configs = {
    "development": {
        "warning": 80,
        "critical": 95
    },
    "production": {
        "warning": 75,
        "critical": 90
    }
}

servers = [
    {
        "name": "web-01",
        "environment": "production",
        "resources": {
            "CPU": 82,
            "Memory": 66,
            "Disk": 94
        }
    },
    {
        "name": "db-01",
        "environment": "production",
        "resources": {
            "CPU": 0,
            "Memory": 91,
            "Disk": None
        }
    },
    {
        "name": "test-01",
        "environment": "development",
        "resources": {
            "CPU": 40,
            "Memory": 52,
            "Disk": 69
        }
    }
]
print("=== Server Health Monitor ===")


selected_environment = "production"
print(f"Environment: {selected_environment}")


config=env_configs.get(selected_environment)
if config is None :
    print("Environment not found")
else :
    warning_threshold=config["warning"]
    critical_threshold=config["critical"]
    print(f"Warning Threshold: {warning_threshold} % \nCritical Threshold:{critical_threshold}")

def get_resource_status(usage, warning_threshold, critical_threshold):
    if usage is None :
        return "UNKNOWN"
    elif usage >= critical_threshold:
        return "CRITICAL"
    elif usage >= warning_threshold:
        return "WARNING"
    else :
        return "NORMAL"

status_count={
    "NORMAL": 0,
    "WARNING": 0,
    "CRITICAL": 0,
    "UNKNOWN": 0
}

monitored_server=0
for server in servers:
    if server["environment"]==selected_environment:
        monitored_server+=1
        print(f"Server : {server["name"]}")
    for resource,usage in server["resources"].items():
        status=get_resource_status(usage,warning_threshold,critical_threshold)
        if usage is None:
            usage_display = "N/A"
        else:
            usage_display = f"{usage}%"

            print(f"{resource}: {usage_display} - {status}")

            status_count[status] += 1
print("\n=== Monitoring Summary ===")

print(f"\nMonitored Servers: {monitored_server}")

print(f"\nNORMAL: {status_count['NORMAL']}")
print(f"WARNING: {status_count['WARNING']}")
print(f"CRITICAL: {status_count['CRITICAL']}")
print(f"UNKNOWN: {status_count['UNKNOWN']}")
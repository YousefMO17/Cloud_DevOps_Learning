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

readings = [
    {"server": "web-01", "environment": "production", "cpu": 82},
    {"server": "db-01", "environment": "production", "cpu": 95},
    {"server": "cache-01", "environment": "production", "cpu": None},
    {"server": "worker-01", "environment": "production", "cpu": 91},
    {"server": "web-01", "environment": "production", "cpu": 93},
    {"server": "backup-01", "environment": "production", "cpu": 40},
    {"server": "db-01", "environment": "production", "cpu": 97},
    {"server": "test-01", "environment": "development", "cpu": 55}
]

selected_environment = "production"

config=env_configs.get(selected_environment)
if config is None :
    print("Environment not found")
else :
    warning_threshold=config["warning"]
    critical_threshold=config["critical"]

selected_readings=[
reading for reading in readings if reading["environment"]==selected_environment
]


def get_cpu_status(usage, warning_threshold, critical_threshold):
    if usage is None:
        return "UNKNOWN"
    elif usage >= critical_threshold:
        return "CRITICAL"
    elif usage>=warning_threshold:
        return "WARNING"
    else :
        return "NORMAL"


status_count={
    "NORMAL":0,
    "WARNING":0,
    "CRITICAL":0,
    "UNKNOWN":0
}
critical_servers=set()

for reading in readings:
    usage=reading["cpu"]
    status=get_cpu_status(usage,warning_threshold,critical_threshold)
    if status=="CRITICAL":
        critical_servers.add(reading["server"])


print("=== CPU Incident Triage Report ===\n\n")
print(f"Environment:{selected_environment}")
print(f"Warning Threshold: {warning_threshold} %")
print(f"Critical Threshold: {critical_threshold} %\n\n")

print(f"Total Readings: {len(readings)}")
print(f"Selected Readings: {len(selected_readings)}\n\n")


print("=== Incident Summary ===")
print(f"\nNORMAL: {status_count['NORMAL']}")
print(f"WARNING: {status_count['WARNING']}")
print(f"CRITICAL: {status_count['CRITICAL']}")
print(f"UNKNOWN: {status_count['UNKNOWN']}")

print(f"Unique Critical Servers: {len(critical_servers)}\n\n")

print("=== Critical Server Names ===")
for x in sorted(critical_servers):
    print(f"- {x}")

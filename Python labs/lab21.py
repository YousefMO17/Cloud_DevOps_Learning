servers = [
    {
        "name": "web-01",
        "disk_usage": 82
    },
    {
        "name": "db-01",
        "disk_usage": 94
    },
    {
        "name": "cache-01"
    },
    {
        "name": "worker-01",
        "disk_usage": 0
    }
]

warning_threshold = 75
critical_threshold = 90
missing_count=0
def get_disk_status(usage, warning_threshold, critical_threshold):
    if usage is None :
        return "UNKNOWN"
    if usage <0 or usage > 100 :
        return "INVALID"
    if usage >= critical_threshold :
        return "CRITICAL"
    elif usage >= warning_threshold:
        return "WARNING"
    else:
        return "NORMAL"

for server in servers :
    status=get_disk_status(server.get("disk_usage"),warning_threshold,critical_threshold)
    if status is "UNKNOWN":
        missing_count+=1
        
    print(f"Server :{server["name"]}")
    print(f"Disk:{server.get("disk_usage")}")
    print(f"STATUS : {status}")

print("=== Monitoring Summary ===")
print(f"Total Servers : {len(servers)}")
print(f"Missing Disk Readings: {missing_count}")



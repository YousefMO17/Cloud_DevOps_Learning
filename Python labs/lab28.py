servers = [
    {
        "name": "web-01",
        "status": "running",
        "cpu": 82
    },
    {
        "name": "db-01",
        "status": "running",
        "cpu": 95
    },
    {
        "name": "cache-01",
        "status": "stopped",
        "cpu": 70
    },
    {
        "name": "worker-01",
        "status": "running",
        "cpu": 91
    },
    {
        "name": "backup-01",
        "status": "stopped",
        "cpu": 20
    }
]

critical_threshold = 90

stopped_server=[
    server["name"] for server in servers if server["status"] == "stopped"
]

high_cpu_server=[ server["name"] for server in servers if server["cpu"] >=critical_threshold and server["status"]=="running"
]
print("=== Server Status Filter ===\n\n")

print(f"Total Servers: {len(servers)}")
print(f"Stopped Servers: {len(stopped_server)}")
print(f"High CPU Servers:{len(high_cpu_server)}\n\n")

print("=== Stopped Servers ===")
for x in sorted(stopped_server) :
    print(f"- {x}")

print("=== High CPU Servers ===")
for y in sorted(high_cpu_server):
    print(f"- {y}")

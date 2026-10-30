alerts = [
    {"server": "web-01", "status": "CRITICAL"},
    {"server": "db-01", "status": "WARNING"},
    {"server": "web-01", "status": "CRITICAL"},
    {"server": "cache-01", "status": "CRITICAL"},
    {"server": "db-01", "status": "CRITICAL"},
    {"server": "cache-01", "status": "CRITICAL"}
]

critical_events = 0
critical_servers = set()

print("=== Critical Alert Deduplicator ===")

for alert in alerts :
    if alert["status"]=="CRITICAL":
        critical_events+=1
        critical_servers.add(alert["server"])
print(f"Total Alerts :{len(alerts)}")
print(f"Critical Events:{critical_events}")
print(f"Unique Critical Servers:{len(critical_servers)}")

for server_name in sorted(critical_servers):
    print(f"-{server_name}")

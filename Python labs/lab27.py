expected_servers = {
    "web-01",
    "db-01",
    "cache-01",
    "worker-01"
}

reporting_servers = {
    "web-01",
    "cache-01",
    "unknown-01"
}
missing_server=expected_servers-reporting_servers
active_server=expected_servers & reporting_servers
unexpected_server=reporting_servers-expected_servers

print("=== Server Inventory Report ===\n\n")

print(f"Expected Servers:{len(expected_servers)}")
print(f"Reporting Servers:{len(reporting_servers)}\n")

print(f"Active Expected Servers:{len(active_server)}")
print(f"Missing Servers:{len(missing_server)}")
print(f"Unexpected Servers:{len(unexpected_server)}\n\n")

print("=== Missing Servers ===")

for server in sorted(missing_server):
    print(f"-{server}")


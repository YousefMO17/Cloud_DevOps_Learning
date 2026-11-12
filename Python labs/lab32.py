servers = [
    {"name": "web-01", "status": "RUNNING"},
    {"name": "db-01", "status": "RUNNING"},
    {"name": "cache-01", "status": "STOPPED"},
    {"name": "worker-01", "status": "RUNNING"}
]

file_path = "server_report.txt"
print("Server report generated successfully!")
with open (file_path,"w",encoding="utf-8") as file :
    file.write("=== Server Status Report ===\n\n")
    for server in servers :
        name=server["name"]
        status=server["status"]
        file.write(f"{name} : {status}\n")
    file.write(f"\n\nTotal Servers{len(servers)}")
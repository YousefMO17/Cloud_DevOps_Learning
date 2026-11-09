file_path = "servers.txt"
total_entries = 0
unique_servers = set()

print("=== Server Inventory Report ===")

with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        server_name=line.strip()
        if server_name != "":
            total_entries+=1
            unique_servers.add(server_name)

print(f"Total Valid Entries: {total_entries}")
print(f"Unique Servers: {len(unique_servers)}")

print("\n=== Servers ===")

for server in sorted(unique_servers):
    print(f"- {server}")
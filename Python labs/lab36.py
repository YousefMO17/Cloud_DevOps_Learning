
from pathlib import Path

script_dir = Path(__file__).resolve().parent
file_path = script_dir / "data" / "lab36_events.txt"

total_events = 0
high_cpu_events = 0
invalid_lines = 0
unique_servers = set()

print("=== Server Event Analyzer ===")

if file_path.is_file():

    with file_path.open("r", encoding="utf-8") as file:

        for line in file:
            line = line.strip()

            if line == "":
                continue

            parts = line.split("|")

            if len(parts) != 3:
                invalid_lines += 1
                continue

            time = parts[0].strip()
            server = parts[1].strip()
            event_type = parts[2].strip()

            total_events += 1
            unique_servers.add(server)

            if event_type == "HIGH CPU":
                high_cpu_events += 1

    print(f"\nTotal Valid Events: {total_events}")
    print(f"HIGH CPU Events: {high_cpu_events}")
    print(f"Invalid Lines: {invalid_lines}")
    print(f"Unique Servers: {len(unique_servers)}")

    print("\n=== Servers ===")

    for server in sorted(unique_servers):
        print(f"- {server}")

else:
    print("Log file not found!")

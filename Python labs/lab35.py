from pathlib import Path

script_dir = Path(__file__).resolve().parent
file_path = script_dir / "data" / "lab35_events.txt"

total_events = 0
high_cpu_events = 0

print("=== Server Log Inspector ===")
if file_path.is_file():
    with open(file_path,"r", encoding="utf-8") as file:

        for line in file:
            event = line.strip()

            if event != "":
                print(event)
                total_events += 1

                if "HIGH CPU" in event:
                    high_cpu_events += 1
    print(f"\nTotal Valid Events: {total_events}")
    print(f"HIGH CPU Events: {high_cpu_events}")

else:
    print("Log file not found!")

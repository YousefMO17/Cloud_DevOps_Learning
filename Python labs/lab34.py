file_path = "lab34_events.txt"

total_events = 0

print("=== Reliable Log Reader ===")

try:
    with open (file_path,"r" ,encoding="utf-8") as file :
        for line in file :
            event=line.strip()
            if event != "":
                print(event)
                total_events+=1
                print(f"Total event {total_events}")

except FileNotFoundError:
    print("Log file not found!")

print("Program finished.")
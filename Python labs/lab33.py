events = [
    {
        "time": "10:30",
        "server": "cache-01",
        "event": "SERVER STOPPED"
    },
    {
        "time": "10:45",
        "server": "db-01",
        "event": "CPU NORMAL"
    },
    {
        "time": "11:00",
        "server": "web-01",
        "event": "HIGH MEMORY"
    }
]

file_path = "server_events.log"

with open (file_path,"a",encoding="utf-8") as file :
    for x in events :
        time=x["time"]
        server=x["server"]
        event=x["event"]
        file.write(f"\nTIME {time}| SERVER {server}| EVENT {event}\n")

print("Events appended successfully!")
print(f"New Events: {len(events)}")
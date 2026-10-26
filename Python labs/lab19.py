server = {
"name" : "web-01",
"region" :"eu-west-1",
"cpu_usage": 83,
"memory_usage": 72,
"status": "RUNNING"
}
warning_threshold = 75
critical_threshold = 90

server["disk_usage"]=95


print ("=== Server Information Report ===")
print(f"Server:{server['name']} \n Region: {server['region']}\n Memory Usage: {server['memory_usage']}\n Status: {server['status']}\n")

def get_cpu_status(cpu_usage,warning_thresold,critical_threshold):
    if cpu_usage>= critical_threshold:
        return "CRITICAL"
    elif cpu_usage>=warning_threshold:
        return "WARNING"
    else :
        return "NORMAL"

cpu_status=get_cpu_status(server["cpu_usage"],warning_threshold,critical_threshold)

print (f"CPU Usage: {server['cpu_usage']}%- {cpu_status}\n Disk Usage: {server['disk_usage']}")
server_name = "web-01"

resources = {
    "CPU": 82,
    "Memory": 66,
    "Disk": 94
}

warning_threshold = 75
critical_threshold = 90
critical_count=0
print("=== Dynamic Resource Monitoring ===")
print(f"Server: {server_name}")


resources["network"]=95
def get_resource_status(usage, warning_threshold, critical_threshold):
    if usage>=critical_threshold:
        return"CRITICAL"
    elif usage >= warning_threshold :
        return "WARNING"
    else :
        return "NORMAL"




for resource,usage in resources.items() :
    status=get_resource_status(usage,warning_threshold,critical_threshold)
    if status =="CRITICAL" :
        critical_count+=1
    print(f":{resource}: {usage} % {status}")


print(f"Critical Resources:{critical_count}" )

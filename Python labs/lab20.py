servers=[
{
"name":"web-01",
"region":"eu-west-1",
"cpu_usage":83,
"memory_usage":72
},
{
"name":"db-01",
"region":"eu-central-1",
"cpu_usage":94,
"memory_usage":81
},
{
"name":"cashe-01",
"region":"eu-east-01",
"cpu_usage":52,
"memory_usage":43
},
{
"name":"worker-01",
"region":"eu-west-1",
"cpu_usage":68,
"memory_usage":91
}
]

warning_threshold = 75
critical_threshold = 90
normal_count=0
warning_count=0
critical_count=0

print("=== Server Fleet Health Report ===")


def get_resource_status(usage, warning_threshold, critical_threshold):
    if usage >= critical_threshold:
        status="CRITICAL"
    elif usage >= warning_threshold :
        status="WARNING"
    else:
        status="NORMAL"
    return status

for server in servers:
    cpu_status=get_resource_status(server["cpu_usage"],warning_threshold,critical_threshold)
    memory_status=get_resource_status(server["memory_usage"],warning_threshold,critical_threshold)
    if cpu_status == "CRITICAL" or memory_status == "CRITICAL":
        overall_status = "CRITICAL"

    elif cpu_status == "WARNING" or memory_status == "WARNING":
        overall_status = "WARNING"

    else:
        overall_status = "NORMAL"

    if overall_status=="CRITICAL":
        critical_count += 1
    elif overall_status=="WARNING":
        warning_count+=1
    else:
        normal_count+=1

    print(f"Server: {server['name']}")
    print(f"Region: {server['region']}")
    print(f"CPU: {server['cpu_usage']}%")
    print(f"Memory: {server['memory_usage']}%")
    print(f"Overall Status: {overall_status}")
    print()
print("=== Fleet Summary ===")
print(f"Total Servers:{len(servers)}")
print(f"Normal:{normal_count}")
print(f"Warning:{warning_count}")
print(f"Critical:{critical_count}")

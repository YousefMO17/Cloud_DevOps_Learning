cpu_usage = {
    "web-01": 82,
    "db-01": 95,
    "cache-01": 45,
    "worker-01": 91,
    "backup-01": 30
}

critical_threshold = 90


critical_severs={
    key:value

    for key,value in cpu_usage.items()
        if value>=critical_threshold
}
print("=== Critical CPU Monitoring ===\n\n")
print(f"Total Servers:{len(cpu_usage)}")
print(f"Critical Servers:{len(critical_severs)}\n\n")

print("=== Critical Server Details ===")

for x,y in sorted(critical_severs.items()):
    print(f"  {x} :{y} %")
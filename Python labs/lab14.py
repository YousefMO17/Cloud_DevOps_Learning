cpu_readings = [45, 82, 96, 68, 90, 75]
critical_threshold = 90

print("=== Critical CPU Summary ===")
def count_critical_readings (readings,threshold):
    critical_count =0
    for cpu in cpu_readings :
        if cpu >= critical_threshold :
            critical_count+=1
        else :
            critical_count+=0
    return critical_count


print(f"Total Readings: {len(cpu_readings)}")
result=count_critical_readings (cpu_readings,critical_threshold)
print(f"Critical Readings:{result}")
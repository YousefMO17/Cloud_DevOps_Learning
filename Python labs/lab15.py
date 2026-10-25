web_cpu_readings = [45, 82, 96, 68, 90]

db_cpu_readings = [60, 81, 85, 72, 95]

print("=== CPU Monitoring Summary ===")
def count_critical_readings (readings ,threshold =90 ):
    local_counter=0
    for result in readings :
        if result >= threshold:
            local_counter+=1
    return local_counter

# key argument 
web_result=count_critical_readings(web_cpu_readings)

print(f"Web Server Critical Readings: {web_result}")

#keyword argument

db_result= count_critical_readings(readings=web_cpu_readings,threshold=80)
print(f"Database Server Critical Readings: {db_result}")

server = {
    "name": "web-01",
    "region": "eu-west-1",
    "environment": "development",
    "monitoring": False
}

print("=== Server Configuration Report ===")
print(f"Server: {server['name']}\nRegion:{server['region']}\nEnvironment:{server['environment']}")

if "moniroting" in server :
    print("\n\nMonitoring setting found\n\n")
else :
    print("\n\nMonitoring setting missing\n\n")


server.update({
    "environment": "production",
    "monitoring" : "True"
})

server["backup_enabled"]=True

print ("=== Updated Configuration ===")

for key,value in server.items():
    print(f"{key} : {value}")





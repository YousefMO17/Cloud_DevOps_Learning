environments = {
    "development": {
        "region": "eu-west-1",
        "instance_type": "t3.micro",
        "monitoring": False
    },
    "production": {
        "region": "eu-central-1",
        "instance_type": "t3.medium",
        "monitoring": True
    }
}

selected_environment = "production"
print("=== Environment Configuration Report ===")

config=environments.get(selected_environment)
if config is None:
    print("Environment not found")
else :
    config["backup_enabled"]=True

print(f"Environment: {selected_environment}")


for key,value in config.items():
    print(f"{key} : {value}")


import platform
import os

os_name = os.name
platform_name = platform.system()
platform_version = platform.version()
platform_release = platform.release()
print(f"OS Name: {os_name}")
print(f"Platform: {platform_name}")
print(f"Platform Version: {platform_version}")
print(f"Platform Release: {platform_release}")


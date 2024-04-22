import subprocess

def get_wifi_profiles():
    try:
        # Run the netsh command to show all Wi-Fi profiles
        result = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], capture_output=True, text=True, check=True)
        output = result.stdout

        # Extract the Wi-Fi profile names from the output
        profiles = [line.split(":")[1].strip() for line in output.splitlines() if "All User Profile" in line]
        return profiles
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        return []

def get_wifi_password(profile):
    try:
        # Run the netsh command to show the password for a specific profile
        result = subprocess.run(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear'], capture_output=True, text=True, check=True)
        output = result.stdout

        # Extract the password from the output
        password_line = [line for line in output.splitlines() if "Key Content" in line]
        if password_line:
            password = password_line[0].split(":")[1].strip()
            return password
        else:
            print(f"No password found for Wi-Fi profile '{profile}'")
            return None
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        return None

def main():
    # Get the list of Wi-Fi profiles
    profiles = get_wifi_profiles()
    print("Wi-Fi profiles found:")
    for profile in profiles:
        print(profile)

        # Get the password for each Wi-Fi profile
        password = get_wifi_password(profile)
        if password:
            print("Password:", password)
        print()

if __name__ == "__main__":
    main()

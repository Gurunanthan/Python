import subprocess
def run_external_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        print("Command Output:")
        print(result.stdout)
        if result.stderr:
            print("Command Error:")
            print(result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
command = "ls"
run_external_command(command)

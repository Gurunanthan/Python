import os
def get_cpu_count():
    cpu_count = os.cpu_count()
    print(f"Number of CPUs: {cpu_count}")
get_cpu_count()


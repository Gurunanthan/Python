import site
def get_site_packages_location():
    site_packages = site.getsitepackages()
    print("Site-packages locations:")
    for directory in site_packages:
        print(directory)
get_site_packages_location()

import os
def print_status():
    os.system("git status")
def git_commit():
    os.system("git add .")
    print("Status before committing:")
    print_status()
    message = input("Enter commit message: ")
    commit_message = "main" if message == "" else message
    os.system('git commit - "%s"' % commit_message)
    confirm_commit = input("Are you sure you want to commit changes? (y/n): ").lower()
    if confirm_commit == "y":
        branch = input("Enter branch (e.g., 'master' or 'main'): ")
        os.system("git push origin %s" % branch)
    else:
        print("Commit canceled.")
if __name__ == "__main__":
    git_commit()

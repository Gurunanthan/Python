import os

def print_status():
    # Display the status of the repository
    os.system("git status")

def git_commit():
    # Print the status before committing

    # Get the commit message from the user
    commit_message = input("Enter commit message: ")

    # Add all modified files
    os.system("git add .")
    print("Status before committing:")
    print_status()

    # Commit changes with the provided commit message
    os.system('git commit -m "%s"' % commit_message)

    # Prompt the user to confirm the commit
    confirm_commit = input("Are you sure you want to commit changes? (yes/no): ").lower()
    if confirm_commit == "yes":
        # Push changes to the specified branch
        branch = input("Enter branch (e.g., 'master' or 'main'): ")
        os.system("git push origin %s" % branch)
    else:
        print("Commit canceled.")

if __name__ == "__main__":
    git_commit()

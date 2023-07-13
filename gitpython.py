import git
import shutil

# Define the repository URL
repo_url = "https://github.com/Aleksbogdanov12/singleton.git"

# Define the list of branches to clone
branches = ["go-client", "g11n-ruby-client", "g11n-java-client",
            "g11n-js-client", "g11n-csharp-client", "g11n-angular-client",
            "devops"]

# Set the target directory to the current directory
target_directory = "./"

# Loop through the branches and clone each one
for branch in branches:
    # Define the target directory for the current branch
    branch_directory = f"{target_directory}/{branch}"
    
    # Clone the branch using GitPython
    git.Repo.clone_from(repo_url, branch_directory, branch=branch)
    shutil.rmtree(f"{branch_directory}/.git")

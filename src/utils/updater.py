import subprocess
import shlex

fetch_command = "git fetch"
pull_command = "git pull origin"
log_command = "git log HEAD..origin/HEAD --oneline"


# NOTE: might refactor this code and well split into different files


def update_available(repo_path: str = ".") -> bool:
    """
    This function, using git, checks if an update is available.
    """
    try:
        print("Checking update")
        split_command = shlex.split(fetch_command)
        subprocess.run(
            split_command,
            cwd=repo_path,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        split_log = shlex.split(log_command)
        result = subprocess.run(
            split_log,
            cwd=repo_path,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        return bool(result.stdout.strip())
    except subprocess.CalledProcessError:
        return False


def updater():
    """
    This function uses the function above to see if the update is there, if truthy then we update using git pull
    """
    split_pull_command = shlex.split(pull_command)
    if update_available():
        print("Update available!")
        subprocess.run(
            split_pull_command,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        print("Updated!")

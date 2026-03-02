import shlex
import subprocess

fetch_command = "git fetch"
log_command = "git log HEAD..origin/HEAD --oneline"


def update_available(repo_path: str = ".") -> bool:
    """
    This function, using git, checks if an update is available.
    """
    try:
        print("Checking update...")
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
        # FIX: Truthy return logic, it always returns truthy even if theres no update.
        return bool(result.stdout.strip())
    except subprocess.CalledProcessError:
        return False

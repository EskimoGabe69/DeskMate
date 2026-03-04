import shlex
import subprocess

fetch_command = "git fetch"
log_command = "git log HEAD..origin/main --oneline"


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
        )
        split_log = shlex.split(log_command)
        result = subprocess.Popen(
            split_log,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        stdout, stderr = result.communicate()

        commit_count = len(stdout.strip().splitlines()) if stdout.strip() else 0

        return bool(commit_count > 0)
    except subprocess.CalledProcessError:
        return False

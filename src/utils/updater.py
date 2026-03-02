import subprocess
import shlex
from utils.update_available import update_available

pull_command = "git pull origin dev-branch"


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
    else:
        print("No Update available!")

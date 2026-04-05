import subprocess
import shlex
from utils.update_available import update_available
from utils.update_choice import update_choice

pull_command = "git pull origin dev-branch"


def updater():
    """
    This function uses the function above to see if the update is there, if truthy then we update using git pull
    """
    split_pull_command = shlex.split(pull_command)
    if update_available():
        print("Update available!")
        if update_choice():
            subprocess.run(
            split_pull_command,
            check=True,
            )
            print("Updated!")
        else:
            print("Update skipped!")
    else:
        print("No Update available!")

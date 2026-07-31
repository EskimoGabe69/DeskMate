import subprocess
import shlex


class ApplicationUpdater:
    def __init__(self) -> None:
        self.pull_command = "git pull origin dev-branch"
        self.fetch_command = "git fetch"
        self.log_command = "git log HEAD..origin/main --oneline"

    def update_available(self, repo_path: str = ".") -> bool:
        """
        This function, using git, checks if an update is available.
        """
        try:
            print("Checking update...")
            split_command = shlex.split(self.fetch_command)
            subprocess.run(
                split_command,
                cwd=repo_path,
                check=True,
            )
            split_log = shlex.split(self.log_command)
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

    def update_choice(self):
        updated_choice_string = input("Do you want to update the application? Y/N?")
        if updated_choice_string.lower() == "y":
            return True
        elif updated_choice_string.lower() == "n":
            return False

    def update_message(self) -> str:
        if self.update_available():
            return "Theres an Update available!\nFor Deskmate!"
        else:
            return ""

    def updater(self):
        """
        This function uses the function above to see if the update is there, if truthy then we update using git pull
        """
        split_pull_command = shlex.split(self.pull_command)
        if self.update_available():
            print("Update available!")
            if self.update_choice():
                subprocess.run(
                    split_pull_command,
                    check=True,
                )
                print("Updated!")
            else:
                print("Update skipped!")
        else:
            print("No Update available!")

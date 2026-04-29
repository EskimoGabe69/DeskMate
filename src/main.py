from core.app import app
from utils.updater import updater

if __name__ == "__main__":
    # TODO: Maybe add a reminder that a new update exists!
    updater()
    app()

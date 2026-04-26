from core.app import app
from utils.updater import updater

if __name__ == "__main__":
    # TODO: Maybe gonna add some GUI pop up for the updater so that you dont interact with the CLI, maybe a version a interactive updater?
    updater()
    app()

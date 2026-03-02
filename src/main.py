# from core.app import app
from utils.updater import updater
# icon_path = "./assets/first_logo.png"

if __name__ == "__main__":
    # NOTE: Here I will add the automatic updater which will execute everytime the program starts.
    # app(icon_path)
    updater()

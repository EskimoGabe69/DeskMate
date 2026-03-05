from core.app import app
from utils.updater import updater

icon_path = "./assets/first_logo.png"

if __name__ == "__main__":
    updater()
    app(icon_path)
    

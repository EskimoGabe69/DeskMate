from core.app import app
from utils.updater import updater

icon_path = "./assets/deskmate_logo.svg"
css_path = "./assets/styles.css"
if __name__ == "__main__":
    updater()
    app(icon_path, css_path)

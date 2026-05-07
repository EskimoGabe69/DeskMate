from utils.update_available import update_available


def update_message() -> str:
    if update_available():
        return "Update available!"
    else:
        return ""

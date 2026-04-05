def update_choice():
    updated_choice_string = input("Do you want to update the application? Y/N?")
    if updated_choice_string.lower() == "y":
        return True
    elif updated_choice_string.lower() == "n":
        return False 

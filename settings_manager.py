test_settings = {
   'Theme': 'dark',
   'Notifications': 'enabled',
   'Volume': 'high'
}

def add_setting(test_settings, setting_types):
    key, value = setting_types
    key = key.lower()
    value = value.lower()
    if key in test_settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        test_settings.update({key: value})
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(test_settings, setting_types):
    key, value = setting_types
    key = key.lower()
    value = value.lower()
    if key in test_settings:
        test_settings.update({key: value})
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(test_settings, key):
    key = key.lower()
    if key in test_settings:
        test_settings.pop(key)
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"

def view_settings(test_settings):
    if test_settings == {}:
        return "No settings available."
    else:
        string_settings = ""
        for key, value in test_settings.items():
            string_settings += f"{key.capitalize()}: {value}\n"
        return f"Current User Settings:\n{string_settings}"
    
if __name__ == "__main__":
    print(add_setting(test_settings, ('language', 'english')))
    print(update_setting(test_settings, ('volume', 'low')))
    print(delete_setting(test_settings, 'theme'))
    print(view_settings(test_settings))    

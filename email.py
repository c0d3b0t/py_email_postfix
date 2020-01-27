import os
import json

def get_new_email():
    return "example+" + str(increment_email_postfix()) + "@gmail.com"

def increment_email_postfix():
    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(dir_path+'/settings.json', 'r+') as json_file:
        data = json.load(json_file)
        data['postfix'] += 1

        json_file.seek(0)
        json_file.write(json.dumps(data))

        return data['postfix']

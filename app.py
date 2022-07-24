# NOOBZHAX 2022

import json, time, os, heroku3, os.path
from datetime import datetime

file = os.path.exists('data.json')


if file:
	print("JSON file available ...")
	with open(file, 'r') as f:
		data = json.load(f)
else:
	print("Trying to get from env")
	data = os.environ.get('DATAS', '')

# print(data)


def changeDyno(apikey, appname, proc, typ):
    try:
        hcon = heroku3.from_key(apikey)
        app = hcon.app(appname)
        print("Scaling app, please wait ...")
        app.process_formation()[proc].scale(int(typ))
        print("Scale successfully")
    except Exception as e:
        pass
        print(e)


today = datetime.now()

try:
    if today.day == 15:
        print("Changing the dyno to second account ...")
        for i in data['datas']:
            proc = i['proc']
            api_a = i['app']['api_a']
            name_a = i['app']['name_a']
            print(f"Scalling down : {name_a},  Type: {proc} ")
            changeDyno(api_a, name_a, proc, 0)
            time.sleep(5)

        print("The app in first acc has been scaled down.")
        time.sleep(5)

        for i in data['datas']:
            proc = i['proc']
            api_b = i['app']['api_b']
            name_b = i['app']['name_b']
            changeDyno(api_b, name_b, proc, 1)
            print(f"Scalling Up : {name_b},  Type: {proc} ")
            time.sleep(5)

        print("The app in second acc has been scaled up.")
        time.sleep(2)
        print("Your first app has been shifted to second account ...")

    elif today.day == 1:
        print("Changing the dyno to first account ...")
        for i in data['datas']:
            proc = i['proc']
            api_b = i['app']['api_b']
            name_b = i['app']['name_b']
            print(f"Scalling down : {name_b},  Type: {proc} ")
            changeDyno(api_a, name_a, proc, 0)
            time.sleep(5)

        print("The app in second acc has been scaled down.")
        time.sleep(5)

        for i in data['datas']:
            proc = i['proc']
            api_a = i['app']['api_a']
            name_a = i['app']['name_a']
            print(f"Scalling Up : {name_a},  Type: {proc} ")
            changeDyno(api_b, name_b, proc, 1)
        print("The app in second acc has been scaled up.")
        time.sleep(2)
        print("Your first app has been shifted to first account ...")

    else:
        print("Today is not 1st or 15nd.")

except Exception as e:
    print(e)

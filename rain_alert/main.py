import requests
import os
from twilio.rest import Client


LAT = 40.8333
LGT = 14.25
api_key = "3ab560495f43d4364621e4885ba514ce"
#api_key = os.environ.get("OWM_API_KEY")
#To create env variable type export OWM_API_KEY=3ab560495f43d4364621e4885ba514ce
#If you wish to execute in  python anywhere you must specify the export command above separated by ";" from python3 main.py
#in the task set
list = []

parameters = {
    "lat": LAT,
    "lon": LGT,
    "appid": api_key,
    "exclude": "current, minutely, daily"
}

#response = requests.get(url="https://api.openweathermap.org/data/3.0/onecall", params=parameters)
#response.raise_for_status()
#weather_data = response.json()

account_sid = 'ACaed10d32db6af315419aac4df12a5c43'
auth_token = '1141a452152ac89abd6593e66fbc5f92'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+14847151706',
                     to='+393406827611'
                 )

print(message.status)

# Hourly_data =weather_data["hourly"]
#
#
# list.append(Hourly_data[0:12]["weather"][0]["id"])
#
# list_new = [id for id in list if id < 700]
# if len(list_new) != 0:
#     print("Bring umbrella")

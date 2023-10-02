import requests
import datetime
from requests.auth import HTTPBasicAuth
import os


APP_ID = "9b8ccff3"
#os.environ["APP_ID"] = APP_ID
#APP_ID = os.environ.get("APP_ID")
API_KEY = "ead0845f80fc055fff2716b3d7e61c0d"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/64e694c4cead86825515b5bf1e9d575f/eduardo'sWorkouts/workouts"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "height_cm": 166,
    "age": 39,
    "weight_kg": "82",
    "gender": "male",
    "query": input("Tell me which exercise you did: ")
}

response = requests.post(url=exercise_endpoint, headers=headers, json=parameters)
data = response.json()
print(data)

date = datetime.datetime.now().strftime("%d/%m/%y")
time = datetime.datetime.now().strftime("%H:%M:%S")
exercise = data["exercises"][0]["user_input"].title()
duration = data["exercises"][0]["duration_min"]
calories = data["exercises"][0]["nf_calories"]
print(exercise, duration, calories)

headers_sheety = {
    "Authorization": "Basic cGlwcG86cGFwZXJpbm8=",
    "Content-Type": "application/json"
}

row_of_data = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories,
    }
}

response = requests.post(url=sheety_endpoint, headers=headers_sheety, json=row_of_data)
print(response.status_code)
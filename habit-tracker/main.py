import requests
import datetime

USERNAME = "skyflye"
TOKEN = "kjashdkashdkashd"
pixela_endpoint = "https://pixe.la/v1/users"

user_params ={
    "token": "kjashdkashdkashd",
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id" : "graph1",
    "name" : "Walking Graph",
    "unit": "Km",
    "type": "float",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

pixel_post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

pixel_config = {
    "date": "20230701",
    "quantity": "7.50",
}

#response = requests.post(url=pixel_post_endpoint, json=pixel_config, headers=headers)
#print(response.text)

yesterday = datetime.datetime(year=2023, month=6, day=30)

pixel_config = {
    "date": yesterday.strftime("%Y%m%d"),
    "quantity": "6",
}

response = requests.post(url=pixel_post_endpoint, json=pixel_config, headers=headers)
print(response.text)

pixel_config_put = {
    "quantity": "6.5",
}

pixel_put_endpoint = f"{pixel_post_endpoint}/{yesterday.strftime('%Y%m%d')}"
response = requests.put(url=pixel_put_endpoint, headers=headers, json=pixel_config_put)
print(response.text)
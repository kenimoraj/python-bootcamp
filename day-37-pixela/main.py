import os

import requests


USER = os.environ['USER']
TOKEN = os.environ['TOKEN']
USER_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{USER_ENDPOINT}/{USER}/graphs"
# --------------- CREATE USER ---------------------- #
# $ curl -X POST https://pixe.la/v1/users -d '{"token":"thisissecret", "username":"a-know", "agreeTermsOfService":"yes", "notMinor":"yes"}'


# cre_usr_json = {
#
#     "token": TOKEN,
#     "username": USER,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
#
# response = requests.post(url=USER_ENDPOINT, json=cre_usr_json)
# response.raise_for_status()
# print(response.json())

# --------------- CREATE GRAPH --------------------- #
# $ curl -X POST https://pixe.la/v1/users/a-know/graphs -H 'X-USER-TOKEN:thisissecret' -d '{"id":"test-graph","name":"graph-name","unit":"commit","type":"int","color":"shibafu"}'



# headers = {
#     "X-USER-TOKEN": TOKEN
# }
#
# cregraph_json = {
#     "id": "testgraph1",
#     "name": "Test Graph",
#     "unit": "commit",
#     "type": "int",
#     "color": "sora"
# }
#
# response = requests.post(url=GRAPH_ENDPOINT, json=cregraph_json, headers=headers)
# response.raise_for_status()
# print(response.json())
# --------------- POST TO GRAPH -------------------- #

# 4 za przedwczoraj, 5 za wczoraj, 20 za dzisiaj

# $ curl -X POST https://pixe.la/v1/users/a-know/graphs/test-graph -H 'X-USER-TOKEN:thisissecret' -d '{"date":"20180915","quantity":"5"}'

endpoint = f"{GRAPH_ENDPOINT}/testgraph1"

headers = {
    "X-USER-TOKEN": TOKEN
}

json_data1 = {

    "date": "20230922",
    "quantity": "4"
}

json_data2 = {

    "date": "20230923",
    "quantity": "5"
}

json_data3 = {

    "date": "20230924",
    "quantity": "20"
}

for j in [json_data1, json_data2, json_data3]:
    response = requests.post(url=endpoint, json=j, headers=headers)
    response.raise_for_status()

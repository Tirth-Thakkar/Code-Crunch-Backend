import requests
import json
from werkzeug.security import generate_password_hash, check_password_hash

#url = "some url that has json with passwords" # Not a real url rn. Later flask API content will be here.

#response = requests.request("GET", url)
#password_list = response.json
users = [
        {
            "username": "JeraldLovesBlueberries",
            "email": "100%legit@emailAddress.pizza",
            "password": "P@$$w0rd"
        },

        {
            "username": "EdgeLord69420",
            "email": "EdgeLord69420@emailAddress.pizza",
            "password": "EdgeLord69420"
        },

        {
            "username": "JhonnoLovesCats",
            "email": "CatsAreCool@email.com",
            "password": "1L0v3Mr.T1bbl3$"
        },

        {
            "username": "ShrekIsLoveShrekIsLife",
            "email": "ShrekIsLoveShrekIsLife@emailAddress.pizza",
            "password": "ShrekIsLoveShrekIsLife"
        },

        {
            "username": "Hardcore_Gamer",
            "email": "Hardcore_Gamer@emailAddress.pizza",
            "password": "Hardcore_Gamer"
        }
    ]

password_list = []
for user in users:
    password_list.append(generate_password_hash(user["password"]))
#print(password_list)
test_password = password_list[0]
decrypted = check_password_hash(test_password, "P@$$w0rd")
if decrypted:
    print("This uid and password works")
else: print("There is something wrong with your uid or password, please reenter the correct information.")
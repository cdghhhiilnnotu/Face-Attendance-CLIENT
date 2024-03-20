import requests
import json

BASE_DIR = "http://127.0.0.1:5000/"

user = {}
def logging_user(username, password):
    try:
        user = requests.get(BASE_DIR + f"/giaovien/logging/{username}/{password}").json()
        return user
    except:
        print("FAIL TO GET API")
        return {}
    
def success_login(username):
    api = requests.get(BASE_DIR + f"/giaovien/login_success/{username}").json()
    with open("api1.json", "w", encoding='utf-8') as outfile:
        json.dump(api, outfile,ensure_ascii=False)



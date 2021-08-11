import requests
import json

# Opens the config.json file and looks for settings
cfg = {}
with open('config.json') as Json:
    cfg = json.load(Json)

# Returns an array with the data and the key
def get(key):
    con = requests.get(cfg['server'] + '/documents/' + key)
    return con.text

# Sends a data and returns an array witk the key
def post(data):
    con = requests.post(cfg['server'] + '/documents/', data=data.encode('UTF-8'))
    return con.text

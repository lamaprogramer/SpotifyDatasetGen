import pandas as pd
import spotify_auth
import spotify_requests
import os, json

def loadSecrets():
    file = open("./data/secrets.json", "r")
    json_data = json.load(file)
    file.close()
    return json_data

def main():
    SECRETS = loadSecrets()
    SPOTIFY_ACCESS_TOKEN = spotify_auth.readAccessToken(SECRETS["SPOTIFY_CLIENT_ID"], SECRETS["SPOTIFY_CLIENT_SECRET"])
    
main()
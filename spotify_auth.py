import requests, time

def fetchAccessToken(client_id: str, client_secret: str):
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {"grant_type": "client_credentials", "client_id": client_id, "client_secret": client_secret}
    
    response = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=data)
    return response.json()
    

def storeAccessToken(accessToken: str, validityDuration: float):
    token_file = open("data/token.txt", "w")
    token_file.write(accessToken + "\n")
    token_file.write(str(time.time() + validityDuration))
    token_file.close()


def readAccessToken(client_id: str, client_secret: str):
    try:
        token_file = open("data/token.txt", "r")
        token = token_file.readline().replace("\n", "")
        use_by = float(token_file.readline())
        if time.time() > use_by:
            print("Loaded token from request.")
            token = fetchAccessToken(client_id, client_secret)
            storeAccessToken(token["access_token"], token["expires_in"])
            return token["access_token"]
        print("Loaded token from cache.")
        #print("Valid for: " + str(use_by-time.time()))
        token_file.close()
        return token
    except FileNotFoundError:
        print("Could not find token, writing new token.")
        token = fetchAccessToken(client_id, client_secret)
        storeAccessToken(token["access_token"], token["expires_in"])
        return token["access_token"]
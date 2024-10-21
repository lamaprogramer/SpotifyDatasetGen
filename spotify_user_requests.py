import request_util

def getTracks(access_token: str, market: str = "", limit: int = 10, offset: int = 0):
    params = {"market": market, "limit": limit, "offset": offset}
    response = request_util.get("https://api.spotify.com/v1/me/tracks/contains", access_token, params=request_util.genParams(params))
    return response.json()

def saveTracks(ids: list, access_token: str):
    params = {"ids": ids}
    response = request_util.put("https://api.spotify.com/v1/me/tracks/contains", access_token, params=request_util.genParams(params))
    return response.json()

def deleteTracks(ids: list, access_token: str):
    params = {"ids": ids}
    response = request_util.delete("https://api.spotify.com/v1/me/tracks/contains", access_token, params=request_util.genParams(params))
    return response.json()

def containsTracks(ids: list, access_token: str):
    params = {"ids": ids}
    response = request_util.get("https://api.spotify.com/v1/me/tracks/contains", access_token, params=request_util.genParams(params))
    return response.json()
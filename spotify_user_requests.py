import request_util

# User Track Player Operations
def getPlaybackState(access_token: str, market: str = "", additional_types: str = ""):
    params = {"market": market, "additional_types": additional_types}
    response = request_util.get("https://api.spotify.com/v1/me/player", access_token, params=request_util.genParams(params))
    return response.json()

def transferPlayback(device_ids: list, access_token: str, play: bool = None):
    data = {"device_ids": device_ids, "play": play}
    response = request_util.put("https://api.spotify.com/v1/me/player", access_token, data=data)
    return response.json()

def getAvaliableDevices(access_token: str):
    response = request_util.get("https://api.spotify.com/v1/me/player/devices", access_token)
    return response.json()

def getCurrentPlayingTrack(access_token: str, market: str = "", additional_types: str = ""):
    params = {"market": market, "additional_types": additional_types}
    response = request_util.get("https://api.spotify.com/v1/me/player/currently-playing", access_token, params=request_util.genParams(params))
    return response.json()

def startOrResumePlayback(access_token: str, device_id: str = "", context_uri: str = "", uris: str = "", offset: dict = None, position_ms: int = None):
    params = {"device_id": device_id}
    data = {"context_uri": context_uri, "uris": uris, "offset": offset, "position_ms": position_ms}
    response = request_util.put("https://api.spotify.com/v1/me/player/play", access_token, params=request_util.genParams(params), data=data)
    return response.json()

def pausePlayback(access_token: str, device_id: str = ""):
    params = {"device_id": device_id}
    response = request_util.put("https://api.spotify.com/v1/me/player/pause", access_token, params=request_util.genParams(params))
    return response.json()

def skipToNext(access_token: str, device_id: str = ""):
    params = {"device_id": device_id}
    response = request_util.post("https://api.spotify.com/v1/me/player/next", access_token, params=request_util.genParams(params))
    return response.json()

def skipToPrevious(access_token: str, device_id: str = ""):
    params = {"device_id": device_id}
    response = request_util.post("https://api.spotify.com/v1/me/player/previous", access_token, params=request_util.genParams(params))
    return response.json()

def seekToPosition(position_ms: int, access_token: str, device_id: str = ""):
    params = {"position_ms": position_ms, "device_id": device_id}
    response = request_util.put("https://api.spotify.com/v1/me/player/seek", access_token, params=request_util.genParams(params))
    return response.json()

def setRepeat(state: str, access_token: str, device_id: str = ""):
    params = {"state": state, "device_id": device_id}
    response = request_util.put("https://api.spotify.com/v1/me/player/repeat", access_token, params=request_util.genParams(params))
    return response.json()

def setPlaybackVolume(volume_percent: int, access_token: str, device_id: str = ""):
    params = {"volume_percent": volume_percent, "device_id": device_id}
    response = request_util.put("https://api.spotify.com/v1/me/player/volume", access_token, params=request_util.genParams(params))
    return response.json()

def setShuffle(state: str, access_token: str, device_id: str = ""):
    params = {"state": state, "device_id": device_id}
    response = request_util.put("https://api.spotify.com/v1/me/player/shuffle", access_token, params=request_util.genParams(params))
    return response.json()

def getRecentlyPlayedTracks(access_token: str, limit: int = None, after: int = None, before: int = None):
    params = {"limit": limit, "after": after, "before": before}
    response = request_util.get("https://api.spotify.com/v1/me/player/recently-played", access_token, params=request_util.genParams(params))
    return response.json()

def getPlaybackQueue(access_token: str):
    response = request_util.get("https://api.spotify.com/v1/me/player/queue", access_token)
    return response.json()

def addToPlaybackQueue(uri: str, access_token: str, device_id: str = ""):
    params = {"uri": uri, "device_id": device_id}
    response = request_util.post("https://api.spotify.com/v1/me/player/queue", access_token, params=request_util.genParams(params))
    return response.json()


# User Playlist Operations
def getMyPlaylists(access_token: str, limit: int = None, offset: int = None):
    params = {"limit": limit, "offset": offset}
    response = request_util.get("https://api.spotify.com/v1/me/playlists", access_token, params=request_util.genParams(params))
    return response.json()

def getUserPlaylists(user_id: str, access_token: str, limit: int = None, offset: int = None):
    params = {"limit": limit, "offset": offset}
    response = request_util.get("https://api.spotify.com/v1/users/"+user_id+"/playlists", access_token, params=request_util.genParams(params))
    return response.json()

def createPlaylist(user_id: str, name: str, access_token: str, public: bool = None, collaborative: bool = None, description: str = ""):
    data = {"name": name, "public": public, "collaborative": collaborative, "description": description}
    response = request_util.post("https://api.spotify.com/v1/users/"+user_id+"/playlists", access_token, data=data)
    return response.json()


# User Show Operations
def getMyShows(access_token: str, limit: int = None, offset: int = None):
    params = {"limit": limit, "offset": offset}
    response = request_util.get("https://api.spotify.com/v1/me/shows", access_token, params=request_util.genParams(params))
    return response.json()

def saveShows(ids: list, access_token: str):
    params = {"ids": ids}
    response = request_util.put("https://api.spotify.com/v1/me/shows", access_token, params=request_util.genParams(params))
    return response.json()

def deleteShows(ids: list, access_token: str):
    params = {"ids": ids}
    response = request_util.delete("https://api.spotify.com/v1/me/shows", access_token, params=request_util.genParams(params))
    return response.json()

def containsShows(ids: list, access_token: str):
    params = {"ids": ids}
    response = request_util.get("https://api.spotify.com/v1/me/shows/contains", access_token, params=request_util.genParams(params))
    return response.json()


# User Track Operations
def getMyTracks(access_token: str, market: str = "", limit: int = None, offset: int = None):
    params = {"market": market, "limit": limit, "offset": offset}
    response = request_util.get("https://api.spotify.com/v1/me/tracks", access_token, params=request_util.genParams(params))
    return response.json()

def saveTracks(ids: list, access_token: str):
    params = {"ids": ids}
    response = request_util.put("https://api.spotify.com/v1/me/tracks", access_token, params=request_util.genParams(params))
    return response.json()

def deleteTracks(ids: list, access_token: str):
    params = {"ids": ids}
    response = request_util.delete("https://api.spotify.com/v1/me/tracks", access_token, params=request_util.genParams(params))
    return response.json()

def containsTracks(ids: list, access_token: str):
    params = {"ids": ids}
    response = request_util.get("https://api.spotify.com/v1/me/tracks/contains", access_token, params=request_util.genParams(params))
    return response.json()


# User Profile Operations
def getMyrofile(access_token: str):
    response = request_util.get("https://api.spotify.com/v1/me", access_token)
    return response.json()

def topItems(type: str, access_token: str, time_range: str = "", limit: int = None, offset: int = None):
    params = {"time_range": time_range, "limit": limit, "offset": offset}
    response = request_util.get("https://api.spotify.com/v1/me/top/"+type, access_token, params=request_util.genParams(params))
    return response.json()

def getUserProfile(user_id: str, access_token: str):
    response = request_util.get("https://api.spotify.com/v1/users/"+user_id, access_token)
    return response.json()

def followPlaylist(playlist_id: str, access_token: str, public: bool = None):
    data = {"public": public}
    response = request_util.put("https://api.spotify.com/v1/playlists/"+playlist_id+"/followers", access_token, data=data)
    return response.json()

def unfollowPlaylist(playlist_id: str, access_token: str):
    response = request_util.delete("https://api.spotify.com/v1/playlists/"+playlist_id+"/followers", access_token)
    return response.json()

def followedArtists(type: str, access_token: str, after: str = "", limit: int = None):
    params = {"type": type, "after": after, "limit": limit}
    response = request_util.get("https://api.spotify.com/v1/me/following", access_token, params=request_util.genParams(params))
    return response.json()

def followArtistsOrUsers(type: str, ids: list, access_token: str):
    params = {"type": type, "ids": ids}
    response = request_util.put("https://api.spotify.com/v1/me/following", access_token, params=params)
    return response.json()

def unfollowArtistsOrUsers(type: str, ids: list, access_token: str):
    params = {"type": type, "ids": ids}
    response = request_util.delete("https://api.spotify.com/v1/me/following", access_token, params=params)
    return response.json()

def followsArtistsOrUsers(type: str, ids: list, access_token: str):
    params = {"type": type, "ids": ids}
    response = request_util.get("https://api.spotify.com/v1/me/following/contains", access_token, params=request_util.genParams(params))
    return response.json()

def followsPlaylist(playlist_id: str, access_token: str):
    response = request_util.get("https://api.spotify.com/v1/playlists/"+playlist_id+"/followers/contains", access_token)
    return response.json()
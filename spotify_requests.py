import request_util
import math

# Tracks
def search(query: str, type: str, access_token: str):
    params = {"p": query, "type": type}
    response = request_util.get("https://api.spotify.com/v1/search", access_token, params=request_util.genParams(params))
    return response.json()

def track(id: str, access_token: str, market: str = ""):
    params = {"market": market}
    response = request_util.get("https://api.spotify.com/v1/tracks/"+id, access_token, params=request_util.genParams(params))
    return response.json()

def tracks(ids: list, access_token: str, market: str = ""):
    params = {"ids": ids, "market": market}
    response = request_util.get("https://api.spotify.com/v1/tracks", access_token, params=request_util.genParams(params))
    return response.json()

def audio_features(ids: list, access_token: str):
    params = {"ids": ids}
    response = request_util.get("https://api.spotify.com/v1/audio_features", access_token, params=request_util.genParams(params))
    return response.json()

def audio_features(id: str, access_token: str):
    response = request_util.get("https://api.spotify.com/v1/audio_features/"+id, access_token)
    return response.json()

def audio_analysis(id: str, access_token: str):
    response = request_util.get("https://api.spotify.com/v1/audio-analysis/"+id, access_token)
    return response.json()

def recommendations(access_token: str, limit: int = 10, market: str = "", seed_artists: str = "", seed_genres: str = "", seed_tracks: str = None, min_acousticness: float = None, 
                    max_acousticness: float = None, target_acousticness: float = None, min_danceability: float = None, max_danceability: float = None, 
                    target_danceability: float = None, min_duration_ms: int = None, max_duration_ms: int = None, target_duration_ms: int = None, 
                    min_energy: float = None, max_energy: float = None, target_energy: float = None, min_instrumentalness: float = None, 
                    max_instrumentalness: float = None, target_instrumentalness: float = None, min_key: float = None, max_key: float = None, 
                    target_key: float = None, min_liveness: float = None, max_liveness: float = None, target_liveness: float = None, min_loudness: float = None, 
                    max_loudness: float = None, target_loudness: float = None, min_mode: float = None, max_mode: float = None, target_mode: float = None, 
                    min_popularity: float = None, max_popularity: float = None, target_popularity: float = None, min_speechiness: float = None, 
                    max_speechiness: float = None, target_speechiness: float = None, min_tempomax_tempo: float = None, target_tempo: float = None, 
                    min_time_signature: float = None, max_time_signature: float = None, target_time_signature: float = None, min_valence: float = None, 
                    max_valence: float = None, target_valence: float = None):
    
    if seed_artists == "" and seed_genres == "" and seed_tracks == "":
        raise ValueError("Request must have a defined seed")
    
    params = {
        'limit': limit, 
        'market': market, 
        'seed_artists': seed_artists, 
        'seed_genres': seed_genres, 
        'seed_tracks': seed_tracks, 
        'min_acousticness': min_acousticness, 
        'max_acousticness': max_acousticness, 
        'target_acousticness': target_acousticness, 
        'min_danceability': min_danceability, 
        'max_danceability': max_danceability, 
        'target_danceability': target_danceability, 
        'min_duration_ms': min_duration_ms, 
        'max_duration_ms': max_duration_ms, 
        'target_duration_ms': target_duration_ms, 
        'min_energy': min_energy, 
        'max_energy': max_energy, 
        'target_energy': target_energy, 
        'min_instrumentalness': min_instrumentalness, 
        'max_instrumentalness': max_instrumentalness, 
        'target_instrumentalness': target_instrumentalness, 
        'min_key': min_key, 
        'max_key': max_key, 
        'target_key': target_key, 
        'min_liveness': min_liveness, 
        'max_liveness': max_liveness, 
        'target_liveness': target_liveness, 
        'min_loudness': min_loudness, 
        'max_loudness': max_loudness, 
        'target_loudness': target_loudness, 
        'min_mode': min_mode, 
        'max_mode': max_mode, 
        'target_mode': target_mode, 
        'min_popularity': min_popularity, 
        'max_popularity': max_popularity, 
        'target_popularity': target_popularity, 
        'min_speechiness': min_speechiness, 
        'max_speechiness': max_speechiness, 
        'target_speechiness': target_speechiness, 
        'min_tempomax_tempo': min_tempomax_tempo, 
        'target_tempo': target_tempo, 
        'min_time_signature': min_time_signature, 
        'max_time_signature': max_time_signature, 
        'target_time_signature': target_time_signature, 
        'min_valence': min_valence, 
        'max_valence': max_valence, 
        'target_valence': target_valence
    }
    
    response = request_util.get("https://api.spotify.com/v1/recommendations", access_token, params=request_util.genParams(params))
    return response.json()

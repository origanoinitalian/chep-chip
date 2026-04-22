import json
from fetcher import fetch_data

def parse_data(data):
    clean_data_dict = {
        "player_name": data["player"]["name"],
        "title": data["player"]["title"],
        "country": data["player"]["country"].split("/")[-1],  # Extract country code from URL
        "location": data["player"]["location"],
        "last_online": data["player"]["last_online"],
        "joined": data["player"]["joined"],
        "status": data["player"]["status"],
        "league": data["player"]["league"],
        "daily_rating": data["player_stats"]["chess_daily"]["last"]["rating"],
        "rapid_rating": data["player_stats"]["chess_rapid"]["last"]["rating"],
        "bullet_rating": data["player_stats"]["chess_bullet"]["last"]["rating"],
        "blitz_rating": data["player_stats"]["chess_blitz"]["last"]["rating"],
        "fide_rating": data["player_stats"]["fide"],
    }
    #print(clean_data_dict)
    json_data = json.dumps(clean_data_dict, indent=4)
    return json_data
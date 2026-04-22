import requests

def fetch_data():
    url_player="https://api.chess.com/pub/player/hikaru"
    url_player_stats = "https://api.chess.com/pub/player/hikaru/stats"

    try:
        headers = {
            "User-Agent": "My-chess-proj/1.0"
        }
        response_player = requests.get(url_player, headers=headers)
        response_player_stats = requests.get(url_player_stats, headers=headers)

        if response_player.status_code == 200 and response_player_stats.status_code == 200:
            data = {
                "player": response_player.json(),
                "player_stats": response_player_stats.json()
            }
            return data
        else:
            print('Error:', response_player.status_code)
            print('Error:', response_player_stats.status_code)
            return None
        
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None
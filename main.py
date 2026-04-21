import requests

def get_posts():
    url="https://api.chess.com/pub/player/hikaru"

    try:
        headers = {
            "User-Agent": "My-chess-proj/1.0"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            posts = response.json()
            return posts
        else:
            print('Error:', response.status_code)
            return None
        
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None

def main():
    posts = get_posts()
    if posts:
        print(posts)


if __name__ == "__main__":
    main()

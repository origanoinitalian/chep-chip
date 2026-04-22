from fetcher import fetch_data
from parser import parse_data

def main():
    data = fetch_data()
    parsed_data = parse_data(data)
    if parsed_data:
        print(parsed_data)


if __name__ == "__main__":
    main()

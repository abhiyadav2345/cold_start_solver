import requests
import time

def make_request(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Request successful: {response.status_code}")
        else:
            print(f"Request failed: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def main():
    url = "https://www.gardengro.in/"  # Replace with the target URL
    interval = 14 * 60  # 14 minutes in seconds

    while True:
        make_request(url)
        print(f"Waiting for {interval / 60} minutes before the next request...")
        time.sleep(interval)

if __name__ == "__main__":
    main()

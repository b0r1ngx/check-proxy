import requests


def check_proxy(proxy):
    try:
        response = requests.get('http://httpbin.org/ip', proxies={"http": proxy, "https": proxy}, timeout=5)
        if response.status_code == 200:
            print(f"Proxy {proxy} is working. Response: {response.json()}")
            return True
        else:
            print(f"Proxy {proxy} returned status code: {response.status_code}")
            return False

    except requests.exceptions.RequestException as e:
        print(f"Proxy {proxy} failed with exception: {e}")
        return False


proxy = 'http://username:password@proxy-server:port'
check_proxy(proxy)

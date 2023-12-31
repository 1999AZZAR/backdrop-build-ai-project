import requests


def send_request(session, proxy):
    try:
        response = session.get('http://httpbin.org/ip', proxies={'http': f"http://{proxy}"})
        print(response.json())
    except:
        pass


if __name__ == "__main__":
    with open('/media/azzar/Betha/Download/project/telegram bot/backdrop/proxy/http_proxies.txt', 'r') as file:
        proxies = file.readlines()

    with requests.Session() as session:
        for proxy in proxies:
            send_request(session, proxy)

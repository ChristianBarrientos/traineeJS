import requests

url = "http://api.isportsapi.com/sport/basketball/player?api_key=y1FTFuSbuo3NvLRU"



response = requests.request("GET", url)

print(response.text)
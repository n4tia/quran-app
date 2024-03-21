import requests,json,os
os.system('cls')


def get_api(url):
    api_get=requests.get(url)
    api=json.loads(api_get.content)
    return api
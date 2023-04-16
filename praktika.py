import json
import requests 
from urllib import parse


#constants
url = "http://api.giphy.com/v1/gifs/search"
api_key = "Qz67CcFnq7tnSy4xeFArMSoShTEvwPzZ"
           
def query(uri, method, kwargs=None):
    query = str(input('Введите запрос для поиска гифки: '))
    limit_per_page = str(input('Введите лимит на количество выдаваемых ссылок на гифки: '))
    params = parse.urlencode({
      "q": f'{query}',
      "api_key": f'{api_key}',
      "limit": f'{limit_per_page}'
    })
    with requests.request(method, uri + "?" + params) as result:
        if result.status_code != 200:
            return None
        return result.json()

def list_urls():
    result = query(url, "GET")
    res = result['data']
    dump = []
    domains = []
    if len(res) == 0:
        return "По запросу нет гифок"
    for i in res:
        if len(res) == 1:
            return i['bitly_gif_url']
        dump.append(i)
    for j in dump:
        domains.append(j['bitly_gif_url'])
    return domains

print(*list_urls(), sep='\n')

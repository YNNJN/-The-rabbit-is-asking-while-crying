import requests
from bs4 import BeautifulSoup

Servicekey = '04SY8J71WZ1Q1761IC2I'
base_url = 'http://api.koreafilm.or.kr/openapi-data2/wisenut/search_api/search_json2.jsp?collection=kmdb_new2'

url = base_url + f'&runtime=110&ServiceKey={Servicekey}'

response = requests.get(url)
response = response.text
data = BeautifulSoup(response, 'html.parser')
data = data['Result']

print(data)
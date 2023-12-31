import requests

page=2
response=requests.get(f'https://reqres.in/api/users/{page}')
if response.status_code==200:
    json_res=response.json()
    data=json_res['data']
    print(response.json())
    print(f'data -> {data}')
    support=json_res['support']
    support_url=support['url']
    print(f'support url --> {support_url}')
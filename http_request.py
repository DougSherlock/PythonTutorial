import requests

payload = {
    'username': 'corey',
    'password': 'testing'
}

# while True:    
search_term = 'humours' #input('Enter a search term or press the Enter key to quit: ')
# print(f'search_term:{search_term}')
if len(search_term) > 0:
    r = requests.get(f'https://thesession.org/tunes/search?format=json&q={search_term}')
    if (r.ok):
        result = r.json()
        # get only the fields we are interested in
        tunes = result['tunes']
        for tune in tunes:
            t = { k: v for k, v in tune.items() if k in {'id', 'name', 'type'} }
            print(t)
    else:
        print(f'HTTP Error: {r.reason}')


# r = requests.get('https://httpbin.org/basic-auth/doug/testing', timeout=3)
# r = requests.get('https://httpbin.org/get', params=payload)
# r = requests.post('https://httpbin.org/post', data=payload)

# print(r.text)
# r_dict = r.json()
# print(r_dict['form'])
# print(r.url)
# print(r.status_code)
# print(r.ok)
# print(r.headers)

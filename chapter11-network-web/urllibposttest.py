from urllib import request, parse

url = 'http://httpbin.org/post'

headers = {
    'User-agent': 'none/ofyourbusiness',
    'Spam': 'Eggs'
}

params = {
    'name1': 'value1',
    'name2': 'value2'
}

querystring = parse.urlencode(params)

req = request.Request(url, querystring.encode('ascii'), headers=headers)
u = request.urlopen(req)
resp = u.read()
print(resp)

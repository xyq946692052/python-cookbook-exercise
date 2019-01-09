import requests

url = 'http://httpbin.org/post'

files = {'file': ('data.text', open('data.text', 'rb'))}

r = requests.post(url, files=files)

import requests

# user agents
heads2 = [
    {
        'User-Agent':'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0',
        'Accept' : '*/*'
    },
    {
        'User-Agent':'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/105.0',
        'Accept' : '*/*'
    }]

req = requests.post('https://github.com',headers=heads2)
print(req)

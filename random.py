import random

users = [
    {
        'Mozilla/5.0' : '(Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Accept' : '*/*'
    },
    {
        'Mozilla/5.0' : '(Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
        'Accept' : '*/*'
    },
]

ran = random.choice(users)

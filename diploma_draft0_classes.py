from urllib.parse import urlencode
import requests
from pprint import pprint

# app_id = '7334295'
username = 'eshmargunov'
userid = '171691064'

token = '73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1'

class User:
    def __init__(self, token):
        self.token = token

    def get_params(self):
        return {
            'access_token': token,
            'user_id': userid,
            'v': 5.103
        }

    def get_friends(self):
        params = self.get_params()
        response = requests.get(
            'https://api.vk.com/method/friends.get',
            params
        )
        return response.json()

    def get_groups(self):
        params = self.get_params()
        params['extended'] = 0
        params['count'] = 200
        params['fields'] = ['name', 'members_count']

        response = requests.get(
            'https://api.vk.com/method/users.getSubscriptions',
            params
        )
        return response.json()

evgeniy = User(token)
friends = evgeniy.get_friends()
groups = evgeniy.get_groups()
pprint(friends)
pprint(groups)


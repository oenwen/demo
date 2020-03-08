import requests
from pprint import pprint
import time

token = '73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1'
userid = 18079762

def get_params():
    return {
        'access_token': token,
        'user_id': userid,
        'v': 5.103
    }

def get_groups():
    params = get_params()
    params['extended'] = 0
    print('*', 'запрашиваю список групп пользователя')
    response = requests.get(
        'https://api.vk.com/method/users.getSubscriptions',
        params
    )
    return response.json()


members_by_group = {}
groups_wo_friends = {}
groups = get_groups()
groups_list = groups['response']['groups']['items']
for group in groups_list:
    time.sleep(0.5)
    params = get_params()
    params['group_id'] = group
    # params['filter'] = 'friends'
    print(f'* ищу друзей в группе {group}')
    response = requests.get(
        'https://api.vk.com/method/groups.getMembers',
        params
    )

    members_by_group[group] = response.json()
    print(response.json())
    try:
        if members_by_group[group]['response']['count'] == 0:
            groups_wo_friends[group] = response.json()
    except KeyError:
        print('KeyError, line 40')
        pprint(members_by_group[group])

pprint(groups_wo_friends)


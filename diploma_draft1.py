# from urllib.parse import urlencode
import requests
from pprint import pprint
import time

# app_id = '7334295'
username = 'eshmargunov'
userid = '171691064'

token = '73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1'

def get_params():
    return {
        'access_token': token,
        'user_id': userid,
        'v': 5.103
    }

def get_friends():
    params = get_params()
    print('*','getting friends')
    response = requests.get(
        'https://api.vk.com/method/friends.get',
        params
    )
    return response.json()

def get_groups():
    params = get_params()
    params['extended'] = 0
    params['count'] = 200
    params['fields'] = ['name', 'members_count']
    print('*', 'getting groups')
    response = requests.get(
        'https://api.vk.com/method/users.getSubscriptions',
        params
    )
    return response.json()

members_by_group = {}
groups_wo_friends = {}
def get_members():
    groups = get_groups()
    groups_list = groups['response']['groups']['items']
    for group in groups_list:
        time.sleep(3)
        params = get_params()
        params['group_id'] = group
        params['filter'] = 'friends'
        print(f'* getting members of group {group}')
        response = requests.get(
            'https://api.vk.com/method/groups.getMembers',
            params
        )
        members_by_group[group] = response.json()
        if members_by_group[group]['response']['count'] == 0:
            groups_wo_friends[group] = response.json()

    # return members_by_group
    return groups_wo_friends

friends = get_friends()
friends_list = friends['response']['items']
groups = get_groups()
groups_list = groups['response']['groups']['items']
groups_wo_friends = get_members()
# pprint(friends_list)
# pprint(groups_list)
pprint(groups_wo_friends)
pprint(groups_wo_friends.keys())
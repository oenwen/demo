import requests
from pprint import pprint
import time

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

def get_members():
    members_by_group = {}
    groups_wo_friends = {}
    groups = get_groups()
    groups_list = groups['response']['groups']['items']
    for group in groups_list:
        time.sleep(0.34)
        params = get_params()
        params['group_id'] = group
        params['filter'] = 'friends'
        print(f'* ищу друзей в группе {group}')
        response = requests.get(
            'https://api.vk.com/method/groups.getMembers',
            params
        )
        members_by_group[group] = response.json()
        if members_by_group[group]['response']['count'] == 0:
            groups_wo_friends[group] = response.json()

    return groups_wo_friends

def groups_info():
    groups = {}
    groups_wo_friends = get_members()
    for group in list(groups_wo_friends.keys()):
        params = get_params()
        params['group_id'] = group
        params['fields'] = ['name', 'id', 'members_count']
        print(f'* запрашиваю информацию о группе {group}')
        time.sleep(0.34)
        response = requests.get(
            'https://api.vk.com/method/groups.getById',
            params
        )
        groups[group] = response.json()

    return groups

if __name__ == '__main__':
    token = '73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1'
    userid = input('Введите id пользователя Вконтакте ')  # 171691064 # 18079762
    groups = groups_info()
    pprint(groups)


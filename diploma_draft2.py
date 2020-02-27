import requests
from pprint import pprint
import time
import json

def get_params():
    return {
        'access_token': TOKEN,
        'user_id': userid,
        'v': 5.103
    }

def get_groups():
    params = get_params()
    params['extended'] = 0
    print('*', 'запрашиваю список групп пользователя')
    time.sleep(2)
    response = requests.get(
        'https://api.vk.com/method/users.getSubscriptions',
        params
    )
    return response.json()

def get_members(): # по умолчанию get members выдает первую 1000 участников, необходимо после этого установить параметр offset (сдвиг)
    # чтобы пересмотреть следующую 1000 и т. д. до конца группы
    members_by_group = {}
    groups_wo_friends = {}
    groups = get_groups()
    groups_list = groups['response']['groups']['items']

    # сначала пересмотреть группы без фильтра, установить количество участников, затем с фильтром по друзьям
    for group in groups_list:
        params = get_params()
        params['group_id'] = group
        params['filter'] = 'friends'
        print(f'* ищу друзей в группе {group}')
        time.sleep(2)
        response = requests.get(
            'https://api.vk.com/method/groups.getMembers',
            params
        )
        # time.sleep(0.5)
        members_by_group[group] = response.json()
        # проверить есть ли ключ response, если нет повторить запрос
        try:
            if members_by_group[group]['response']['count'] == 0:
                groups_wo_friends[group] = response.json()
        except KeyError:
            print('KeyError, line 40')
            pprint(members_by_group[group])

    return groups_wo_friends

def groups_info():
    groups = {}
    groups_wo_friends = get_members()
    for group in list(groups_wo_friends.keys()):
        params = get_params()
        params['group_id'] = group
        params['fields'] = ['name', 'id', 'members_count']
        print(f'* запрашиваю информацию о группе {group}')
        time.sleep(2)
        response = requests.get(
            'https://api.vk.com/method/groups.getById',
            params
        )
        # time.sleep(0.5)
        try:
            # проверить есть ли ключ response, если нет повторить запрос
            group_info = response.json()['response'][0]
            group_short_info = {'name': group_info['name'], 'gid': group_info['id'], 'members_count': group_info['members_count']}
            groups[group] = group_short_info
        except KeyError:
            print('KeyError, line 61')
            pprint(response.json())

    return groups

if __name__ == '__main__':
    TOKEN = '73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1'
    userid = input('Введите id пользователя Вконтакте ')  # 171691064 # 18079762 # 50469616
    groups = groups_info()
    with open('groups.json', 'w', encoding = 'utf8') as file:
        json.dump(groups, file, ensure_ascii = False, indent = 2)



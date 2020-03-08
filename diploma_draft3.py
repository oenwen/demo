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

def get_groups(): # выводит первые двести групп
    params = get_params()
    params['extended'] = 0
    print('Запрашиваю список групп пользователя')
    time.sleep(1)
    response = requests.get(
        'https://api.vk.com/method/users.getSubscriptions',
        params
    )
    return response.json()  # # {'response': {'groups': {'count': 112,
                    # 'items': [108972597, ...]

def get_members(): # по умолчанию get members выдает первую 1000 участников,
    # параметр offset позволяет пересмотреть следующую 1000 и т. д. до конца группы

    members_by_group = {}
    groups = get_groups()
    groups_list = groups['response']['groups']['items'] # список групп пользователя
    for group in groups_list:
        params = get_params()
        params['group_id'] = group
        params['offset'] = 0
        # params['filter'] = 'friends'
        print(f'Ищу участников группы {group}')
        time.sleep(0.5)
        response = requests.get(
            'https://api.vk.com/method/groups.getMembers',
            params
        )
        members_dict = response.json()['response']
        members_quantity = int(members_dict['count'])

        while len(members_dict['items']) < members_quantity:
            params['offset'] += 1000
            time.sleep(0.5)
            response2 = requests.get(
                'https://api.vk.com/method/groups.getMembers',
                params
            )
            try:
                response2.json().get('response')
                members_dict['items'] += response2.json()['response']['items']
                members_quantity = int(response2.json()['response']['count'])
                print('|', end = '')
            except KeyError:
                params['offset'] -= 1000
                continue

        members_by_group[group] = members_dict

    return members_by_group #{'group id': {'count':'', 'items': ''}}

def get_friends():
    friends_list = list()
    params = get_params()
    time.sleep(0.5)
    response = requests.get(
        'https://api.vk.com/method/friends.get',
        params
    )
    print('Запрашиваю список друзей')
    friends_list = response.json()['response']['items']
    return friends_list

def friends_in_groups():
    groups_wo_friends = {}
    friends_list = get_friends()
    members_by_group = get_members()
    for group in members_by_group.keys():
        counter = 0
        print('members_by_group[group][items]')
        print(members_by_group[group]['items'])
        for friend in friends_list:
            if friend not in members_by_group[group]['items']:
                counter += 1
        if counter > 0:
            groups_wo_friends[group] = {}
    return groups_wo_friends

def groups_info():
    groups = {}
    groups_wo_friends = friends_in_groups()
    for group in list(groups_wo_friends.keys()):
        params = get_params()
        params['group_id'] = group
        params['fields'] = ['name', 'id', 'members_count']
        print(f'Запрашиваю информацию о группе {group}')
        time.sleep(1)
        response = requests.get(
            'https://api.vk.com/method/groups.getById',
            params
        )

        try:
            # проверить есть ли ключ response, если нет повторить запрос
            group_info = response.json()['response'][0]
            group_short_info = {'name': group_info['name'], 'gid': group_info['id'], 'members_count': group_info['members_count']}
            groups[group] = group_short_info
        except KeyError:
            print('KeyError, line 126')
            pprint(response.json())

    return groups

if __name__ == '__main__':
    TOKEN = '73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1'
    userid = input('Введите id пользователя Вконтакте ')  # 171691064 # 18079762 # 50469616

    groups = groups_info()

    with open('groups.json', 'w', encoding = 'utf8') as file:
        json.dump(groups, file, ensure_ascii = False, indent = 2)





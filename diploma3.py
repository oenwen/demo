import requests
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
    time.sleep(1)
    response = requests.get(
        'https://api.vk.com/method/users.getSubscriptions',
        params
    )
    return response.json()

def get_members(): # по умолчанию get members выдает первую 1000 участников
    groups_wo_friends = {}
    groups = get_groups()
    groups_list = groups['response']['groups']['items']

    for group in groups_list:
        params = get_params()
        params['group_id'] = group
        params['filter'] = 'friends'
        print(f'* ищу друзей в группе {group}')
        time.sleep(0.5)
        response = requests.get(
            'https://api.vk.com/method/groups.getMembers',
            params
        )     
        if response.json()['response']['count'] == 0:                   groups_wo_friends[group] = response.json()
    return groups_wo_friends

def groups_info():
    groups = {}
    groups_wo_friends = get_members()
    for group in list(groups_wo_friends.keys()):
        params = get_params()
        params['group_id'] = group
        params['fields'] = ['name', 'id', 'members_count']
        print(f'* запрашиваю информацию о группе {group}')
        time.sleep(1)
        response = requests.get(
            'https://api.vk.com/method/groups.getById',
            params
        )     
        group_info = response.json()['response'][0]
        group_short_info = {'name': group_info['name'], 'gid': group_info['id'], 'members_count': group_info['members_count']}
        groups[group] = group_short_info  
    return groups

if __name__ == '__main__':
    TOKEN = '73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1'
    userid = input('Введите id пользователя Вконтакте ')  
    groups = groups_info()
    with open('groups.json', 'w', encoding = 'utf8') as file:
        json.dump(groups, file, ensure_ascii = False, indent = 2)

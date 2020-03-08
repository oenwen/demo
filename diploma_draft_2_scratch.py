from pprint import pprint
import requests
import time

TOKEN = '73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1'
userid = 171691064

params = {
        'access_token': TOKEN,
        'user_id': userid,
        'v': 5.103
    }

params_g = params
params_g['extended'] = 0
groups = requests.get(
        'https://api.vk.com/method/users.getSubscriptions',
        params_g)
groups_json = groups.json()
# pprint(groups_json) # {'response': {'groups': {'count': 112,
                    # 'items': [108972597, ...]

# def get_members(): # по умолчанию get members выдает первую 1000 участников, необходимо после этого установить параметр offset (сдвиг)
    # чтобы пересмотреть следующую 1000 и т. д. до конца группы

members_by_group = {}
# groups_wo_friends = {}
# groups = get_groups()
groups_list = groups_json['response']['groups']['items']  # список групп пользователя

# сначала пересмотреть группы без фильтра, установить количество участников, затем с фильтром по друзьям
for group in groups_list:
    params_l = params
    params_l['group_id'] = group
    params_l['offset'] = 0
    # params_l['filter'] = 'friends' # пересматривает только первую 1000 и выбирает френдов
    print(f'* ищу участников группы {group}')
    time.sleep(1)
    response = requests.get(
        'https://api.vk.com/method/groups.getMembers',
        params_l
    )

    members_dict = response.json()['response']

    members_quantity = int(members_dict['count'])
    # len(members_dict['items']) = len(members_dict['items'])

    while len(members_dict['items']) < members_quantity: # while при фильтре по друзьям не задействуется,
        # т.к. кол-во френдов из первой 1000 меньше 1000!
        params_l['offset'] += 1000
        time.sleep(0.5)
        response2 = requests.get(
            'https://api.vk.com/method/groups.getMembers',
            params_l
        )
        try:
            response2.json().get('response')
            members_dict['items'] += response2.json()['response']['items']
            members_quantity = int(response2.json()['response']['count'])
            print(response.json()['response'])
            print(response2.json()['response'])
            print(members_dict['count'])
            print(len(members_dict['items']))
            print(members_quantity, '- members quantity')
        except KeyError:
            print('KeyError')
            # print(response2.json())
            params_l['offset'] -= 1000
            continue


    members_by_group[group] = members_dict

pprint(members_dict)
#
#     try:
#         members_by_group[group] = response.json()['response']
#         # pprint(members_by_group[group])  # = {'count': 3076,
#         #                                        'items': [33903,....]
#         # members_quantity = int(members_by_group[group]['count'])  # число участников группы
#         print(len(
#             members_by_group[group]['items']
#         ))
#     except KeyError:
#         print('KeyError', response.json())
#
# for key, value in members_by_group:
#     try:
#         assert value['count'] == len('items')
#     except AssertionError:



# print(members_by_group.keys())

    #

    # # проверить есть ли ключ response, если нет повторить запрос
    # try:
    #     if members_by_group[group]['response']['count'] == 0:
    #         groups_wo_friends[group] = response.json()
    # except KeyError:
    #     print('KeyError, line 40')
    #     pprint(members_by_group[group])



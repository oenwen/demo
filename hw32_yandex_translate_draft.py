import requests
# import os
#  документация https://yandex.ru/dev/translate/doc/dg/reference/translate-docpage/

API_KEY = 'trnsl.1.1.20200216T103746Z.cea2650cfe7e2c45.81ed8cdb2c9de7d1e7030a2b2611f10bb4bbf176'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def sourse_file(path):
    file = open(path, encoding = 'utf8')
    sourse_text = file.read()
    file.close()
    # print(sourse_text)
    return sourse_text

def translate_it(text, to_lang):
    """
        https://translate.yandex.net/api/v1.5/tr.json/translate ?
        key=<API-ключ>
         & text=<переводимый текст>
         & lang=<направление перевода>
         & [format=<формат текста>]
         & [options=<опции перевода>]
         & [callback=<имя callback-функции>]
        :param to_lang:
        :return:
        """

    params = {
        'key': API_KEY,
        'text': text,
        'lang': 'fr-{}'.format(to_lang),
    }
    response = requests.get(URL, params=params)
    json_ = response.json()
    return ''.join(json_['text'])

def target_file(path):

    target_text = translate_it(text, 'ru')
    with open(path, 'w', encoding = 'utf8') as file:
        target_file = file.write(target_text)
    return(target_file)


if __name__ == '__main__':
    sourse_files = ['DE.txt', 'ES.txt', 'FR.txt']
    # target_files = ['DE-RU.txt', 'ES-RU.txt', 'FR-RU.txt']
    for f in sourse_files:
        text = sourse_file(f)


    target_file(f)

    # print(translate_it(text,'ru'))

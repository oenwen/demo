import requests
#  документация https://yandex.ru/dev/translate/doc/dg/reference/translate-docpage/

API_KEY = 'trnsl.1.1.20200216T103746Z.cea2650cfe7e2c45.81ed8cdb2c9de7d1e7030a2b2611f10bb4bbf176'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_it(path1, path2, lang, to_lang):
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
    with open (path1, encoding = 'utf8') as sourse_file:
        sourse_text = sourse_file.read()

    params = {
        'key': API_KEY,
        'text': sourse_text,
        'lang': '{}-{}'.format(lang, to_lang),
    }
    response = requests.get(URL, params=params)
    json_ = response.json()

    with open(path2, 'w', encoding = 'utf8') as target_file:
        target_file.write(''.join(json_['text']))

    return ''.join(json_['text'])

if __name__ == '__main__':
    for lang in ['de', 'es', 'fr']:
        path1 = '{}.txt'.format(lang)
        path2 = '{}-ru.txt'.format(lang)
        translate_it(path1, path2, lang,'ru')

import requests
#  документация https://yandex.ru/dev/translate/doc/dg/reference/translate-docpage/

API_KEY = 'trnsl.1.1.20200216T103746Z.cea2650cfe7e2c45.81ed8cdb2c9de7d1e7030a2b2611f10bb4bbf176' # мой
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

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
        'lang': 'ru-{}'.format(to_lang),
    }
    response = requests.get(URL, params=params)
    json_ = response.json()
    return ''.join(json_['text'])



# print(translate_it('В настоящее время доступна единственная опция — 
# признак включения в ответ автоматически определенного языка переводимого текста. Этому соответствует значение 1 этого параметра.', 'no'))

if __name__ == '__main__':
    print(translate_it('привет', 'en'))

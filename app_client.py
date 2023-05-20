import requests

params = {
    'user': '@avoid_the_void',
    'message': 'Hello, welcome to our bot',
    'btn': 'Go to bot',
    'link': '@BotFather',
    'name': 'd8b30cfc8fce07ef628a933007abcff4'
}
response = requests.post('http://localhost:3000/bot.site.ru/sendMessage', json=params)

'''params = {
    'group_name': 'Всем привет',
    'users': ['@ifbsvdz', '@soffitaa_s', '@avoid_the_void'],
    'message': 'Привет, можете ливать',
    'name': '768ad01dee5f9e97e8245482cefae053'
}
response = requests.post('http://localhost:3000/bot.site.ru/createGroup', json=params)'''

'''params = {
    'group_id': 1615064261,
    'name': '768ad01dee5f9e97e8245482cefae053'
}
response = requests.post('http://localhost:3000/bot.site.ru/deleteGroup', json=params)'''

'''params = {
    'api_id': 27620027,
    'api_hash': "e06096faec31a487eec67824842e227c"
}
response = requests.post('http://localhost:3000/bot.site.ru/authorize', json=params)'''


print(response.json())

from flask import Flask, request
from flask_restful import Api
from pyrogram import Client
from pyrogram.raw import functions
import secrets


app = Flask(__name__)
api = Api()


'''@app.post("/bot.site.ru/signUp")
async def signUp():
    try:
        data = request.get_json()
        api_id = data.get('api_id')
        api_hash = data.get('api_hash')
        phone_number = data.get('phone_number')
        token = secrets.token_hex(16)

        client = Client(f'{token}', api_id, api_hash)
        await client.connect()
        scode = await client.send_code(phone_number)
        await client.sign_in(phone_number, scode.phone_code_hash, code)
        return {
            "Status": "Success",
            "Token": token
        }
    except Exception as err:
        return {
            "Status": "Error",
            "Code": 400,
            "Error": f'{err}'
        }


@app.post("/bot.site.ru/confirm")
async def confirm():
    try:
        data = request.get_json()
        auth_token = request.headers.get('Authorization')
        code = data.get('code')
        token = data.get('token')
        phone_number = data.get('phone_number')


        client = Client(f'{token}')
        await client.sign_in(phone_number, )
        await client.sign_in(phone_number, scode.phone_code_hash, code)
        return {
            "Status": "Success",
            "Code": 200
        }
    except Exception as err:
        return {
            "Status": "Error",
            "Code": 400,
            "Error": f'{err}'
        }'''




@app.post("/bot.site.ru/authorize")
async def authorize():
    try:
        data = request.get_json()
        api_id = data.get('api_id')
        api_hash = data.get('api_hash')
        token = secrets.token_hex(16)
        async with Client(f'{token}', api_id, api_hash) as application:
            await application.send_message('me', "Ваш аккаунт был авторизован")
        return {
            "Status": "Success",
            "Token": token
        }
    except Exception as err:
        return {
            "Status": "Error",
            "Code": 400,
            "Error": f'{err}'
        }


@app.post("/bot.site.ru/sendMessage")
async def send_message():
    try:
        data = request.get_json()
        auth_token = request.headers.get('Authorization')
        user = data.get('user')
        message = data.get('message')
        btn = data.get('btn')
        link = data.get('link')
        async with Client(f"{auth_token}") as application:
            await application.send_message(user, f'{message}\n{btn}: {link}')
        return {
            "Status": "Success",
            "Code": 200
        }
    except Exception as err:
        return {
            "Status": "Error",
            "Code": 400,
            "Error": f'{err}'
        }


@app.post("/bot.site.ru/createGroup")
async def create_group():
    try:
        data = request.get_json()
        auth_token = request.headers.get('Authorization')
        group_name = data.get('group_name')
        users = data.get('users')
        message = data.get('message')
        async with Client(f"{auth_token}") as application:
            group = await application.create_group(group_name, users)
            await application.send_message(group.id, f'{message}')
            supergroup = await application.invoke(functions.messages.MigrateChat(chat_id=abs(group.id)))
        return {
            "Status": "Success",
            "Code": 200,
            "Group_id": supergroup.updates[0].channel_id
        }
    except Exception as err:
        return {
            "Status": "Error",
            "Code": 400,
            "Error": f'{err}'
        }


@app.post("/bot.site.ru/deleteGroup")
async def delete_group():
    try:
        data = request.get_json()
        auth_token = request.headers.get('Authorization')
        group_id = data.get('group_id')
        group_id = int('-100' + str(group_id))
        async with Client(f'{auth_token}') as application:
            await application.delete_supergroup(group_id)
        return {
            "Status": "Success",
            "Code": 200,
        }
    except Exception as err:
        return {
            "Status": "Error",
            "Code": 400,
            "Error": f'{err}'
        }

if __name__ == '__main__':
    app.run(host='0.0.0.0')
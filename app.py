from utils import *
import pandas as pd

async def add_user(request):

    try:

        data = [i for i in request.query.values()]
        token = data[-1]
        name, surname, login, password, date_of_birth, permission_user = data[:-1]

        assert len(data) == 7
        assert permission_user == 'administrator' or permission_user == 'readonly'

        current_id = decode_token(token)
        permission = get_permission_by_id(current_id)

        if permission:
            new_id = get_new_id()

            query_users = f"INSERT INTO public.users VALUES({new_id}, '{name}', '{surname}', '{login}', '{password}', date('{date_of_birth}'));"
            query_permissions = f"INSERT INTO public.permissions VALUES ({new_id}, '{permission_user}', '{login}')"
            data = make_request(db_pool, query_users)
            data = make_request(db_pool, query_permissions)
            return web.json_response(text=f'User {login} added successfuly.', status=200)

        else:
            return web.json_response(text='\nForbidden', status=401)

    except:
        return web.json_response(text=f'\nData of new user is unvalid.\n')

async def delete_user(request):
    data = [i for i in request.query.values()]
    login_to_delete, token = data
    id = decode_token(token)
    permission = get_permission_by_id(id)

    if permission:
        query = f"DELETE FROM public.users WHERE login='{login_to_delete}';"
        query_0 = f"DELETE FROM public.permissions WHERE login='{login_to_delete}';"

        make_request_wo_response(db_pool, query)
        make_request_wo_response(db_pool, query_0)

        return web.json_response(text=f'\nUser {login_to_delete} deleted successfully.\n')
    else:
        return web.json_response(text='\nForbidden', status=401)

async def read(request):
    token = request.query['token']
    id = decode_token(token)
    query = "SELECT * FROM public.users;"
    data = make_request(db_pool, query)

    df = pd.DataFrame(columns=['id', 'name', 'surname', 'login', 'password', 'date_of_birth'])
    for i in data:

        df.loc[len(df)]= i

    return web.json_response(text=f'\n{df}')

async def update(request):
    try:
        data = request.query
        parsed_fields = [i for i in request.query]
        login_to_update = data[f'{parsed_fields[0]}']
        token = data[f'{parsed_fields[-1]}']
        fields_to_update = parsed_fields[1:-1]

        assert len(fields_to_update) != 0

        current_id = decode_token(token)
        permission = get_permission_by_id(current_id)
        if permission:
            for field in fields_to_update:
                query = f"UPDATE users SET {field}='{data[f'{field}']}' WHERE login='{login_to_update}';"
                resp = make_request_wo_response(db_pool, query)
                return resp
           
        else:
            return web.json_response(text='\nForbidden', status=401)
    except:
        web.json_response(text='\nUnvalid data to update', status=401)



async def login(request):

    try:

        login = request.query['login']
        password = request.query['password']
        assert login != ''
        assert password != ''
    except:
        return web.json_response(text='Login or password is None')
    
    correct_password = check_correct_password(login, password)
    if correct_password:
        user_id = get_id_by_login(login)
        permission = get_permission_by_id(user_id)
        token = jwt.encode({'login':f'{login}', 'user_id': f'{user_id}', 'permission' : f'{permission}'}, "secret", algorithm='HS256')

        return web.json_response(text=f'\nSuccessful authorization!\n\nYour token:\n{token}')

    else:
        return web.json_response(text='\nWrong login or password. Please try again.', status=405)

if __name__ == '__main__':
    app = web.Application()

    app.router.add_route('POST','/login', login)
    app.router.add_route('POST','/create', add_user)
    app.router.add_route('DELETE','/delete', delete_user)
    app.router.add_route('GET', '/read', read)
    app.router.add_route('PUT', '/update', update)
    web.run_app(app, host='0.0.0.0', port='8080')

import sqlalchemy
from aiohttp import web
import jwt

db_pool = sqlalchemy.create_engine("postgresql://admin:admin@localhost/users_db", pool_size=200, max_overflow=0)

def decode_token(token):
    try:
        decoded_token = jwt.decode(token, "secret", algorithms=['HS256'])
        current_id = decoded_token['user_id']
        return current_id
    except:
        web.json_response(text='\nUnvalid token. Please check that you are authorized.', status=401)
def make_request(db_pool, query):
    with db_pool.connect() as connection:
        data = connection.execute(query)

        return data

def make_request_wo_response(db_pool, query):
    with db_pool.connect() as connection:
        connection.execute(query)

def get_password(db_pool, login):
    query = f"SELECT login, password FROM public.users WHERE login = '{login}';"

    data = make_request(db_pool, query)
    for i in data:
        user_password = i[-1]
    return user_password

def get_user_id(login):
    query = f"select id from public.users where login='{login}';"

    data = make_request(db_pool, query)

    for i in data:
        user_id = i[0]
    return user_id

def get_new_id():
    query = "SELECT COUNT (*) FROM public.users;"
    with db_pool.connect() as connection:
        data = connection.execute(query)
        for i in data:
            new_id = i[0]
        return new_id 

def get_id_by_login(login):
    query = f"SELECT id, login FROM users WHERE login = '{login}';"
    with db_pool.connect() as connection:
        data = connection.execute(query)
        for i in data:
            user_id = i[0]
        return user_id 


def get_permission_by_id(id):
    query = f"SELECT permission FROM public.permissions WHERE id = '{id}';"

    with db_pool.connect() as connection:
        data = connection.execute(query)
        for i in data:
            permission = i[0]
        
        if permission == 'administrator':
            permission = True
        else:
            permission = False 

def check_correct_password(login, password):
    user_password = get_password(db_pool, login)
    if user_password == password:
        return True
    else:
        return False
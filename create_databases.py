import sqlalchemy

db_pool = sqlalchemy.create_engine("postgresql://admin:admin@localhost/users_db", pool_size=200, max_overflow=0)
query_0 = "CREATE TABLE public.users (id int NULL, name varchar NULL, surname varchar NULL, login varchar NULL, password varchar NULL,	date_of_birth date NULL);"
query_1 = "INSERT INTO public.users VALUES(0,'admin','admin','admin','admin', date('1990-01-01'));"
query_2 = "CREATE TABLE public.permissions (id int NULL, permission varchar NULL, login varchar NULL);"
query_3 = "INSERT INTO public.permissions VALUES (0,'administrator','admin');"


queryes = [query_0, query_1, query_2, query_3]


db_pool = sqlalchemy.create_engine("postgresql://admin:admin@localhost/users_db", pool_size=200, max_overflow=0)
with db_pool.connect() as connection:
    for query in queryes:
        data = connection.execute(query)
